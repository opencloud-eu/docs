Environment variables for the **invitations** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`INVITATIONS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|`error`|
|`INVITATIONS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9269`|
|`INVITATIONS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`INVITATIONS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`INVITATIONS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`INVITATIONS_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`127.0.0.1:9265`|
|`INVITATIONS_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`/graph/v1.0`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`INVITATIONS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`[https://localhost:9200]`|
|`OC_CORS_ALLOW_METHODS`<br/>`INVITATIONS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`[]`|
|`OC_CORS_ALLOW_HEADERS`<br/>`INVITATIONS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`[]`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`INVITATIONS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`false`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`false`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|``|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|``|
|`OC_KEYCLOAK_BASE_PATH`<br/>`INVITATIONS_KEYCLOAK_BASE_PATH`| 1.0.0 |string|`The URL to access keycloak.`|``|
|`OC_KEYCLOAK_CLIENT_ID`<br/>`INVITATIONS_KEYCLOAK_CLIENT_ID`| 1.0.0 |string|`The client ID to authenticate with keycloak.`|``|
|`OC_KEYCLOAK_CLIENT_SECRET`<br/>`INVITATIONS_KEYCLOAK_CLIENT_SECRET`| 1.0.0 |string|`The client secret to use in authentication.`|``|
|`OC_KEYCLOAK_CLIENT_REALM`<br/>`INVITATIONS_KEYCLOAK_CLIENT_REALM`| 1.0.0 |string|`The realm the client is defined in.`|``|
|`OC_KEYCLOAK_USER_REALM`<br/>`INVITATIONS_KEYCLOAK_USER_REALM`| 1.0.0 |string|`The realm users are defined.`|``|
|`OC_KEYCLOAK_INSECURE_SKIP_VERIFY`<br/>`INVITATIONS_KEYCLOAK_INSECURE_SKIP_VERIFY`| 1.0.0 |bool|`Disable TLS certificate validation for Keycloak connections. Do not set this in production environments.`|`false`|
|`OC_JWT_SECRET`<br/>`INVITATIONS_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`|``|
