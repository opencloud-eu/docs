Environment variables for the **eventhistory** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_LOG_LEVEL`<br/>`EVENTHISTORY_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|error|
|`EVENTHISTORY_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9270|
|`EVENTHISTORY_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`EVENTHISTORY_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`EVENTHISTORY_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`EVENTHISTORY_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|127.0.0.1:9274|
|`OC_EVENTS_ENDPOINT`<br/>`EVENTHISTORY_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`EVENTHISTORY_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|opencloud-cluster|
|`OC_INSECURE`<br/>`OC_EVENTS_TLS_INSECURE`<br/>`EVENTHISTORY_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`EVENTHISTORY_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. Will be seen as empty if NOTIFICATIONS_EVENTS_TLS_INSECURE is provided.`||
|`OC_EVENTS_ENABLE_TLS`<br/>`EVENTHISTORY_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`EVENTHISTORY_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`EVENTHISTORY_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_PERSISTENT_STORE`<br/>`EVENTHISTORY_STORE`| 1.0.0 |string|`The type of the store. Supported values are: 'memory', 'nats-js-kv', 'redis-sentinel', 'noop'. See the text description for details.`|nats-js-kv|
|`OC_PERSISTENT_STORE_NODES`<br/>`EVENTHISTORY_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|[127.0.0.1:9233]|
|`EVENTHISTORY_STORE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|eventhistory|
|`EVENTHISTORY_STORE_TABLE`| 1.0.0 |string|`The database table the store should use.`||
|`OC_PERSISTENT_STORE_TTL`<br/>`EVENTHISTORY_STORE_TTL`| 1.0.0 |Duration|`Time to live for events in the store. Defaults to '336h' (2 weeks). See the Environment Variable Types description for more details.`|336h0m0s|
|`OC_PERSISTENT_STORE_AUTH_USERNAME`<br/>`EVENTHISTORY_STORE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_PERSISTENT_STORE_AUTH_PASSWORD`<br/>`EVENTHISTORY_STORE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
