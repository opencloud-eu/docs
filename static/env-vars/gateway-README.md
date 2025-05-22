# Gateway

The gateway service is responsible for passing requests to the storage providers. Other services never talk to the storage providers directly but will always send their requests via the `gateway` service.

## Caching

The gateway service is using caching as it is highly frequented with the same requests. As of now it uses two different caches:
  -   the `provider cache` is caching requests to list or get storage providers.
  -   the `create home cache` is caching requests to create personal spaces (as they only need to be executed once).

Both caches can be configured via the `OC_CACHE_*` envvars (or `GATEWAY_PROVIDER_CACHE_*` and `GATEWAY_CREATE_HOME_CACHE_*` respectively). See the [envvar section](/services/gateway/configuration/#environment-variables) for details.

Use `OC_CACHE_STORE` (`GATEWAY_PROVIDER_CACHE_STORE`, `GATEWAY_CREATE_HOME_CACHE_STORE`) to define the type of cache to use:
  -   `memory`: Basic in-memory store and the default.
  -   `redis-sentinel`: Stores data in a configured Redis Sentinel cluster.
  -   `nats-js-kv`: Stores data using key-value-store feature of [nats jetstream](https://docs.nats.io/nats-concepts/jetstream/key-value-store)
  -   `noop`: Stores nothing. Useful for testing. Not recommended in production environments.

Other store types may work but are not supported currently.

Note: The service can only be scaled if not using `memory` store and the stores are configured identically over all instances!

Note that if you have used one of the deprecated stores, you should reconfigure to one of the supported ones as the deprecated stores will be removed in a later version.

Store specific notes:
  -   When using `redis-sentinel`, the Redis master to use is configured via e.g. `OC_CACHE_STORE_NODES` in the form of `&lt;sentinel-host&gt;:&lt;sentinel-port&gt;/&lt;redis-master&gt;` like `10.10.0.200:26379/mymaster`.
  -   When using `nats-js-kv` it is recommended to set `OC_CACHE_STORE_NODES` to the same value as `OC_EVENTS_ENDPOINT`. That way the cache uses the same nats instance as the event bus.
  -   When using the `nats-js-kv` store, it is possible to set `OC_CACHE_DISABLE_PERSISTENCE` to instruct nats to not persist cache data on disc.

## Service Endpoints

**IMPORTANT**\
This functionality is currently highly experimental and intended for testing only! There are known bugs that need to be sorted out like not removing sockets when a service ends.

The gateway acts as a proxy for other CS3 services. As such it has to forward requests to a lot of services and needs to establish connections by looking up the IP address using the service registry. Instead of using the service registry each endpoint can also be configured to use the grpc `dns://` or `kubernetes://` URLs, which might be useful when running in kubernetes.

For a local single node deployment you might want to use `unix:` sockets as shown below. Using unix sockets will reduce the amount of service lookups and omit the TCP stack. For now, this is experimental and the services do not delete the socket on shutdown. PRs welcome.

The scheme for this setup is the following. Note that there is, except storage, always a service and a gateway envvar triple:

| **envvar** | **default** | **alternative** |
|------|------|------|
| OC_GRPC_PROTOCOL or &lt;br&gt; `&lt;service&gt;`_GRPC_PROTOCOL | tcp | unix |
| `&lt;service&gt;`_GRPC_ADDR | 127.0.0.1:`&lt;port&gt;` | /var/run/opencloud/`&lt;service&gt;`.sock |
| GATEWAY_`&lt;service&gt;`_ENDPOINT | eu.opencloud.api.`&lt;service&gt;` | unix:/var/run/opencloud/`&lt;service&gt;`.sock &lt;br&gt; dns: ... &lt;br&gt; kubernetes: ... |

```console
USERS_GRPC_PROTOCOL=unix"
USERS_GRPC_ADDR=/var/run/opencloud/users.sock"
GATEWAY_USERS_ENDPOINT=unix:/var/run/opencloud/users.sock"

GROUPS_GRPC_PROTOCOL=unix"
GROUPS_GRPC_ADDR=/var/run/opencloud/groups.sock"
GATEWAY_GROUPS_ENDPOINT=unix:/var/run/opencloud/groups.sock"

AUTH_APP_GRPC_PROTOCOL=unix"
AUTH_APP_GRPC_ADDR=/var/run/opencloud/auth-app.sock"
GATEWAY_AUTH_APP_ENDPOINT=unix:/var/run/opencloud/auth-app.sock"

AUTH_BASIC_GRPC_PROTOCOL=unix"
AUTH_BASIC_GRPC_ADDR=/var/run/opencloud/auth-basic.sock"
GATEWAY_AUTH_BASIC_ENDPOINT=unix:/var/run/opencloud/auth-basic.sock"

AUTH_MACHINE_GRPC_PROTOCOL=unix"
AUTH_MACHINE_GRPC_ADDR=/var/run/opencloud/auth-machine.sock"
GATEWAY_AUTH_MACHINE_ENDPOINT=unix:/var/run/opencloud/auth-machine.sock"

AUTH_SERVICE_GRPC_PROTOCOL=unix"
AUTH_SERVICE_GRPC_ADDR=/var/run/opencloud/auth-service.sock"
GATEWAY_AUTH_SERVICE_ENDPOINT=unix:/var/run/opencloud/auth-service.sock"

STORAGE_PUBLIC_LINK_GRPC_PROTOCOL=unix"
STORAGE_PUBLIC_LINK_GRPC_ADDR=/var/run/opencloud/storage-public-link.sock"
GATEWAY_STORAGE_PUBLIC_LINK_ENDPOINT=unix:/var/run/opencloud/storage-public-link.sock"

STORAGE_USERS_GRPC_PROTOCOL=unix"
STORAGE_USERS_GRPC_ADDR=/var/run/opencloud/storage-users.sock"
GATEWAY_STORAGE_USERS_ENDPOINT=unix:/var/run/opencloud/storage-users.sock"
// graph sometimes bypasses the gateway so we need to configure the socket here as wel
GRAPH_SPACES_STORAGE_USERS_ADDRESS=unix:/var/run/opencloud/storage-users.sock"

STORAGE_SHARES_GRPC_PROTOCOL=unix"
STORAGE_SHARES_GRPC_ADDR=/var/run/opencloud/storage-shares.sock"
GATEWAY_STORAGE_SHARES_ENDPOINT=unix:/var/run/opencloud/storage-shares.sock"

APP_REGISTRY_GRPC_PROTOCOL=unix"
APP_REGISTRY_GRPC_ADDR=/var/run/opencloud/app-registry.sock"
GATEWAY_APP_REGISTRY_ENDPOINT=unix:/var/run/opencloud/app-registry.sock"

OCM_GRPC_PROTOCOL=unix"
OCM_GRPC_ADDR=/var/run/opencloud/ocm.sock"
GATEWAY_OCM_ENDPOINT=unix:/var/run/opencloud/ocm.sock"

// storage related
SETTINGS_STORAGE_GATEWAY_GRPC_ADDR="unix:/var/run/opencloud/storage-system.sock"
SETTINGS_STORAGE_GRPC_ADDR="unix:/var/run/opencloud/storage-system.sock"
STORAGE_SYSTEM_GRPC_PROTOCOL="unix"
STORAGE_SYSTEM_GRPC_ADDR="/var/run/opencloud/storage-system.sock"
SHARING_USER_CS3_PROVIDER_ADDR="unix:/var/run/opencloud/storage-system.sock"
SHARING_USER_JSONCS3_PROVIDER_ADDR="unix:/var/run/opencloud/storage-system.sock"
SHARING_PUBLIC_CS3_PROVIDER_ADDR="unix:/var/run/opencloud/storage-system.sock"
SHARING_PUBLIC_JSONCS3_PROVIDER_ADDR="unix:/var/run/opencloud/storage-system.sock"
```

## Storage Registry

In order to add another storage provider the CS3 storage registry that is running as part of the CS3 gateway hes to be made aware of it. The easiest cleanest way to do it is to set `GATEWAY_STORAGE_REGISTRY_CONFIG_JSON=/path/to/storages.json` and list all storage providers like this:

```json
&#123;
  "eu.opencloud.api.storage-users": &#123;
    "providerid": "&#123;storage-users-mount-uuid&#125;",
    "spaces": &#123;
      "personal": &#123;
        "mount_point":   "/users",
        "path_template": "/users/&#123;&#123;.Space.Owner.Id.OpaqueId&#125;&#125;"
      &#125;,
      "project": &#123;
        "mount_point":   "/projects",
        "path_template": "/projects/&#123;&#123;.Space.Name&#125;&#125;"
      &#125;
    &#125;
  &#125;,
  "eu.opencloud.api.storage-shares": &#123;
    "providerid": "a0ca6a90-a365-4782-871e-d44447bbc668",
    "spaces": &#123;
      "virtual": &#123;
        "mount_point": "/users/&#123;&#123;.CurrentUser.Id.OpaqueId&#125;&#125;/Shares"
      &#125;,
      "grant": &#123;
        "mount_point": "."
      &#125;,
      "mountpoint": &#123;
        "mount_point":   "/users/&#123;&#123;.CurrentUser.Id.OpaqueId&#125;&#125;/Shares",
        "path_template": "/users/&#123;&#123;.CurrentUser.Id.OpaqueId&#125;&#125;/Shares/&#123;&#123;.Space.Name&#125;&#125;"
      &#125;
    &#125;
  &#125;,
  "eu.opencloud.api.storage-publiclink": &#123;
    "providerid": "7993447f-687f-490d-875c-ac95e89a62a4",
    "spaces": &#123;
      "grant": &#123;
        "mount_point": "."
      &#125;,
      "mountpoint": &#123;
        "mount_point":   "/public",
        "path_template": "/public/&#123;&#123;.Space.Root.OpaqueId&#125;&#125;"
      &#125;
    &#125;
  &#125;,
  "eu.opencloud.api.ocm": &#123;
    "providerid": "89f37a33-858b-45fa-8890-a1f2b27d90e1",
    "spaces": &#123;
      "grant": &#123;
        "mount_point": "."
      &#125;,
      "mountpoint": &#123;
        "mount_point":   "/ocm",
        "path_template": "/ocm/&#123;&#123;.Space.Root.OpaqueId&#125;&#125;"
      &#125;
    &#125;
  &#125;,
  "eu.opencloud.api.storage-hello": &#123;
    "providerid": "hello-storage-id",
    "spaces": &#123;
      "project": &#123;
        "mount_point":   "/hello",
        "path_template": "/hello/&#123;&#123;.Space.Name&#125;&#125;"
      &#125;
    &#125;
  &#125;
&#125;
```

In the above replace `&#123;storage-users-mount-uuid&#125;` with the mount UUID that was generated for the storage-users service. You can find it in the `config.yaml` generated on by `opencloud init`. The last entry `eu.opencloud.api.storage-hello` and its `providerid` `"hello-storage-id"` are an example for in additional storage provider, in this case running `hellofs`, an example minimal storage driver.
