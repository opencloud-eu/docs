
2025-05-07-11-16-16
| Deprecation Info | Deprecation Version | Removal Version | Deprecation Replacement |
|---|---|---|

|  | next |  |  |
Environment variables for the **storage-users** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`STORAGE_USERS_SERVICE_NAME`| 1.0.0 |string|Service name to use. Change this when starting an additional storage provider with a custom configuration to prevent it from colliding with the default 'storage-users' service.|storage-users|
|`OC_TRACING_ENABLED`<br/>`STORAGE_USERS_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`STORAGE_USERS_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`STORAGE_USERS_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`STORAGE_USERS_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`STORAGE_USERS_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`STORAGE_USERS_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`STORAGE_USERS_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`STORAGE_USERS_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`STORAGE_USERS_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9159|
|`STORAGE_USERS_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`STORAGE_USERS_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`STORAGE_USERS_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`STORAGE_USERS_GRPC_ADDR`| 1.0.0 |string|The bind address of the GRPC service.|127.0.0.1:9157|
|`OC_GRPC_PROTOCOL`<br/>`STORAGE_USERS_GRPC_PROTOCOL`| 1.0.0 |string|The transport protocol of the GPRC service.|tcp|
|`STORAGE_USERS_HTTP_ADDR`| 1.0.0 |string|The bind address of the HTTP service.|127.0.0.1:9158|
|`STORAGE_USERS_HTTP_PROTOCOL`| 1.0.0 |string|The transport protocol of the HTTP service.|tcp|
|`OC_CORS_ALLOW_ORIGINS`<br/>`STORAGE_USERS_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.|[https://localhost:9200]|
|`OC_CORS_ALLOW_METHODS`<br/>`STORAGE_USERS_CORS_ALLOW_METHODS`| 1.0.0 |[]string|A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.|[POST HEAD PATCH OPTIONS GET DELETE]|
|`OC_CORS_ALLOW_HEADERS`<br/>`STORAGE_USERS_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.|[Authorization Origin X-Requested-With X-Request-Id X-HTTP-Method-Override Content-Type Upload-Length Upload-Offset Tus-Resumable Upload-Metadata Upload-Defer-Length Upload-Concat Upload-Incomplete Upload-Draft-Interop-Version]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`STORAGE_USERS_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.|false|
|`OC_CORS_EXPOSE_HEADERS`<br/>`STORAGE_USERS_CORS_EXPOSE_HEADERS`| 1.0.0 |[]string|A list of exposed CORS headers. See following chapter for more details: *Access-Control-Expose-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers. See the Environment Variable Types description for more details.|[Upload-Offset Location Upload-Length Tus-Version Tus-Resumable Tus-Max-Size Tus-Extension Upload-Metadata Upload-Defer-Length Upload-Concat Upload-Incomplete Upload-Draft-Interop-Version]|
|`OC_CORS_MAX_AGE`<br/>`STORAGE_USERS_CORS_MAX_AGE`| 1.0.0 |uint|The max cache duration of preflight headers. See following chapter for more details: *Access-Control-Max-Age* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age. See the Environment Variable Types description for more details.|86400|
|`OC_JWT_SECRET`<br/>`STORAGE_USERS_JWT_SECRET`| 1.0.0 |string|The secret to mint and validate jwt tokens.||
|`OC_REVA_GATEWAY`| 1.0.0 |string|The CS3 gateway endpoint.|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.||
|`STORAGE_USERS_SKIP_USER_GROUPS_IN_TOKEN`| 1.0.0 |bool|Disables the loading of user's group memberships from the reva access token.|false|
|`STORAGE_USERS_GRACEFUL_SHUTDOWN_TIMEOUT`| 1.0.0 |int|The number of seconds to wait for the 'storage-users' service to shutdown cleanly before exiting with an error that gets logged. Note: This setting is only applicable when running the 'storage-users' service as a standalone service. See the text description for more details.|30|
|`STORAGE_USERS_DRIVER`| 1.0.0 |string|The storage driver which should be used by the service. Defaults to 'decomposed', Supported values are: 'decomposed', 'decomposeds3' and 'owncloudsql'. For backwards compatibility reasons it's also possible to use the 'ocis' and 's3ng' driver and configure them using the 'decomposed'/'decomposeds3' options. The 'decomposed' driver stores all data (blob and meta data) in an POSIX compliant volume. The 'decomposeds3' driver stores metadata in a POSIX compliant volume and uploads blobs to the s3 bucket.|posix|
|`OC_DECOMPOSEDFS_PROPAGATOR`<br/>`STORAGE_USERS_DECOMPOSED_PROPAGATOR`| 1.0.0 |string|The propagator used for decomposedfs. At the moment, only 'sync' is fully supported, 'async' is available as an experimental option.|sync|
|`STORAGE_USERS_ASYNC_PROPAGATOR_PROPAGATION_DELAY`| 1.0.0 |Duration|The delay between a change made to a tree and the propagation start on treesize and treetime. Multiple propagations are computed to a single one. See the Environment Variable Types description for more details.|0s|
|`STORAGE_USERS_DECOMPOSED_ROOT`| 1.0.0 |string|The directory where the filesystem storage will store blobs and metadata. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/users.|/home/opencloud/.opencloud/storage/users|
|`STORAGE_USERS_DECOMPOSED_USER_LAYOUT`| 1.0.0 |string|Template string for the user storage layout in the user directory.|`{{.Id.OpaqueId}}`|
|`STORAGE_USERS_PERMISSION_ENDPOINT`<br/>`STORAGE_USERS_DECOMPOSED_PERMISSIONS_ENDPOINT`| 1.0.0 |string|Endpoint of the permissions service. The endpoints can differ for 'decomposed' and 'decomposeds3'.|eu.opencloud.api.settings|
|`STORAGE_USERS_DECOMPOSED_PERSONAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct personal space aliases.|`{{.SpaceType}}`/`{{.User.Username \| lower}}`|
|`STORAGE_USERS_DECOMPOSED_PERSONAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the personal space roots.||
|`STORAGE_USERS_DECOMPOSED_GENERAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct general space aliases.|`{{.SpaceType}}`/`{{.SpaceName \| replace " " "-" \| lower}}`|
|`STORAGE_USERS_DECOMPOSED_GENERAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the projects space roots.||
|`STORAGE_USERS_DECOMPOSED_SHARE_FOLDER`| 1.0.0 |string|Name of the folder jailing all shares.|/Shares|
|`STORAGE_USERS_DECOMPOSED_MAX_ACQUIRE_LOCK_CYCLES`| 1.0.0 |int|When trying to lock files, OpenCloud will try this amount of times to acquire the lock before failing. After each try it will wait for an increasing amount of time. Values of 0 or below will be ignored and the default value will be used.|20|
|`STORAGE_USERS_DECOMPOSED_LOCK_CYCLE_DURATION_FACTOR`| 1.0.0 |int|When trying to lock files, OpenCloud will multiply the cycle with this factor and use it as a millisecond timeout. Values of 0 or below will be ignored and the default value will be used.|30|
|`OC_MAX_CONCURRENCY`<br/>`STORAGE_USERS_DECOMPOSED_MAX_CONCURRENCY`| 1.0.0 |int|Maximum number of concurrent go-routines. Higher values can potentially get work done faster but will also cause more load on the system. Values of 0 or below will be ignored and the default value will be used.|5|
|`OC_ASYNC_UPLOADS`| 1.0.0 |bool|Enable asynchronous file uploads.|true|
|`OC_SPACES_MAX_QUOTA`<br/>`STORAGE_USERS_DECOMPOSED_MAX_QUOTA`| 1.0.0 |uint64|Set a global max quota for spaces in bytes. A value of 0 equals unlimited. If not using the global OC_SPACES_MAX_QUOTA, you must define the FRONTEND_MAX_QUOTA in the frontend service.|0|
|`OC_DISABLE_VERSIONING`| 1.0.0 |bool|Disables versioning of files. When set to true, new uploads with the same filename will overwrite existing files instead of creating a new version.|false|
|`OC_DECOMPOSEDFS_PROPAGATOR`<br/>`STORAGE_USERS_DECOMPOSEDS3_PROPAGATOR`| 1.0.0 |string|The propagator used for decomposedfs. At the moment, only 'sync' is fully supported, 'async' is available as an experimental option.|sync|
|`STORAGE_USERS_ASYNC_PROPAGATOR_PROPAGATION_DELAY`| 1.0.0 |Duration|The delay between a change made to a tree and the propagation start on treesize and treetime. Multiple propagations are computed to a single one. See the Environment Variable Types description for more details.|0s|
|`STORAGE_USERS_DECOMPOSEDS3_ROOT`| 1.0.0 |string|The directory where the filesystem storage will store metadata for blobs. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/users.|/home/opencloud/.opencloud/storage/users|
|`STORAGE_USERS_DECOMPOSEDS3_USER_LAYOUT`| 1.0.0 |string|Template string for the user storage layout in the user directory.|`{{.Id.OpaqueId}}`|
|`STORAGE_USERS_PERMISSION_ENDPOINT`<br/>`STORAGE_USERS_DECOMPOSEDS3_PERMISSIONS_ENDPOINT`| 1.0.0 |string|Endpoint of the permissions service. The endpoints can differ for 'decomposed' and 'decomposeds3'.|eu.opencloud.api.settings|
|`STORAGE_USERS_DECOMPOSEDS3_REGION`| 1.0.0 |string|Region of the S3 bucket.|default|
|`STORAGE_USERS_DECOMPOSEDS3_ACCESS_KEY`| 1.0.0 |string|Access key for the S3 bucket.||
|`STORAGE_USERS_DECOMPOSEDS3_SECRET_KEY`| 1.0.0 |string|Secret key for the S3 bucket.||
|`STORAGE_USERS_DECOMPOSEDS3_ENDPOINT`| 1.0.0 |string|Endpoint for the S3 bucket.||
|`STORAGE_USERS_DECOMPOSEDS3_BUCKET`| 1.0.0 |string|Name of the S3 bucket.||
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_DISABLE_CONTENT_SHA256`| 1.0.0 |bool|Disable sending content sha256 when copying objects to S3.|false|
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_DISABLE_MULTIPART`| 1.0.0 |bool|Disable multipart uploads when copying objects to S3|true|
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_SEND_CONTENT_MD5`| 1.0.0 |bool|Send a Content-MD5 header when copying objects to S3.|true|
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_CONCURRENT_STREAM_PARTS`| 1.0.0 |bool|Always precreate parts when copying objects to S3.|true|
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_NUM_THREADS`| 1.0.0 |uint|Number of concurrent uploads to use when copying objects to S3.|4|
|`STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_PART_SIZE`| 1.0.0 |uint64|Part size for concurrent uploads to S3. If no value or 0 is set, the library's default value of 16MB is used. The value range is min 5MB and max 5GB.|0|
|`STORAGE_USERS_DECOMPOSEDS3_PERSONAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct personal space aliases.|`{{.SpaceType}}`/`{{.User.Username \| lower}}`|
|`STORAGE_USERS_DECOMPOSEDS3_PERSONAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the personal space roots.||
|`STORAGE_USERS_DECOMPOSEDS3_GENERAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct general space aliases.|`{{.SpaceType}}`/`{{.SpaceName \| replace " " "-" \| lower}}`|
|`STORAGE_USERS_DECOMPOSEDS3_GENERAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the projects space roots.||
|`STORAGE_USERS_DECOMPOSEDS3_SHARE_FOLDER`| 1.0.0 |string|Name of the folder jailing all shares.|/Shares|
|`STORAGE_USERS_DECOMPOSEDS3_MAX_ACQUIRE_LOCK_CYCLES`| 1.0.0 |int|When trying to lock files, OpenCloud will try this amount of times to acquire the lock before failing. After each try it will wait for an increasing amount of time. Values of 0 or below will be ignored and the default value of 20 will be used.|20|
|`STORAGE_USERS_DECOMPOSEDS3_LOCK_CYCLE_DURATION_FACTOR`| 1.0.0 |int|When trying to lock files, OpenCloud will multiply the cycle with this factor and use it as a millisecond timeout. Values of 0 or below will be ignored and the default value of 30 will be used.|30|
|`OC_MAX_CONCURRENCY`<br/>`STORAGE_USERS_DECOMPOSEDS3_MAX_CONCURRENCY`| 1.0.0 |int|Maximum number of concurrent go-routines. Higher values can potentially get work done faster but will also cause more load on the system. Values of 0 or below will be ignored and the default value of 100 will be used.|5|
|`OC_ASYNC_UPLOADS`| 1.0.0 |bool|Enable asynchronous file uploads.|true|
|`OC_DISABLE_VERSIONING`| 1.0.0 |bool|Disables versioning of files. When set to true, new uploads with the same filename will overwrite existing files instead of creating a new version.|false|
|`STORAGE_USERS_OWNCLOUDSQL_DATADIR`| 1.0.0 |string|The directory where the filesystem storage will store SQL migration data. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/owncloud.|/home/opencloud/.opencloud/storage/owncloud|
|`STORAGE_USERS_OWNCLOUDSQL_SHARE_FOLDER`| 1.0.0 |string|Name of the folder jailing all shares.|/Shares|
|`STORAGE_USERS_OWNCLOUDSQL_LAYOUT`| 1.0.0 |string|Path layout to use to navigate into a users folder in an owncloud data directory|`{{.Username}}`|
|`STORAGE_USERS_OWNCLOUDSQL_UPLOADINFO_DIR`| 1.0.0 |string|The directory where the filesystem will store uploads temporarily. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/uploadinfo.|/home/opencloud/.opencloud/storage/uploadinfo|
|`STORAGE_USERS_OWNCLOUDSQL_DB_USERNAME`| 1.0.0 |string|Username for the database.|owncloud|
|`STORAGE_USERS_OWNCLOUDSQL_DB_PASSWORD`| 1.0.0 |string|Password for the database.|owncloud|
|`STORAGE_USERS_OWNCLOUDSQL_DB_HOST`| 1.0.0 |string|Hostname or IP of the database server.||
|`STORAGE_USERS_OWNCLOUDSQL_DB_PORT`| 1.0.0 |int|Port that the database server is listening on.|3306|
|`STORAGE_USERS_OWNCLOUDSQL_DB_NAME`| 1.0.0 |string|Name of the database to be used.|owncloud|
|`STORAGE_USERS_OWNCLOUDSQL_USERS_PROVIDER_ENDPOINT`| 1.0.0 |string|Endpoint of the users provider.|eu.opencloud.api.users|
|`STORAGE_USERS_POSIX_ROOT`| 1.0.0 |string|The directory where the filesystem storage will store its data. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/users.|/home/opencloud/.opencloud/storage/users|
|`OC_DECOMPOSEDFS_PROPAGATOR`<br/>`STORAGE_USERS_POSIX_PROPAGATOR`| 2.0.0 |string|The propagator used for the posix driver. At the moment, only 'sync' is fully supported, 'async' is available as an experimental option.||
|`STORAGE_USERS_ASYNC_PROPAGATOR_PROPAGATION_DELAY`| 1.0.0 |Duration|The delay between a change made to a tree and the propagation start on treesize and treetime. Multiple propagations are computed to a single one. See the Environment Variable Types description for more details.|0s|
|`STORAGE_USERS_POSIX_PERSONAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct personal space aliases.|`{{.SpaceType}}`/`{{.User.Username \| lower}}`|
|`STORAGE_USERS_POSIX_PERSONAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the personal space roots.|users/`{{.User.Id.OpaqueId}}`|
|`STORAGE_USERS_POSIX_GENERAL_SPACE_ALIAS_TEMPLATE`| 1.0.0 |string|Template string to construct general space aliases.|`{{.SpaceType}}`/`{{.SpaceName \| replace " " "-" \| lower}}`|
|`STORAGE_USERS_POSIX_GENERAL_SPACE_PATH_TEMPLATE`| 1.0.0 |string|Template string to construct the paths of the projects space roots.|projects/`{{.SpaceId}}`|
|`STORAGE_USERS_PERMISSION_ENDPOINT`<br/>`STORAGE_USERS_POSIX_PERMISSIONS_ENDPOINT`| 1.0.0 |string|Endpoint of the permissions service. The endpoints can differ for 'decomposed', 'posix' and 'decomposeds3'.|eu.opencloud.api.settings|
|`OC_ASYNC_UPLOADS`| 1.0.0 |bool|Enable asynchronous file uploads.|true|
|`STORAGE_USERS_POSIX_SCAN_DEBOUNCE_DELAY`| 1.0.0 |Duration|The time in milliseconds to wait before scanning the filesystem for changes after a change has been detected.|1s|
|`OC_SPACES_MAX_QUOTA`<br/>`STORAGE_USERS_POSIX_MAX_QUOTA`| 2.0.0 |uint64|Set a global max quota for spaces in bytes. A value of 0 equals unlimited. If not using the global OC_SPACES_MAX_QUOTA, you must define the FRONTEND_MAX_QUOTA in the frontend service.|0|
|`STORAGE_USERS_POSIX_MAX_ACQUIRE_LOCK_CYCLES`| 2.0.0 |int|When trying to lock files, OpenCloud will try this amount of times to acquire the lock before failing. After each try it will wait for an increasing amount of time. Values of 0 or below will be ignored and the default value will be used.|0|
|`STORAGE_USERS_POSIX_LOCK_CYCLE_DURATION_FACTOR`| 2.0.0 |int|When trying to lock files, OpenCloud will multiply the cycle with this factor and use it as a millisecond timeout. Values of 0 or below will be ignored and the default value will be used.|0|
|`OC_MAX_CONCURRENCY`<br/>`STORAGE_USERS_POSIX_MAX_CONCURRENCY`| 2.0.0 |int|Maximum number of concurrent go-routines. Higher values can potentially get work done faster but will also cause more load on the system. Values of 0 or below will be ignored and the default value will be used.|0|
|`OC_DISABLE_VERSIONING`| 2.0.0 |bool|Disables versioning of files. When set to true, new uploads with the same filename will overwrite existing files instead of creating a new version.|false|
|`STORAGE_USERS_POSIX_USE_SPACE_GROUPS`| 1.0.0 |bool|Use space groups to manage permissions on spaces.|false|
|`STORAGE_USERS_POSIX_ENABLE_FS_REVISIONS`| 1.0.0 |bool|Allow for generating revisions from changes done to the local storage. Note: This doubles the number of bytes stored on disk because a copy of the current revision is stored to be turned into a revision later.|false|
|`STORAGE_USERS_POSIX_WATCH_FS`| 2.0.0 |bool|Enable the filesystem watcher to detect changes to the filesystem. This is used to detect changes to the filesystem and update the metadata accordingly.|false|
|`STORAGE_USERS_POSIX_WATCH_TYPE`| 1.0.0 |string|Type of the watcher to use for getting notified about changes to the filesystem. Currently available options are 'inotifywait' (default), 'cephfs', 'gpfswatchfolder' and 'gpfsfileauditlogging'.||
|`STORAGE_USERS_POSIX_WATCH_PATH`| 1.0.0 |string|Path to the watch directory/file. Only applies to the 'gpfsfileauditlogging' and 'inotifywait' watcher, in which case it is the path of the file audit log file/base directory to watch.||
|`STORAGE_USERS_POSIX_WATCH_NOTIFICATION_BROKERS,STORAGE_USERS_POSIX_WATCH_FOLDER_KAFKA_BROKERS`| 1.0.0 |string|Comma-separated list of kafka brokers to read the watchfolder events from.||
|`STORAGE_USERS_POSIX_WATCH_ROOT`| next |string|Path to the watch root directory. Event paths will be considered relative to this path. Only applies to the 'gpswatchfolder' and 'cephfs' watchers.||
|`STORAGE_USERS_POSIX_INOTIFY_STATS_FREQUENCY`| next |Duration|Frequency to log inotify stats.|5m0s|
|`STORAGE_USERS_DATA_SERVER_URL`| 1.0.0 |string|URL of the data server, needs to be reachable by the data gateway provided by the frontend service or the user if directly exposed.|http://localhost:9158/data|
|`STORAGE_USERS_DATA_GATEWAY_URL`| 1.0.0 |string|URL of the data gateway server|https://localhost:9200/data|
|`STORAGE_USERS_TRANSFER_EXPIRES`| 1.0.0 |int64|The time after which the token for upload postprocessing expires|86400|
|`OC_EVENTS_ENDPOINT`<br/>`STORAGE_USERS_EVENTS_ENDPOINT`| 1.0.0 |string|The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`STORAGE_USERS_EVENTS_CLUSTER`| 1.0.0 |string|The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.|opencloud-cluster|
|`OC_INSECURE`<br/>`STORAGE_USERS_EVENTS_TLS_INSECURE`| 1.0.0 |bool|Whether to verify the server TLS certificates.|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`STORAGE_USERS_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|The root CA certificate used to validate the server's TLS certificate. If provided STORAGE_USERS_EVENTS_TLS_INSECURE will be seen as false.||
|`OC_EVENTS_ENABLE_TLS`<br/>`STORAGE_USERS_EVENTS_ENABLE_TLS`| 1.0.0 |bool|Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.|false|
|`STORAGE_USERS_EVENTS_NUM_CONSUMERS`| 1.0.0 |int|The amount of concurrent event consumers to start. Event consumers are used for post-processing files. Multiple consumers increase parallelisation, but will also increase CPU and memory demands. The setting has no effect when the OC_ASYNC_UPLOADS is set to false. The default and minimum value is 1.|0|
|`OC_EVENTS_AUTH_USERNAME`<br/>`STORAGE_USERS_EVENTS_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`STORAGE_USERS_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_CACHE_STORE`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_STORE`| 1.0.0 |string|The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.|memory|
|`OC_CACHE_STORE_NODES`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_STORE_NODES`| 1.0.0 |[]string|A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.|[127.0.0.1:9233]|
|`OC_CACHE_DATABASE`| 1.0.0 |string|The database name the configured store should use.|storage-users|
|`OC_CACHE_TTL`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_TTL`| 1.0.0 |Duration|Default time to live for user info in the user info cache. Only applied when access tokens has no expiration. See the Environment Variable Types description for more details.|24m0s|
|`OC_CACHE_DISABLE_PERSISTENCE`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_DISABLE_PERSISTENCE`| 1.0.0 |bool|Disables persistence of the cache. Only applies when store type 'nats-js-kv' is configured. Defaults to false.|false|
|`OC_CACHE_AUTH_USERNAME`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the cache store. Only applies when store type 'nats-js-kv' is configured.||
|`OC_CACHE_AUTH_PASSWORD`<br/>`STORAGE_USERS_FILEMETADATA_CACHE_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the cache store. Only applies when store type 'nats-js-kv' is configured.||
|`OC_CACHE_STORE`<br/>`STORAGE_USERS_ID_CACHE_STORE`| 1.0.0 |string|The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.|nats-js-kv|
|`OC_CACHE_STORE_NODES`<br/>`STORAGE_USERS_ID_CACHE_STORE_NODES`| 1.0.0 |[]string|A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.|[127.0.0.1:9233]|
|`OC_CACHE_DATABASE`| 1.0.0 |string|The database name the configured store should use.|ids-storage-users|
|`OC_CACHE_TTL`<br/>`STORAGE_USERS_ID_CACHE_TTL`| 1.0.0 |Duration|Default time to live for user info in the user info cache. Only applied when access tokens have no expiration. Defaults to 300s which is derived from the underlaying package though not explicitly set as default. See the Environment Variable Types description for more details.|24m0s|
|`OC_CACHE_DISABLE_PERSISTENCE`<br/>`STORAGE_USERS_ID_CACHE_DISABLE_PERSISTENCE`| 1.0.0 |bool|Disables persistence of the cache. Only applies when store type 'nats-js-kv' is configured. Defaults to false.|false|
|`OC_CACHE_AUTH_USERNAME`<br/>`STORAGE_USERS_ID_CACHE_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the cache store. Only applies when store type 'nats-js-kv' is configured.||
|`OC_CACHE_AUTH_PASSWORD`<br/>`STORAGE_USERS_ID_CACHE_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the cache store. Only applies when store type 'nats-js-kv' is configured.||
|`STORAGE_USERS_MOUNT_ID`| 1.0.0 |string|Mount ID of this storage.||
|`STORAGE_USERS_EXPOSE_DATA_SERVER`| 1.0.0 |bool|Exposes the data server directly to users and bypasses the data gateway. Ensure that the data server address is reachable by users.|false|
|`STORAGE_USERS_READ_ONLY`| 1.0.0 |bool|Set this storage to be read-only.|false|
|`STORAGE_USERS_UPLOAD_EXPIRATION`| 1.0.0 |int64|Duration in seconds after which uploads will expire. Note that when setting this to a low number, uploads could be cancelled before they are finished and return a 403 to the user.|86400|
|`OC_ADMIN_USER_ID`<br/>`STORAGE_USERS_PURGE_TRASH_BIN_USER_ID`| 1.0.0 |string|ID of the user who collects all necessary information for deletion. Consider that the UUID can be encoded in some LDAP deployment configurations like in .ldif files. These need to be decoded beforehand.||
|`STORAGE_USERS_PURGE_TRASH_BIN_PERSONAL_DELETE_BEFORE`| 1.0.0 |Duration|Specifies the period of time in which items that have been in the personal trash-bin for longer than this value should be deleted. A value of 0 means no automatic deletion. See the Environment Variable Types description for more details.|720h0m0s|
|`STORAGE_USERS_PURGE_TRASH_BIN_PROJECT_DELETE_BEFORE`| 1.0.0 |Duration|Specifies the period of time in which items that have been in the project trash-bin for longer than this value should be deleted. A value of 0 means no automatic deletion. See the Environment Variable Types description for more details.|720h0m0s|
|`OC_SERVICE_ACCOUNT_ID`<br/>`STORAGE_USERS_SERVICE_ACCOUNT_ID`| 1.0.0 |string|The ID of the service account the service should use. See the 'auth-service' service description for more details.||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`STORAGE_USERS_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|The service account secret.||
|`OC_GATEWAY_GRPC_ADDR`<br/>`STORAGE_USERS_GATEWAY_GRPC_ADDR`| 1.0.0 |string|The bind address of the gateway GRPC address.|127.0.0.1:9142|
|`OC_MACHINE_AUTH_API_KEY`<br/>`STORAGE_USERS_MACHINE_AUTH_API_KEY`| 1.0.0 |string|Machine auth API key used to validate internal requests necessary for the access to resources from other services.||
|`STORAGE_USERS_CLI_MAX_ATTEMPTS_RENAME_FILE`| 1.0.0 |int|The maximum number of attempts to rename a file when a user restores a file to an existing destination with the same name. The minimum value is 100.|0|