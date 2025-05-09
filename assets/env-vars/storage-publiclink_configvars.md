Environment variables for the **storage-publiclink** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`STORAGE_PUBLICLINK_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`STORAGE_PUBLICLINK_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`STORAGE_PUBLICLINK_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`STORAGE_PUBLICLINK_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`STORAGE_PUBLICLINK_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`STORAGE_PUBLICLINK_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`STORAGE_PUBLICLINK_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`STORAGE_PUBLICLINK_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`STORAGE_PUBLICLINK_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9179|
|`STORAGE_PUBLICLINK_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`STORAGE_PUBLICLINK_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`STORAGE_PUBLICLINK_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`STORAGE_PUBLICLINK_GRPC_ADDR`| 1.0.0 |string|The bind address of the GRPC service.|127.0.0.1:9178|
|`OC_GRPC_PROTOCOL`<br/>`STORAGE_PUBLICLINK_GRPC_PROTOCOL`| 1.0.0 |string|The transport protocol of the GRPC service.|tcp|
|`OC_JWT_SECRET`<br/>`STORAGE_PUBLICLINK_JWT_SECRET`| 1.0.0 |string|The secret to mint and validate jwt tokens.||
|`OC_REVA_GATEWAY`| 1.0.0 |string|The CS3 gateway endpoint.|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.||
|`STORAGE_PUBLICLINK_SKIP_USER_GROUPS_IN_TOKEN`| 1.0.0 |bool|Disables the loading of user's group memberships from the reva access token.|false|
|`STORAGE_PUBLICLINK_STORAGE_PROVIDER_MOUNT_ID`| 1.0.0 |string|Mount ID of this storage. Admins can set the ID for the storage in this config option manually which is then used to reference the storage. Any reasonable long string is possible, preferably this would be an UUIDv4 format.|7993447f-687f-490d-875c-ac95e89a62a4|