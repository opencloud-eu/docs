Environment variables for the **sse** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`SSE_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`SSE_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`SSE_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`SSE_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`SSE_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9139`|
|`SSE_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`SSE_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`SSE_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`SSE_KEEPALIVE_INTERVAL`| 1.0.0 |Duration|`To prevent intermediate proxies from closing the SSE connection, send periodic SSE comments to keep it open.`|`0s`|
|`OC_EVENTS_ENDPOINT`<br/>`SSE_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|`127.0.0.1:9233`|
|`OC_EVENTS_CLUSTER`<br/>`SSE_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|`opencloud-cluster`|
|`OC_INSECURE`<br/>`OC_EVENTS_TLS_INSECURE`<br/>`SSE_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|`false`|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`SSE_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided SSE_EVENTS_TLS_INSECURE will be seen as false.`|``|
|`OC_EVENTS_ENABLE_TLS`<br/>`SSE_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`false`|
|`OC_EVENTS_AUTH_USERNAME`<br/>`SSE_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`OC_EVENTS_AUTH_PASSWORD`<br/>`SSE_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|``|
|`SSE_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`127.0.0.1:9135`|
|`SSE_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`/`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`SSE_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`[*]`|
|`OC_CORS_ALLOW_METHODS`<br/>`SSE_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`[GET]`|
|`OC_CORS_ALLOW_HEADERS`<br/>`SSE_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Ocs-Apirequest]`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`SSE_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`true`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`false`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|``|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|``|
|`OC_JWT_SECRET`<br/>`SSE_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`|``|
