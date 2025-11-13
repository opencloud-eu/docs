Environment variables for the **policies** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`POLICIES_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|`127.0.0.1:9125`|
|`POLICIES_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9129`|
|`POLICIES_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`POLICIES_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`POLICIES_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`OC_EVENTS_ENDPOINT`<br/>`POLICIES_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|`127.0.0.1:9233`|
|`OC_EVENTS_CLUSTER`<br/>`POLICIES_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|`opencloud-cluster`|
|`OC_INSECURE`<br/>`POLICIES_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether the server should skip the client certificate verification during the TLS handshake.`|`false`|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`POLICIES_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided POLICIES_EVENTS_TLS_INSECURE will be seen as false.`|``|
|`OC_EVENTS_ENABLE_TLS`<br/>`POLICIES_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`false`|
|`OC_EVENTS_AUTH_USERNAME`<br/>`POLICIES_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_EVENTS_AUTH_PASSWORD`<br/>`POLICIES_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_LOG_LEVEL`<br/>`POLICIES_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`POLICIES_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`POLICIES_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`POLICIES_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`POLICIES_ENGINE_TIMEOUT`| 1.0.0 |Duration|`Sets the timeout the rego expression evaluation can take. Rules default to deny if the timeout was reached. See the Environment Variable Types description for more details.`|`10s`|
|`POLICIES_ENGINE_MIMES`| 1.0.0 |string|`Sets the mimes file path which maps mimetypes to associated file extensions. See the text description for details.`|``|
|`POLICIES_POSTPROCESSING_QUERY`| 1.0.0 |string|`Defines the 'Complete Rules' variable defined in the rego rule set this step uses for its evaluation. Defaults to deny if the variable was not found.`|``|
|`OC_TRACING_ENABLED`<br/>`POLICIES_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|`false`|
|`OC_TRACING_TYPE`<br/>`POLICIES_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`|``|
|`OC_TRACING_ENDPOINT`<br/>`POLICIES_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`|``|
|`OC_TRACING_COLLECTOR`<br/>`POLICIES_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`|``|
