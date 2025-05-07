Environment variables for the **clientlog** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`CLIENTLOG_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`CLIENTLOG_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`CLIENTLOG_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`CLIENTLOG_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`CLIENTLOG_USERLOG_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`CLIENTLOG_USERLOG_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`CLIENTLOG_USERLOG_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`CLIENTLOG_USERLOG_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`CLIENTLOG_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9260|
|`CLIENTLOG_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`CLIENTLOG_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`CLIENTLOG_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`OC_JWT_SECRET`<br/>`CLIENTLOG_JWT_SECRET`| 1.0.0 |string|The secret to mint and validate jwt tokens.||
|`OC_REVA_GATEWAY`| 1.0.0 |string|CS3 gateway used to look up user metadata|eu.opencloud.api.gateway|
|`OC_EVENTS_ENDPOINT`<br/>`CLIENTLOG_EVENTS_ENDPOINT`| 1.0.0 |string|The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`CLIENTLOG_EVENTS_CLUSTER`| 1.0.0 |string|The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.|opencloud-cluster|
|`OC_INSECURE`<br/>`CLIENTLOG_EVENTS_TLS_INSECURE`| 1.0.0 |bool|Whether to verify the server TLS certificates.|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`CLIENTLOG_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|The root CA certificate used to validate the server's TLS certificate. If provided NOTIFICATIONS_EVENTS_TLS_INSECURE will be seen as false.||
|`OC_EVENTS_ENABLE_TLS`<br/>`CLIENTLOG_EVENTS_ENABLE_TLS`| 1.0.0 |bool|Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`CLIENTLOG_EVENTS_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`CLIENTLOG_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_SERVICE_ACCOUNT_ID`<br/>`CLIENTLOG_SERVICE_ACCOUNT_ID`| 1.0.0 |string|The ID of the service account the service should use. See the 'auth-service' service description for more details.||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`CLIENTLOG_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|The service account secret.||