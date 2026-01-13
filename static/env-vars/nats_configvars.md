Environment variables for the **nats** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`NATS_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|false|
|`OC_TRACING_TYPE`<br/>`NATS_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`||
|`OC_TRACING_ENDPOINT`<br/>`NATS_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`||
|`OC_TRACING_COLLECTOR`<br/>`NATS_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`||
|`OC_LOG_LEVEL`<br/>`NATS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`||
|`OC_LOG_PRETTY`<br/>`NATS_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|false|
|`OC_LOG_COLOR`<br/>`NATS_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|false|
|`OC_LOG_FILE`<br/>`NATS_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`||
|`NATS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9234|
|`NATS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`NATS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`NATS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`NATS_NATS_HOST`| 1.0.0 |string|`Bind address.`|127.0.0.1|
|`NATS_NATS_PORT`| 1.0.0 |int|`Bind port.`|9233|
|`NATS_NATS_CLUSTER_ID`| 1.0.0 |string|`ID of the NATS cluster.`|opencloud-cluster|
|`NATS_NATS_STORE_DIR`| 1.0.0 |string|`The directory where the filesystem storage will store NATS JetStream data. If not defined, the root directory derives from $OC_BASE_DATA_PATH/nats.`|/home/chaser/.opencloud/nats|
|`NATS_TLS_CERT`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the NATS listener. If not defined, the root directory derives from $OC_BASE_DATA_PATH/nats.`|/home/chaser/.opencloud/nats/tls.crt|
|`NATS_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the NATS listener. If not defined, the root directory derives from $OC_BASE_DATA_PATH/nats.`|/home/chaser/.opencloud/nats/tls.key|
|`OC_INSECURE`<br/>`NATS_TLS_SKIP_VERIFY_CLIENT_CERT`| 1.0.0 |bool|`Whether the NATS server should skip the client certificate verification during the TLS handshake.`|false|
|`OC_EVENTS_ENABLE_TLS`<br/>`NATS_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|false|
