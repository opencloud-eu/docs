
2026-10-24-00-07-47

## Deprecation Notice

| Deprecation Info | Deprecation Version | Removal Version | Deprecation Replacement |
|---|---|---|:---|
| THUMBNAILS_FILESYSTEMSTORAGE_ROOT is deprecated. The webdav service owns the thumbnail cache now, so use WEBDAV_THUMBNAILS_CACHE_DIR instead. | next | next-prod | WEBDAV_THUMBNAILS_CACHE_DIR |

## Environment variables for the **webdav** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_LOG_LEVEL`<br/>`WEBDAV_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|`"error"`|
|`WEBDAV_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`"127.0.0.1:9119"`|
|`WEBDAV_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|`""`|
|`WEBDAV_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`"false"`|
|`WEBDAV_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`"false"`|
|`WEBDAV_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|`"127.0.0.1:9115"`|
|`WEBDAV_HTTP_ROOT`| 1.0.0 |string|`Subdirectory that serves as the root for this HTTP service.`|`"/"`|
|`OC_CORS_ALLOW_ORIGINS`<br/>`WEBDAV_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|`"[*]"`|
|`OC_CORS_ALLOW_METHODS`<br/>`WEBDAV_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|`"[GET POST PUT PATCH DELETE OPTIONS]"`|
|`OC_CORS_ALLOW_HEADERS`<br/>`WEBDAV_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|`"[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Cache-Control]"`|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`WEBDAV_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|`"true"`|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|`Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.`|`"false"`|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|`Path/File name of the TLS server certificate (in PEM format) for the http services.`|`""`|
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|`Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.`|`""`|
|`OC_URL`<br/>`OC_PUBLIC_URL`| 1.0.0 |string|`URL, where OpenCloud is reachable for users.`|`"https://localhost:9200"`|
|`WEBDAV_WEBDAV_NAMESPACE`| 1.0.0 |string|`CS3 path layout to use when forwarding /webdav requests`|`"/users/{{.Id.OpaqueId}}"`|
|`OC_REVA_GATEWAY`| 1.0.0 |string|`CS3 gateway used to look up user metadata`|`"eu.opencloud.api.gateway"`|
|`OC_DISABLE_PREVIEWS`<br/>`WEBDAV_DISABLE_PREVIEWS`| 1.0.0 |bool|`Set this option to 'true' to disable rendering of thumbnails triggered via webdav access. Note that when disabled, all access to preview related webdav paths will return a 404.`|`"false"`|
|`WEBDAV_THUMBNAILS_GENERATOR_URL`| next |string|`Base URL of the thumbnail generator service, e.g. \http://thumbnails:9186`|`"http://127.0.0.1:9186"`|
|`WEBDAV_THUMBNAILS_GENERATOR_TIMEOUT`| next |string|`HTTP timeout for requests to the thumbnail generator, e.g. 30s`|`"30s"`|
|`THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`<br/>`OC_THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`<br/>`WEBDAV_THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE`| next |string|`Maximum file size of an input image a thumbnail is made of. The generator refuses a larger body, so both read the same name by default. Usable common abbreviations: [KB, KiB, MB, MiB, GB, GiB], example: 50MB`|`"50MB"`|
|`WEBDAV_THUMBNAILS_CACHE_BACKEND`| next |string|`Cache backend for imagor thumbnails: 'none', 'memory', 'file', or 's3'. Default: file.`|`"file"`|
|`WEBDAV_THUMBNAILS_CACHE_DIR`| next |string|`Directory for file-based thumbnail cache (Default: $OC_BASE_DATA_PATH/thumbnails/files). Only used when WEBDAV_THUMBNAILS_CACHE_BACKEND is 'file'.`|`""`|
|`THUMBNAILS_FILESYSTEMSTORAGE_ROOT`| 1.0.0 |string|`Directory the thumbnails service stored its files in. Read as a fallback for WEBDAV_THUMBNAILS_CACHE_DIR.`|`""`|
|`THUMBNAILS_RESOLUTIONS`<br/>`WEBDAV_THUMBNAILS_RESOLUTIONS`| next |[]string|`Allowed thumbnail edge lengths, like 512. Each axis of a requested size is rounded up to the next one of these before the box is sent to the generator. Legacy WidthxHeight entries are still accepted and contribute both of their sides.`|`"[16 32 64 128 192 256 320 384 448 512 640 768 1024 1280 1920 2048]"`|
|`WEBDAV_THUMBNAILS_CACHE_S3_BUCKET`| next |string|`S3 bucket name for thumbnail cache when WEBDAV_THUMBNAILS_CACHE_BACKEND is 's3'.`|`""`|
|`WEBDAV_THUMBNAILS_CACHE_S3_REGION`| next |string|`S3 region for thumbnail cache when WEBDAV_THUMBNAILS_CACHE_BACKEND is 's3'.`|`""`|
|`WEBDAV_THUMBNAILS_CACHE_S3_ENDPOINT`| next |string|`S3 endpoint URL (for MinIO or compatible services) when WEBDAV_THUMBNAILS_CACHE_BACKEND is 's3'.`|`""`|
|`WEBDAV_THUMBNAILS_CACHE_S3_ACCESS_KEY`| next |string|`S3 access key for thumbnail cache authentication.`|`""`|
|`WEBDAV_THUMBNAILS_CACHE_S3_SECRET_KEY`| next |string|`S3 secret key for thumbnail cache authentication.`|`""`|
|`OC_THUMBNAILS_ADDITIONAL_SOURCE_TYPES`<br/>`WEBDAV_THUMBNAILS_ADDITIONAL_SOURCE_TYPES`| next |[]string|`Additional mime types a preview is announced and attempted for, e.g. image/vnd.microsoft.icon for a generator that reads icons. The built-in list is included; this only adds to them. A type the running generator cannot read answers 404.`|`"[]"`|
|`OC_THUMBNAILS_ADDITIONAL_GENERATOR_FORMATS`<br/>`WEBDAV_THUMBNAILS_ADDITIONAL_GENERATOR_FORMATS`| next |[]string|`Additional formats the thumbnail generator writes, one per type it writes, as type:format entries, e.g. image/webp:webp. The format is the name the generator's own format filter uses. The built-in list is included; an entry for a type that is already listed replaces it. A type that is not listed is asked for as a JPEG instead, because what the generator behind the URL really writes is its own business.`|`"[]"`|
|`OC_THUMBNAILS_ADDITIONAL_OUTPUT_TYPES`<br/>`WEBDAV_THUMBNAILS_ADDITIONAL_OUTPUT_TYPES`| next |[]string|`Additional types a thumbnail is returned in, one per type of the image it is made from, as source:target entries, e.g. image/vnd.microsoft.icon:image/png. The built-in list is included; an entry for a source type that is already listed replaces it. The target is asked for by the name WEBDAV_THUMBNAILS_ADDITIONAL_GENERATOR_FORMATS gives it. A type that is not listed becomes a JPEG; a target this service has no format name for is asked for as a JPEG as well.`|`"[]"`|
|`THUMBNAILS_TXT_FONTMAP_FILE`<br/>`WEBDAV_THUMBNAILS_TXT_FONTMAP_FILE`| next |string|`The path to a font map file for txt thumbnails.`|`""`|
