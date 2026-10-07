## Environment variables for the **auth-guest** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`AUTH_GUEST_LOG_LEVEL`| next |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|`"error"`|
|`AUTH_GUEST_DEBUG_ADDR`| next |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`"127.0.0.1:9267"`|
|`AUTH_GUEST_DEBUG_TOKEN`| next |string|`Token to secure the metrics endpoint.`|`""`|
|`AUTH_GUEST_DEBUG_PPROF`| next |bool|`Enables pprof, which can be used for profiling.`|`"false"`|
|`AUTH_GUEST_DEBUG_ZPAGES`| next |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`"false"`|
|`AUTH_GUEST_EVENTS_DISABLED`| next |bool|`Disables listening for events. Set this to true if the service should only handle HTTP requests.`|`"false"`|
|`OC_EVENTS_ENDPOINT`| next |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|`"127.0.0.1:9233"`|
|`OC_EVENTS_CLUSTER`| next |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|`"opencloud-cluster"`|
|`OC_INSECURE`<br/>`OC_EVENTS_TLS_INSECURE`| next |bool|`Whether to verify the server TLS certificates.`|`"false"`|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`| next |string|`The root CA certificate used to validate the server's TLS certificate. If provided AUTH_GUEST_EVENTS_TLS_INSECURE will be seen as false.`|`""`|
|`OC_EVENTS_ENABLE_TLS`| next |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`"false"`|
|`OC_EVENTS_AUTH_USERNAME`| next |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`""`|
|`OC_EVENTS_AUTH_PASSWORD`| next |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|`""`|
|`OC_REVA_GATEWAY`| next |string|`CS3 gateway used to look up user metadata`|`"eu.opencloud.api.gateway"`|
|`AUTH_GUEST_GRPC_ADDR`| next |string|`The bind address of the GRPC service.`|`"127.0.0.1:9268"`|
|`OC_GRPC_PROTOCOL`<br/>`AUTH_GUEST_GRPC_PROTOCOL`| next |string|`The transport protocol of the GRPC service.`|`"tcp"`|
|`AUTH_GUEST_HTTP_DISABLED`| next |bool|`Disables the HTTP service. Set this to true if the service should only handle events.`|`"false"`|
|`AUTH_GUEST_HTTP_ADDR`| next |string|`The bind address of the HTTP service.`|`"127.0.0.1:9266"`|
|`AUTH_GUEST_HTTP_ROOT`| next |string|`Subdirectory that serves as the root for this HTTP service.`|`"/graph"`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`AUTH_GUEST_CORS_ALLOW_ORIGINS`| next |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`"[*]"`|
|`OC_CORS_ALLOW_METHODS`<br/>`AUTH_GUEST_CORS_ALLOW_METHODS`| next |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`"[GET POST PUT PATCH DELETE]"`|
|`OC_CORS_ALLOW_HEADERS`<br/>`AUTH_GUEST_CORS_ALLOW_HEADERS`| next |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`"[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Ocs-Apirequest]"`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`AUTH_GUEST_CORS_ALLOW_CREDENTIALS`| next |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`"true"`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`"false"`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|`""`|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|`""`|
|`AUTH_GUEST_TOKENS_STORAGE_ROOT`| next |string|`The directory where the guest share tokens are stored. If not defined, the root directory derives from $OC_BASE_DATA_PATH/auth-guest.`|`"/var/lib/opencloud/auth-guest"`|
|`OC_JWT_SECRET`<br/>`AUTH_GUEST_JWT_SECRET`| next |string|`The secret to mint and validate jwt tokens.`|`""`|
|`AUTH_GUEST_SESSION_JWT_SECRET`| next |string|`The secret used to sign and validate guest session tokens. It must differ from OC_JWT_SECRET.`|`""`|
|`AUTH_GUEST_JWT_COOKIE_NAME`| next |string|`The name of the session cookie set when a guest token is redeemed.`|`"__Host-oc_guest_session"`|
|`AUTH_GUEST_JWT_TTL`| next |Duration|`The lifetime of a redeemed guest session token.`|`"24h0m0s"`|
|`OC_SERVICE_ACCOUNT_ID`<br/>`AUTH_GUEST_SERVICE_ACCOUNT_ID`| next |string|`The ID of the service account the service should use. See the 'auth-service' service description for more details.`|`""`|
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`AUTH_GUEST_SERVICE_ACCOUNT_SECRET`| next |string|`The service account secret.`|`""`|
|`AUTH_GUEST_NUM_CONSUMERS`| next |int|`The amount of concurrent event consumers to start. Event consumers are used for processing events. Multiple consumers increase parallelisation, but will also increase CPU and memory demands.`|`"1"`|
