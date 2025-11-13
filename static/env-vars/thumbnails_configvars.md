Environment variables for the **thumbnails** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_TRACING_ENABLED`<br/>`THUMBNAILS_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|`false`|
|`OC_TRACING_TYPE`<br/>`THUMBNAILS_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`|``|
|`OC_TRACING_ENDPOINT`<br/>`THUMBNAILS_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`|``|
|`OC_TRACING_COLLECTOR`<br/>`THUMBNAILS_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`|``|
|`OC_LOG_LEVEL`<br/>`THUMBNAILS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`THUMBNAILS_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`THUMBNAILS_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`THUMBNAILS_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`THUMBNAILS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9189`|
|`THUMBNAILS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`THUMBNAILS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`THUMBNAILS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`THUMBNAILS_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|`127.0.0.1:9185`|
|`THUMBNAILS_MAX_CONCURRENT_REQUESTS`| 1.0.0 |int|`Number of maximum concurrent thumbnail requests. Default is 0 which is unlimited.`|`0`|
|`THUMBNAILS_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`127.0.0.1:9186`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`false`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|``|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|``|
|`THUMBNAILS_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`/thumbnails`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`THUMBNAILS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`[*]`|
|`OC_CORS_ALLOW_METHODS`<br/>`THUMBNAILS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`[GET POST PUT PATCH DELETE OPTIONS]`|
|`OC_CORS_ALLOW_HEADERS`<br/>`THUMBNAILS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Cache-Control]`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`THUMBNAILS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`true`|
|`THUMBNAILS_RESOLUTIONS`| 1.0.0 |[]string|`The supported list of target resolutions in the format WidthxHeight like 32x32. You can define any resolution as required. See the Environment Variable Types description for more details.`|`[16x16 32x32 64x64 128x128 1080x1920 1920x1080 2160x3840 3840x2160 4320x7680 7680x4320]`|
|`THUMBNAILS_FILESYSTEMSTORAGE_ROOT`| 1.0.0 |string|`The directory where the filesystem storage will store the thumbnails. If not defined, the root directory derives from $OC_BASE_DATA_PATH/thumbnails.`|`/Users/t.schweiger/.opencloud/thumbnails`|
|`OC_INSECURE`<br/>`THUMBNAILS_WEBDAVSOURCE_INSECURE`| 1.0.0 |bool|`Ignore untrusted SSL certificates when connecting to the webdav source.`|`false`|
|`OC_INSECURE`<br/>`THUMBNAILS_CS3SOURCE_INSECURE`| 1.0.0 |bool|`Ignore untrusted SSL certificates when connecting to the CS3 source.`|`false`|
|`OC_REVA_GATEWAY`| 1.0.0 |string|`CS3 gateway used to look up user metadata`|`eu.opencloud.api.gateway`|
|`THUMBNAILS_TXT_FONTMAP_FILE`| 1.0.0 |string|`The path to a font file for txt thumbnails.`|``|
|`THUMBNAILS_TRANSFER_TOKEN`| 1.0.0 |string|`The secret to sign JWT to download the actual thumbnail file.`|``|
|`THUMBNAILS_DATA_ENDPOINT`| 1.0.0 |string|`The HTTP endpoint where the actual thumbnail file can be downloaded.`|`http://127.0.0.1:9186/thumbnails/data`|
|`THUMBNAILS_MAX_INPUT_WIDTH`| 1.0.0 |int|`The maximum width of an input image which is being processed.`|`7680`|
|`THUMBNAILS_MAX_INPUT_HEIGHT`| 1.0.0 |int|`The maximum height of an input image which is being processed.`|`7680`|
|`THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`| 1.0.0 |string|`The maximum file size of an input image which is being processed. Usable common abbreviations: [KB, KiB, MB, MiB, GB, GiB, TB, TiB, PB, PiB, EB, EiB], example: 2GB.`|`50MB`|
