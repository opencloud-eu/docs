# OCM

The `ocm` service provides federated sharing functionality based on the [sciencemesh](https://sciencemesh.io/) and [ocm](https://github.com/cs3org/OCM-API) HTTP APIs. Internally the `ocm` service consists of the following services and endpoints:

External HTTP APIs:
* sciencemesh: serves the API for the invitation workflow
* ocmd: serves the API for managing federated shares

Internal GRPC APIs:
* ocmproviderauthorizer: manages the list of trusted providers and verifies requests
* ocminvitemanager: manages the list and state of invite tokens
* ocmshareprovider: manages ocm shares on the sharer
* ocmcore: used for creating federated shares on the receiver side
* authprovider: authenticates webdav requests using the ocm share tokens

## Enable OCM

To enable OpenCloudMesh, you have to set the following environment variable.

```console
OC_ENABLE_OCM=true
```

## Trust Between Instances

The `ocm` services implements an invitation workflow which needs to be followed before creating federated shares. Invitations are limited to trusted instances, however.

The list of trusted instances is managed by the `ocmproviderauthorizer` service. The only supported backend currently is `json` which stores the list in a json file on disk. Note that the `ocmproviders.json` file, which holds that configuration, is expected to be located in the root of the OpenCloud config directory if not otherwise defined. See the `OCM_OCM_PROVIDER_AUTHORIZER_PROVIDERS_FILE` envvar for more details.

When all instances of a federation should trust each other, an `ocmproviders.json` file like this can be used for all instances:
```json
[
    &#123;
        "name": "OpenCloud Test 1",
        "full_name": "OpenCloud Test provider 1",
        "organization": "OpenCloud One",
        "domain": "cloud1.opencloud.test",
        "homepage": "https://cloud1.opencloud.test",
        "description": "First OpenCloud Example cloud storage",
        "services": [
            &#123;
                "endpoint": &#123;
                    "type": &#123;
                        "name": "OCM",
                        "description": "cloud1.opencloud.test Open Cloud Mesh API"
                    &#125;,
                    "name": "cloud1.opencloud.test - OCM API",
                    "path": "https://cloud1.opencloud.test/ocm/",
                    "is_monitored": true
                &#125;,
                "api_version": "0.0.1",
                "host": "http://cloud1.opencloud.test"
            &#125;,
            &#123;
                "endpoint": &#123;
                    "type": &#123;
                        "name": "Webdav",
                        "description": "cloud1.opencloud.test Webdav API"
                    &#125;,
                    "name": "cloud1.opencloud.test Example - Webdav API",
                    "path": "https://cloud1.opencloud.test/dav/",
                    "is_monitored": true
                &#125;,
                "api_version": "0.0.1",
                "host": "https://cloud1.opencloud.test/"
            &#125;
        ]
    &#125;,
    &#123;
        "name": "OpenCloud Test 2",
        "full_name": "OpenCloud Test provider 2",
        "organization": "OpenCloud Two",
        "domain": "cloud2.opencloud.test",
        "homepage": "https://cloud2.opencloud.test",
        "description": "Second OpenCloud Example cloud storage",
        "services": [
            &#123;
                "endpoint": &#123;
                    "type": &#123;
                        "name": "OCM",
                        "description": "cloud2.opencloud.test Open Cloud Mesh API"
                    &#125;,
                    "name": "cloud2.opencloud.test - OCM API",
                    "path": "https://cloud2.opencloud.test/ocm/",
                    "is_monitored": true
                &#125;,
                "api_version": "0.0.1",
                "host": "http://cloud2.opencloud.test"
            &#125;,
            &#123;
                "endpoint": &#123;
                    "type": &#123;
                        "name": "Webdav",
                        "description": "cloud2.opencloud.test Webdav API"
                    &#125;,
                    "name": "cloud2.opencloud.test Example - Webdav API",
                    "path": "https://cloud2.opencloud.test/dav/",
                    "is_monitored": true
                &#125;,
                "api_version": "0.0.1",
                "host": "https://cloud2.opencloud.test/"
            &#125;
        ]
    &#125;
]
```

&#123;&#123;&lt; hint info &gt;&#125;&#125;
Note: the `domain` must not contain the protocol as it has to match the [GOCDB site object domain](https://developer.sciencemesh.io/docs/technical-documentation/central-database/#site-object).
&#123;&#123;&lt; /hint &gt;&#125;&#125;

The above federation consists of two instances: `cloud1.opencloud.test` and `cloud2.opencloud.test` that can use the Invitation workflow described below to generate, send and accept invitations.

## Invitation Workflow

Before sharing a resource with a remote user this user has to be invited by the sharer.

In order to do so a POST request is sent to the `generate-invite` endpoint of the sciencemesh API. The generated token is passed on to the receiver, who will then use the `accept-invite` endpoint to accept the invitation. As a result remote users will be added to the `ocminvitemanager` on both sides. See [invitation flow](invitation_flow) for the according sequence diagram.

The data backend of the `ocminvitemanager` is configurable. The only supported backend currently is `json` which stores the data in a json file on disk.

## Creating Shares

&#123;&#123;&lt; hint info &gt;&#125;&#125;
The below info is outdated as we allow creating federated shares using the graph API. Clients can now discover the available sharing roles and invite federated users using the graph API.
&#123;&#123;&lt; /hint &gt;&#125;&#125;

OCM Shares are currently created using the ocs API, just like regular shares. The difference is the share type, which is 6 (ShareTypeFederatedCloudShare) in this case, and a few additional parameters required for identifying the remote user.

See [Create share flow](create_share_flow) for the according sequence diagram.

The data backends of the `ocmshareprovider` and `ocmcore` services are configurable. The only supported backend currently is `json` which stores the data in a json file on disk.
