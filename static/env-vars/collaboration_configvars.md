Environment variables for the **collaboration** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`COLLABORATION_SERVICE_NAME`| 3.6.0 |string|`The name of the service which is registered. You only need to change this when more than one collaboration service is needed.`|collaboration|
|`COLLABORATION_APP_NAME`| 1.0.0 |string|`The name of the app which is shown to the user. You can chose freely but you are limited to a single word without special characters or whitespaces. We recommend to use pascalCase like 'CollaboraOnline'.`|Collabora|
|`COLLABORATION_APP_PRODUCT`| 1.0.0 |string|`The WebOffice app, either Collabora, OnlyOffice, Microsoft365 or MicrosoftOfficeOnline.`||
|`COLLABORATION_APP_DESCRIPTION`| 1.0.0 |string|`App description`|Open office documents with Collabora|
|`COLLABORATION_APP_ICON`| 1.0.0 |string|`Icon for the app`|image-edit|
|`COLLABORATION_APP_ADDR`| 1.0.0 |string|`The URL where the WOPI app is located, such as \https://127.0.0.1:8080.`|https://127.0.0.1:9980|
|`COLLABORATION_APP_INSECURE`| 1.0.0 |bool|`Skip TLS certificate verification when connecting to the WOPI app`|false|
|`COLLABORATION_APP_PROOF_DISABLE`| 1.0.0 |bool|`Disable the proof keys verification`|false|
|`COLLABORATION_APP_PROOF_DURATION`| 1.0.0 |string|`Duration for the proof keys to be cached in memory, using time.ParseDuration format. If the duration can't be parsed, we'll use the default 12h as duration`|12h|
|`COLLABORATION_APP_LICENSE_CHECK_ENABLE`| 1.0.0 |bool|`Enable license checking to edit files. Needs to be enabled when using Microsoft365 with the business flow.`|false|
|`OC_PERSISTENT_STORE`<br/>`COLLABORATION_STORE`| 1.0.0 |string|`The type of the store. Supported values are: 'memory', 'nats-js-kv', 'redis-sentinel', 'noop'. See the text description for details.`|nats-js-kv|
|`OC_PERSISTENT_STORE_NODES`<br/>`COLLABORATION_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|[127.0.0.1:9233]|
|`COLLABORATION_STORE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|collaboration|
|`COLLABORATION_STORE_TABLE`| 1.0.0 |string|`The database table the store should use.`||
|`OC_PERSISTENT_STORE_TTL`<br/>`COLLABORATION_STORE_TTL`| 1.0.0 |Duration|`Time to live for events in the store. Defaults to '30m' (30 minutes). See the Environment Variable Types description for more details.`|30m0s|
|`OC_PERSISTENT_STORE_AUTH_USERNAME`<br/>`COLLABORATION_STORE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_PERSISTENT_STORE_AUTH_PASSWORD`<br/>`COLLABORATION_STORE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_JWT_SECRET`<br/>`COLLABORATION_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`||
|`COLLABORATION_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|127.0.0.1:9301|
|`OC_GRPC_PROTOCOL`<br/>`COLLABORATION_GRPC_PROTOCOL`| 1.0.0 |string|`The transport protocol of the GRPC service.`|tcp|
|`COLLABORATION_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|127.0.0.1:9300|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|false|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`||
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`||
|`COLLABORATION_WOPI_SRC`| 1.0.0 |string|`The WOPI source base URL containing schema, host and port. Set this to the schema and domain where the collaboration service is reachable for the wopi app, such as \https://office.example.test.`|https://localhost:9300|
|`COLLABORATION_WOPI_SECRET`| 1.0.0 |string|`Used to mint and verify WOPI JWT tokens and encrypt and decrypt the REVA JWT token embedded in the WOPI JWT token.`||
|`COLLABORATION_WOPI_DISABLE_CHAT`<br/>`OC_WOPI_DISABLE_CHAT`| 1.0.0 |bool|`Disable chat in the office web frontend. This feature applies to OnlyOffice and Microsoft.`|false|
|`COLLABORATION_WOPI_PROXY_URL`| 1.0.0 |string|`The URL to the OpenCloud WOPI proxy. Optional. To use this feature, you need an office365 proxy subscription. If you become part of the Microsoft CSP program (\https://learn.microsoft.com/en-us/partner-center/enroll/csp-overview), you can use WebOffice without a proxy.`||
|`COLLABORATION_WOPI_PROXY_SECRET`| 1.0.0 |string|`Optional, the secret to authenticate against the OpenCloud WOPI proxy. This secret can be obtained from OpenCloud via the office365 proxy subscription.`||
|`COLLABORATION_WOPI_SHORTTOKENS`| 1.0.0 |bool|`Use short access tokens for WOPI access. This is useful for office packages, like Microsoft Office Online, which have URL length restrictions. If enabled, a persistent store must be configured.`|false|
|`OC_REVA_GATEWAY`| 1.0.0 |string|`CS3 gateway used to look up user metadata.`|eu.opencloud.api.gateway|
|`COLLABORATION_CS3API_DATAGATEWAY_INSECURE`| 1.0.0 |bool|`Connect to the CS3API data gateway insecurely.`|false|
|`COLLABORATION_CS3API_APP_REGISTRATION_INTERVAL`| next |Duration|`The interval at which the app provider registers itself.`|30s|
|`OC_TRACING_ENABLED`<br/>`COLLABORATION_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|false|
|`OC_TRACING_TYPE`<br/>`COLLABORATION_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`||
|`OC_TRACING_ENDPOINT`<br/>`COLLABORATION_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`||
|`OC_TRACING_COLLECTOR`<br/>`COLLABORATION_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`||
|`OC_LOG_LEVEL`<br/>`COLLABORATION_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`||
|`OC_LOG_PRETTY`<br/>`COLLABORATION_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|false|
|`OC_LOG_COLOR`<br/>`COLLABORATION_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|false|
|`OC_LOG_FILE`<br/>`COLLABORATION_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`||
|`COLLABORATION_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9304|
|`COLLABORATION_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`COLLABORATION_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`COLLABORATION_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
