Environment variables for the **settings** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`SETTINGS_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|false|
|`OC_TRACING_TYPE`<br/>`SETTINGS_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`||
|`OC_TRACING_ENDPOINT`<br/>`SETTINGS_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`||
|`OC_TRACING_COLLECTOR`<br/>`SETTINGS_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`||
|`OC_LOG_LEVEL`<br/>`SETTINGS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`||
|`OC_LOG_PRETTY`<br/>`SETTINGS_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|false|
|`OC_LOG_COLOR`<br/>`SETTINGS_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|false|
|`OC_LOG_FILE`<br/>`SETTINGS_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`||
|`SETTINGS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9194|
|`SETTINGS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`SETTINGS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`SETTINGS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`SETTINGS_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|127.0.0.1:9190|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|false|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`||
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`||
|`SETTINGS_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|/|
|`OC_CORS_ALLOW_ORIGINS`<br/>`SETTINGS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|[*]|
|`OC_CORS_ALLOW_METHODS`<br/>`SETTINGS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|[GET POST PUT PATCH DELETE OPTIONS]|
|`OC_CORS_ALLOW_HEADERS`<br/>`SETTINGS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`SETTINGS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|true|
|`SETTINGS_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|127.0.0.1:9191|
|`SETTINGS_STORAGE_GATEWAY_GRPC_ADDR`<br/>`STORAGE_GATEWAY_GRPC_ADDR`| 1.0.0 |string|`GRPC address of the STORAGE-SYSTEM service.`|eu.opencloud.api.storage-system|
|`SETTINGS_STORAGE_GRPC_ADDR`<br/>`STORAGE_GRPC_ADDR`| 1.0.0 |string|`GRPC address of the STORAGE-SYSTEM service.`|eu.opencloud.api.storage-system|
|`OC_SYSTEM_USER_ID`<br/>`SETTINGS_SYSTEM_USER_ID`| 1.0.0 |string|`ID of the OpenCloud STORAGE-SYSTEM system user. Admins need to set the ID for the STORAGE-SYSTEM system user in this config option which is then used to reference the user. Any reasonable long string is possible, preferably this would be an UUIDv4 format.`||
|`OC_SYSTEM_USER_IDP`<br/>`SETTINGS_SYSTEM_USER_IDP`| 1.0.0 |string|`IDP of the OpenCloud STORAGE-SYSTEM system user.`|internal|
|`OC_SYSTEM_USER_API_KEY`| 1.0.0 |string|`API key for the STORAGE-SYSTEM system user.`||
|`OC_CACHE_STORE`<br/>`SETTINGS_CACHE_STORE`| 1.0.0 |string|`The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.`|memory|
|`OC_CACHE_STORE_NODES`<br/>`SETTINGS_CACHE_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|[127.0.0.1:9233]|
|`OC_CACHE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|settings-cache|
|`SETTINGS_FILE_CACHE_TABLE`| 1.0.0 |string|`The database table the store should use for the file cache.`|settings_files|
|`SETTINGS_DIRECTORY_CACHE_TABLE`| 1.0.0 |string|`The database table the store should use for the directory cache.`|settings_dirs|
|`OC_CACHE_TTL`<br/>`SETTINGS_CACHE_TTL`| 1.0.0 |Duration|`Default time to live for entries in the cache. Only applied when access tokens has no expiration. See the Environment Variable Types description for more details.`|10m0s|
|`OC_CACHE_DISABLE_PERSISTENCE`<br/>`SETTINGS_CACHE_DISABLE_PERSISTENCE`| 1.0.0 |bool|`Disables persistence of the cache. Only applies when store type 'nats-js-kv' is configured. Defaults to false.`|false|
|`OC_CACHE_AUTH_USERNAME`<br/>`SETTINGS_CACHE_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured.`||
|`OC_CACHE_AUTH_PASSWORD`<br/>`SETTINGS_CACHE_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured.`||
|`SETTINGS_BUNDLES_PATH`| 1.0.0 |string|`The path to a JSON file with a list of bundles. If not defined, the default bundles will be loaded.`||
|`OC_ADMIN_USER_ID`<br/>`SETTINGS_ADMIN_USER_ID`| 1.0.0 |string|`ID of the user that should receive admin privileges. Consider that the UUID can be encoded in some LDAP deployment configurations like in .ldif files. These need to be decoded beforehand.`||
|`OC_JWT_SECRET`<br/>`SETTINGS_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`||
|`IDM_CREATE_DEMO_USERS`<br/>`SETTINGS_SETUP_DEFAULT_ASSIGNMENTS`| 1.0.0 |bool|`The default role assignments the demo users should be setup.`|false|
|`SETTINGS_SERVICE_ACCOUNT_IDS`<br/>`OC_SERVICE_ACCOUNT_ID`| 1.0.0 |[]string|`The list of all service account IDs. These will be assigned the hidden 'service-account' role. Note: When using 'OC_SERVICE_ACCOUNT_ID' this will contain only one value while 'SETTINGS_SERVICE_ACCOUNT_IDS' can have multiple. See the 'auth-service' service description for more details about service accounts.`|[service-user-id]|
|`OC_DEFAULT_LANGUAGE`| 1.0.0 |string|`The default language used by services and the WebUI. If not defined, English will be used as default. See the documentation for more details.`||
|`OC_TRANSLATION_PATH`<br/>`SETTINGS_TRANSLATION_PATH`| 1.0.0 |string|`(optional) Set this to a path with custom translations to overwrite the builtin translations. Note that file and folder naming rules apply, see the documentation for more details.`||
