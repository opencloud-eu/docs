Environment variables for the **postprocessing** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`POSTPROCESSING_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`POSTPROCESSING_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`POSTPROCESSING_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`POSTPROCESSING_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`POSTPROCESSING_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9255`|
|`POSTPROCESSING_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`POSTPROCESSING_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`POSTPROCESSING_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`OC_PERSISTENT_STORE`<br/>`POSTPROCESSING_STORE`| 1.0.0 |string|`The type of the store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.`|`nats-js-kv`|
|`OC_PERSISTENT_STORE_NODES`<br/>`POSTPROCESSING_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|`[127.0.0.1:9233]`|
|`POSTPROCESSING_STORE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|`postprocessing`|
|`POSTPROCESSING_STORE_TABLE`| 1.0.0 |string|`The database table the store should use.`|``|
|`OC_PERSISTENT_STORE_TTL`<br/>`POSTPROCESSING_STORE_TTL`| 1.0.0 |Duration|`Time to live for events in the store. See the Environment Variable Types description for more details.`|`0s`|
|`OC_PERSISTENT_STORE_AUTH_USERNAME`<br/>`POSTPROCESSING_STORE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`|``|
|`OC_PERSISTENT_STORE_AUTH_PASSWORD`<br/>`POSTPROCESSING_STORE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`|``|
|`OC_EVENTS_ENDPOINT`<br/>`POSTPROCESSING_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|`127.0.0.1:9233`|
|`OC_EVENTS_CLUSTER`<br/>`POSTPROCESSING_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|`opencloud-cluster`|
|`OC_INSECURE`<br/>`POSTPROCESSING_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether the OpenCloud server should skip the client certificate verification during the TLS handshake.`|`false`|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`POSTPROCESSING_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided POSTPROCESSING_EVENTS_TLS_INSECURE will be seen as false.`|``|
|`OC_EVENTS_ENABLE_TLS`<br/>`POSTPROCESSING_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`false`|
|`OC_EVENTS_AUTH_USERNAME`<br/>`POSTPROCESSING_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_EVENTS_AUTH_PASSWORD`<br/>`POSTPROCESSING_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`SEARCH_EVENTS_MAX_ACK_PENDING`| 4.0.0 |int|`The maximum number of unacknowledged messages. This is used to limit the number of messages that can be in flight at the same time.`|`10000`|
|`SEARCH_EVENTS_ACK_WAIT`| 4.0.0 |Duration|`The time to wait for an ack before the message is redelivered. This is used to ensure that messages are not lost if the consumer crashes.`|`1m0s`|
|`POSTPROCESSING_WORKERS`| 1.0.0 |int|`The number of concurrent go routines that fetch events from the event queue.`|`3`|
|`POSTPROCESSING_STEPS`| 1.0.0 |[]string|`A list of postprocessing steps processed in order of their appearance. Currently supported values by the system are: 'virusscan', 'policies' and 'delay'. Custom steps are allowed. See the documentation for instructions. See the Environment Variable Types description for more details.`|`[]`|
|`POSTPROCESSING_DELAY`| 1.0.0 |Duration|`After uploading a file but before making it available for download, a delay step can be added. Intended for developing purposes only. If a duration is set but the keyword 'delay' is not explicitely added to 'POSTPROCESSING_STEPS', the delay step will be processed as last step. In such a case, a log entry will be written on service startup to remind the admin about that situation. See the Environment Variable Types description for more details.`|`0s`|
|`POSTPROCESSING_RETRY_BACKOFF_DURATION`| 1.0.0 |Duration|`The base for the exponential backoff duration before retrying a failed postprocessing step. See the Environment Variable Types description for more details.`|`5s`|
|`POSTPROCESSING_MAX_RETRIES`| 1.0.0 |int|`The maximum number of retries for a failed postprocessing step.`|`14`|
