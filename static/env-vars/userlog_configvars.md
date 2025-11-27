Environment variables for the **userlog** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_LOG_LEVEL`<br/>`USERLOG_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`USERLOG_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`USERLOG_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`USERLOG_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`USERLOG_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9214`|
|`USERLOG_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`USERLOG_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`USERLOG_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`USERLOG_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`127.0.0.1:9210`|
|`USERLOG_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`/`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`USERLOG_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`[*]`|
|`OC_CORS_ALLOW_METHODS`<br/>`USERLOG_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`[GET]`|
|`OC_CORS_ALLOW_HEADERS`<br/>`USERLOG_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Ocs-Apirequest]`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`USERLOG_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`true`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`false`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|``|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|``|
|`OC_JWT_SECRET`<br/>`USERLOG_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`|``|
|`OC_REVA_GATEWAY`| 1.0.0 |string|`CS3 gateway used to look up user metadata`|`eu.opencloud.api.gateway`|
|`OC_TRANSLATION_PATH`<br/>`USERLOG_TRANSLATION_PATH`| 1.0.0 |string|`(optional) Set this to a path with custom translations to overwrite the builtin translations. Note that file and folder naming rules apply, see the documentation for more details.`|``|
|`OC_DEFAULT_LANGUAGE`| 1.0.0 |string|`The default language used by services and the WebUI. If not defined, English will be used as default. See the documentation for more details.`|``|
|`OC_EVENTS_ENDPOINT`<br/>`USERLOG_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|`127.0.0.1:9233`|
|`OC_EVENTS_CLUSTER`<br/>`USERLOG_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|`opencloud-cluster`|
|`OC_INSECURE`<br/>`USERLOG_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|`false`|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`USERLOG_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided NOTIFICATIONS_EVENTS_TLS_INSECURE will be seen as false.`|``|
|`OC_EVENTS_ENABLE_TLS`<br/>`USERLOG_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`false`|
|`OC_EVENTS_AUTH_USERNAME`<br/>`USERLOG_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_EVENTS_AUTH_PASSWORD`<br/>`USERLOG_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_MAX_CONCURRENCY`<br/>`USERLOG_MAX_CONCURRENCY`| 1.0.0 |int|`Maximum number of concurrent go-routines. Higher values can potentially get work done faster but will also cause more load on the system. Values of 0 or below will be ignored and the default value will be used.`|`1`|
|`OC_PERSISTENT_STORE`<br/>`USERLOG_STORE`| 1.0.0 |string|`The type of the store. Supported values are: 'memory', 'nats-js-kv', 'redis-sentinel', 'noop'. See the text description for details.`|`memory`|
|`OC_PERSISTENT_STORE_NODES`<br/>`USERLOG_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|`[]`|
|`USERLOG_STORE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|`userlog`|
|`USERLOG_STORE_TABLE`| 1.0.0 |string|`The database table the store should use.`|`events`|
|`OC_PERSISTENT_STORE_TTL`<br/>`USERLOG_STORE_TTL`| 1.0.0 |Duration|`Time to live for events in the store. Defaults to '336h' (2 weeks). See the Environment Variable Types description for more details.`|`336h0m0s`|
|`OC_PERSISTENT_STORE_AUTH_USERNAME`<br/>`USERLOG_STORE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`|``|
|`OC_PERSISTENT_STORE_AUTH_PASSWORD`<br/>`USERLOG_STORE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`|``|
|`OC_DISABLE_SSE,USERLOG_DISABLE_SSE`| 1.0.0 |bool|`Disables server-sent events (sse). When disabled, clients will no longer receive sse notifications.`|`false`|
|`USERLOG_GLOBAL_NOTIFICATIONS_SECRET`| 1.0.0 |string|`The secret to secure the global notifications endpoint. Only system admins and users knowing that secret can call the global notifications POST/DELETE endpoints.`|``|
|`OC_SERVICE_ACCOUNT_ID`<br/>`USERLOG_SERVICE_ACCOUNT_ID`| 1.0.0 |string|`The ID of the service account the service should use. See the 'auth-service' service description for more details.`|``|
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`USERLOG_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|`The service account secret.`|``|
