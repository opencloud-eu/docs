Environment variables for the **ocs** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_LOG_LEVEL`<br/>`OCS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|error|
|`OCS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9114|
|`OCS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`OCS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`OCS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`OCS_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|127.0.0.1:9110|
|`OCS_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|/ocs|
|`OC_CORS_ALLOW_ORIGINS`<br/>`OCS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|[*]|
|`OC_CORS_ALLOW_METHODS`<br/>`OCS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|[GET POST PUT PATCH DELETE OPTIONS]|
|`OC_CORS_ALLOW_HEADERS`<br/>`OCS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Cache-Control]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`OCS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|true|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|false|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`||
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`||
|`OC_CACHE_STORE`<br/>`OCS_PRESIGNEDURL_SIGNING_KEYS_STORE`| 1.0.0 |string|`The type of the signing key store. Supported values are: 'redis-sentinel' and 'nats-js-kv'. See the text description for details.`|nats-js-kv|
|`OC_CACHE_STORE_NODES`<br/>`OCS_PRESIGNEDURL_SIGNING_KEYS_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|[127.0.0.1:9233]|
|`OC_CACHE_TTL`<br/>`OCS_PRESIGNEDURL_SIGNING_KEYS_STORE_TTL`| 1.0.0 |Duration|`Default time to live for signing keys. See the Environment Variable Types description for more details.`|12h0m0s|
|`OC_CACHE_AUTH_USERNAME`<br/>`OCS_PRESIGNEDURL_SIGNING_KEYS_STORE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_CACHE_AUTH_PASSWORD`<br/>`OCS_PRESIGNEDURL_SIGNING_KEYS_STORE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_JWT_SECRET`<br/>`OCS_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`||
