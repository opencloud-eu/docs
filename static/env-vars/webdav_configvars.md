Environment variables for the **webdav** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`WEBDAV_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`WEBDAV_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`WEBDAV_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`WEBDAV_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`WEBDAV_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`WEBDAV_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`WEBDAV_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`WEBDAV_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`WEBDAV_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9119|
|`WEBDAV_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`WEBDAV_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`WEBDAV_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`WEBDAV_HTTP_ADDR`| 1.0.0 |string|The bind address of the HTTP service.|127.0.0.1:9115|
|`WEBDAV_HTTP_ROOT`| 1.0.0 |string|Subdirectory that serves as the root for this HTTP service.|/|
|`OC_CORS_ALLOW_ORIGINS`<br/>`WEBDAV_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.|[*]|
|`OC_CORS_ALLOW_METHODS`<br/>`WEBDAV_CORS_ALLOW_METHODS`| 1.0.0 |[]string|A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.|[GET POST PUT PATCH DELETE OPTIONS]|
|`OC_CORS_ALLOW_HEADERS`<br/>`WEBDAV_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.|[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Cache-Control]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`WEBDAV_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.|true|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.|false|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|Path/File name of the TLS server certificate (in PEM format) for the http services.||
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.||
|`OC_DISABLE_PREVIEWS`<br/>`WEBDAV_DISABLE_PREVIEWS`| 1.0.0 |bool|Set this option to 'true' to disable rendering of thumbnails triggered via webdav access. Note that when disabled, all access to preview related webdav paths will return a 404.|false|
|`OC_URL`<br/>`OC_PUBLIC_URL`| 1.0.0 |string|URL, where OpenCloud is reachable for users.|https://127.0.0.1:9200|
|`WEBDAV_WEBDAV_NAMESPACE`| 1.0.0 |string|CS3 path layout to use when forwarding /webdav requests|/users/&#123;&#123;.Id.OpaqueId&#125;&#125;|
|`OC_REVA_GATEWAY`| 1.0.0 |string|CS3 gateway used to look up user metadata|eu.opencloud.api.gateway|
|`OC_REVA_GATEWAY_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the CS3 gateway endpoint. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_REVA_GATEWAY_TLS_CACERT`| 1.0.0 |string|The root CA certificate used to validate the gateway's TLS certificate.||