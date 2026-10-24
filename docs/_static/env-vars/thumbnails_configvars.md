## Environment variables for the **thumbnails** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`THUMBNAILS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|`"error"`|
|`THUMBNAILS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`"127.0.0.1:9189"`|
|`THUMBNAILS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|`""`|
|`THUMBNAILS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`"false"`|
|`THUMBNAILS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`"false"`|
|`THUMBNAILS_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`"127.0.0.1:9186"`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`"false"`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|`""`|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|`""`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`THUMBNAILS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`"[*]"`|
|`OC_CORS_ALLOW_METHODS`<br/>`THUMBNAILS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`"[GET POST PUT PATCH DELETE OPTIONS]"`|
|`OC_CORS_ALLOW_HEADERS`<br/>`THUMBNAILS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`"[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Cache-Control]"`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`THUMBNAILS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`"true"`|
|`THUMBNAILS_MAX_INPUT_WIDTH`| 1.0.0 |int|`The maximum width of an input image which is being processed.`|`"7680"`|
|`THUMBNAILS_MAX_OUTPUT_WIDTH`| next |int|`The maximum width of a thumbnail that may be asked for. A larger box is refused with HTTP 422. webdav never asks for more than its largest configured resolution, so this bounds everything else that reaches the endpoint.`|`"2048"`|
|`THUMBNAILS_MAX_OUTPUT_HEIGHT`| next |int|`The maximum height of a thumbnail that may be asked for.`|`"2048"`|
|`THUMBNAILS_MAX_INPUT_HEIGHT`| 1.0.0 |int|`The maximum height of an input image which is being processed.`|`"7680"`|
|`THUMBNAILS_MAX_CONCURRENT_REQUESTS`| next |int|`Maximum number of concurrent thumbnail generation requests. Default is 0 which is unlimited.`|`"0"`|
|`OC_THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`<br/>`THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`| 1.0.0 |string|`The maximum size of an image posted to the generator. Usable common abbreviations: [KB, KiB, MB, MiB, GB, GiB], example: 50MB. An empty value means unlimited.`|`"50MB"`|
|`THUMBNAILS_MAX_ANIMATION_FRAMES`| next |int|`The maximum number of frames an animated image may have. A file with more frames is refused before any of them is decoded. Default is 100, 0 is unlimited.`|`"100"`|
