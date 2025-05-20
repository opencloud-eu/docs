Environment variables for the **audit** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`AUDIT_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`AUDIT_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`AUDIT_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`AUDIT_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`AUDIT_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`AUDIT_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`AUDIT_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`AUDIT_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`AUDIT_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9229|
|`AUDIT_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`AUDIT_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`AUDIT_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`OC_EVENTS_ENDPOINT`<br/>`AUDIT_EVENTS_ENDPOINT`| 1.0.0 |string|The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`AUDIT_EVENTS_CLUSTER`| 1.0.0 |string|The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.|opencloud-cluster|
|`OC_INSECURE`<br/>`AUDIT_EVENTS_TLS_INSECURE`| 1.0.0 |bool|Whether to verify the server TLS certificates.|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`AUDIT_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|The root CA certificate used to validate the server's TLS certificate. If provided AUDIT_EVENTS_TLS_INSECURE will be seen as false.||
|`OC_EVENTS_ENABLE_TLS`<br/>`AUDIT_EVENTS_ENABLE_TLS`| 1.0.0 |bool|Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`AUDIT_EVENTS_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`AUDIT_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`AUDIT_LOG_TO_CONSOLE`| 1.0.0 |bool|Logs to stdout if set to 'true'. Independent of the LOG_TO_FILE option.|true|
|`AUDIT_LOG_TO_FILE`| 1.0.0 |bool|Logs to file if set to 'true'. Independent of the LOG_TO_CONSOLE option.|false|
|`AUDIT_FILEPATH`| 1.0.0 |string|Filepath of the logfile. Mandatory if LOG_TO_FILE is set to 'true'.||
|`AUDIT_FORMAT`| 1.0.0 |string|Log format. Supported values are '' (empty) and 'json'. Using 'json' is advised, '' (empty) renders the 'minimal' format. See the text description for more details.|json|