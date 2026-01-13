Environment variables for the **webfinger** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`WEBFINGER_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|`error`|
|`WEBFINGER_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9279`|
|`WEBFINGER_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`WEBFINGER_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`WEBFINGER_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`WEBFINGER_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`127.0.0.1:9275`|
|`WEBFINGER_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`/`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`WEBFINGER_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`[https://localhost:9200]`|
|`OC_CORS_ALLOW_METHODS`<br/>`WEBFINGER_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`[]`|
|`OC_CORS_ALLOW_HEADERS`<br/>`WEBFINGER_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`[]`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`WEBFINGER_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`false`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`false`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|``|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|``|
|`WEBFINGER_RELATIONS`| 1.0.0 |[]string|`A list of relation URIs or registered relation types to add to webfinger responses. See the Environment Variable Types description for more details.`|`[http://openid.net/specs/connect/1.0/issuer http://webfinger.opencloud/rel/server-instance]`|
|`OC_URL`<br/>`OC_OIDC_ISSUER`<br/>`WEBFINGER_OIDC_ISSUER`| 1.0.0 |string|`The identity provider href for the openid-discovery relation.`|`https://localhost:9200`|
|`OC_URL`<br/>`WEBFINGER_OPENCLOUD_SERVER_INSTANCE_URL`| 1.0.0 |string|`The URL for the legacy OpenCloud server instance relation (not to be confused with the product OpenCloud Server). It defaults to the OC_URL but can be overridden to support some reverse proxy corner cases. To shard the deployment, multiple instances can be configured in the configuration file.`|`https://localhost:9200`|
|`OC_INSECURE`<br/>`WEBFINGER_INSECURE`| 1.0.0 |bool|`Allow insecure connections to the WEBFINGER service.`|`false`|
