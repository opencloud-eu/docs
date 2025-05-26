Environment variables for the **notifications** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`NOTIFICATIONS_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`NOTIFICATIONS_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`NOTIFICATIONS_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`NOTIFICATIONS_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`NOTIFICATIONS_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`NOTIFICATIONS_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`NOTIFICATIONS_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`NOTIFICATIONS_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`NOTIFICATIONS_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9174|
|`NOTIFICATIONS_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`NOTIFICATIONS_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`NOTIFICATIONS_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`OC_URL`<br/>`NOTIFICATIONS_WEB_UI_URL`| 1.0.0 |string|The public facing URL of the OpenCloud Web UI, used e.g. when sending notification eMails|https://localhost:9200|
|`NOTIFICATIONS_SMTP_HOST`| 1.0.0 |string|SMTP host to connect to.||
|`NOTIFICATIONS_SMTP_PORT`| 1.0.0 |int|Port of the SMTP host to connect to.|0|
|`NOTIFICATIONS_SMTP_SENDER`| 1.0.0 |string|`Sender address of emails that will be sent (e.g. 'OpenCloud <noreply@example.com>').`||
|`NOTIFICATIONS_SMTP_USERNAME`| 1.0.0 |string|Username for the SMTP host to connect to.||
|`NOTIFICATIONS_SMTP_PASSWORD`| 1.0.0 |string|Password for the SMTP host to connect to.||
|`NOTIFICATIONS_SMTP_INSECURE`| 1.0.0 |bool|Allow insecure connections to the SMTP server.|false|
|`NOTIFICATIONS_SMTP_AUTHENTICATION`| 1.0.0 |string|Authentication method for the SMTP communication. Possible values are 'login', 'plain', 'crammd5', 'none' or 'auto'. If set to 'auto' or unset, the authentication method is automatically negotiated with the server.||
|`NOTIFICATIONS_SMTP_ENCRYPTION`| 1.0.0 |string|Encryption method for the SMTP communication. Possible values are 'starttls', 'ssltls' and 'none'.|none|
|`OC_EVENTS_ENDPOINT`<br/>`NOTIFICATIONS_EVENTS_ENDPOINT`| 1.0.0 |string|The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`NOTIFICATIONS_EVENTS_CLUSTER`| 1.0.0 |string|The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.|opencloud-cluster|
|`OC_INSECURE`<br/>`NOTIFICATIONS_EVENTS_TLS_INSECURE`| 1.0.0 |bool|Whether to verify the server TLS certificates.|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`NOTIFICATIONS_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|The root CA certificate used to validate the server's TLS certificate. If provided NOTIFICATIONS_EVENTS_TLS_INSECURE will be seen as false.||
|`OC_EVENTS_ENABLE_TLS`<br/>`NOTIFICATIONS_EVENTS_ENABLE_TLS`| 1.0.0 |bool|Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`NOTIFICATIONS_EVENTS_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`NOTIFICATIONS_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EMAIL_TEMPLATE_PATH`<br/>`NOTIFICATIONS_EMAIL_TEMPLATE_PATH`| 1.0.0 |string|Path to Email notification templates overriding embedded ones.||
|`OC_TRANSLATION_PATH`<br/>`NOTIFICATIONS_TRANSLATION_PATH`| 1.0.0 |string|(optional) Set this to a path with custom translations to overwrite the builtin translations. Note that file and folder naming rules apply, see the documentation for more details.||
|`OC_DEFAULT_LANGUAGE`| 1.0.0 |string|The default language used by services and the WebUI. If not defined, English will be used as default. See the documentation for more details.||
|`OC_REVA_GATEWAY`| 1.0.0 |string|CS3 gateway used to look up user metadata|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.||
|`OC_SERVICE_ACCOUNT_ID`<br/>`NOTIFICATIONS_SERVICE_ACCOUNT_ID`| 1.0.0 |string|The ID of the service account the service should use. See the 'auth-service' service description for more details.||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`NOTIFICATIONS_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|The service account secret.||
|`OC_PERSISTENT_STORE`<br/>`NOTIFICATIONS_STORE`| 1.0.0 |string|The type of the store. Supported values are: 'memory', 'nats-js-kv', 'redis-sentinel', 'noop'. See the text description for details.|nats-js-kv|
|`OC_PERSISTENT_STORE_NODES`<br/>`NOTIFICATIONS_STORE_NODES`| 1.0.0 |[]string|A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.|[127.0.0.1:9233]|
|`NOTIFICATIONS_STORE_DATABASE`| 1.0.0 |string|The database name the configured store should use.|notifications|
|`NOTIFICATIONS_STORE_TABLE`| 1.0.0 |string|The database table the store should use.||
|`OC_PERSISTENT_STORE_TTL`<br/>`NOTIFICATIONS_STORE_TTL`| 1.0.0 |Duration|Time to live for notifications in the store. Defaults to '336h' (2 weeks). See the Environment Variable Types description for more details.|336h0m0s|
|`OC_PERSISTENT_STORE_AUTH_USERNAME`<br/>`NOTIFICATIONS_STORE_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.||
|`OC_PERSISTENT_STORE_AUTH_PASSWORD`<br/>`NOTIFICATIONS_STORE_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.||