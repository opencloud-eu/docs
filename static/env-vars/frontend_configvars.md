
2025-11-11-09-16-18

# Deprecation Notice

| Deprecation Info | Deprecation Version | Removal Version | Deprecation Replacement |
|---|---|---|---|
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_STORE, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_STORE_NODES, the OCS API is deprecated | 1.0.0 | next-prod |  |
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_TTL, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_DISABLE_PERSISTENCE, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_AUTH_USERNAME, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_STAT_CACHE_AUTH_PASSWORD, the OCS API is deprecated | 1.0.0 | next-prod |  |
| The OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_LIST_OCM_SHARES, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_INCLUDE_OCM_SHAREES, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_PUBLIC_SHARE_MUST_HAVE_PASSWORD, the OCS API is deprecated | 1.0.0 | next-prod |  |
| FRONTEND_OCS_PUBLIC_WRITABLE_SHARE_MUST_HAVE_PASSWORD, the OCS API is deprecated | 1.0.0 | next-prod |  |
Environment variables for the **frontend** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`FRONTEND_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|false|
|`OC_TRACING_TYPE`<br/>`FRONTEND_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`||
|`OC_TRACING_ENDPOINT`<br/>`FRONTEND_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`||
|`OC_TRACING_COLLECTOR`<br/>`FRONTEND_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`||
|`OC_LOG_LEVEL`<br/>`FRONTEND_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`||
|`OC_LOG_PRETTY`<br/>`FRONTEND_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|false|
|`OC_LOG_COLOR`<br/>`FRONTEND_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|false|
|`OC_LOG_FILE`<br/>`FRONTEND_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`||
|`FRONTEND_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9141|
|`FRONTEND_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`FRONTEND_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`FRONTEND_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`FRONTEND_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|127.0.0.1:9140|
|`FRONTEND_HTTP_PROTOCOL`| 1.0.0 |string|`The transport protocol of the HTTP service.`|tcp|
|`FRONTEND_HTTP_PREFIX`| 1.0.0 |string|`The Path prefix where the frontend can be accessed (defaults to /).`||
|`OC_CORS_ALLOW_ORIGINS`<br/>`FRONTEND_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|[https://localhost:9200]|
|`OC_CORS_ALLOW_METHODS`<br/>`FRONTEND_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|[OPTIONS HEAD GET PUT POST PATCH DELETE MKCOL PROPFIND PROPPATCH MOVE COPY REPORT SEARCH]|
|`OC_CORS_ALLOW_HEADERS`<br/>`FRONTEND_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|[Origin Accept Content-Type Depth Authorization Ocs-Apirequest If-None-Match If-Match Destination Overwrite X-Request-Id X-Requested-With Tus-Resumable Tus-Checksum-Algorithm Upload-Concat Upload-Length Upload-Metadata Upload-Defer-Length Upload-Expires Upload-Checksum Upload-Offset X-HTTP-Method-Override Cache-Control]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`FRONTEND_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|false|
|`OC_TRANSFER_SECRET`| 1.0.0 |string|`Transfer secret for signing file up- and download requests.`||
|`OC_JWT_SECRET`<br/>`FRONTEND_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`||
|`OC_REVA_GATEWAY`| 1.0.0 |string|`The CS3 gateway endpoint.`|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|`TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.`||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|`Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.`||
|`OC_MACHINE_AUTH_API_KEY`<br/>`FRONTEND_MACHINE_AUTH_API_KEY`| 1.0.0 |string|`The machine auth API key used to validate internal requests necessary to access resources from other services.`||
|`FRONTEND_SKIP_USER_GROUPS_IN_TOKEN`| 1.0.0 |bool|`Disables the loading of user's group memberships from the reva access token.`|false|
|`FRONTEND_ENABLE_FAVORITES`| 1.0.0 |bool|`Enables the support for favorites in the clients.`|false|
|`OC_SPACES_MAX_QUOTA`<br/>`FRONTEND_MAX_QUOTA`| 1.0.0 |uint64|`Set the global max quota value in bytes. A value of 0 equals unlimited. The value is provided via capabilities.`|0|
|`FRONTEND_UPLOAD_MAX_CHUNK_SIZE`| 1.0.0 |int|`Sets the max chunk sizes in bytes for uploads via the clients.`|10000000|
|`FRONTEND_UPLOAD_HTTP_METHOD_OVERRIDE`| 1.0.0 |string|`Advise TUS to replace PATCH requests by POST requests.`||
|`FRONTEND_DEFAULT_UPLOAD_PROTOCOL`| 1.0.0 |string|`The default upload protocol to use in clients. Currently only 'tus' is available. See the developer API documentation for more details about TUS.`|tus|
|`OC_ENABLE_OCM`<br/>`FRONTEND_ENABLE_FEDERATED_SHARING_INCOMING`| 1.0.0 |bool|`Changing this value is NOT supported. Enables support for incoming federated sharing for clients. The backend behaviour is not changed.`|false|
|`OC_ENABLE_OCM`<br/>`FRONTEND_ENABLE_FEDERATED_SHARING_OUTGOING`| 1.0.0 |bool|`Changing this value is NOT supported. Enables support for outgoing federated sharing for clients. The backend behaviour is not changed.`|false|
|`FRONTEND_SEARCH_MIN_LENGTH`| 1.0.0 |int|`Minimum number of characters to enter before a client should start a search for Share receivers. This setting can be used to customize the user experience if e.g too many results are displayed.`|3|
|`OC_EDITION`<br/>`FRONTEND_EDITION`| 1.0.0 |string|`Edition of OpenCloud. Used for branding purposes.`||
|`OC_DISABLE_SSE`<br/>`FRONTEND_DISABLE_SSE`| 1.0.0 |bool|`When set to true, clients are informed that the Server-Sent Events endpoint is not accessible.`|false|
|`FRONTEND_DEFAULT_LINK_PERMISSIONS`| 1.0.0 |int|`Defines the default permissions a link is being created with. Possible values are 0 (= internal link, for instance members only) and 1 (= public link with viewer permissions). Defaults to 1.`|1|
|`OC_URL`<br/>`FRONTEND_PUBLIC_URL`| 1.0.0 |string|`The public facing URL of the OpenCloud frontend.`|https://localhost:9200|
|`OC_MAX_CONCURRENCY`<br/>`FRONTEND_MAX_CONCURRENCY`| 1.0.0 |int|`Maximum number of concurrent go-routines. Higher values can potentially get work done faster but will also cause more load on the system. Values of 0 or below will be ignored and the default value will be used.`|1|
|`OC_INSECURE`<br/>`FRONTEND_APP_HANDLER_INSECURE`| 1.0.0 |bool|`Allow insecure connections to the frontend.`|false|
|`FRONTEND_APP_HANDLER_SECURE_VIEW_APP_ADDR`| 1.0.0 |string|`Service name or address of the app provider to use for secure view. Should match the service name or address of the registered CS3 app provider.`|eu.opencloud.api.collaboration|
|`FRONTEND_ARCHIVER_MAX_NUM_FILES`| 1.0.0 |int64|`Max number of files that can be packed into an archive.`|10000|
|`FRONTEND_ARCHIVER_MAX_SIZE`| 1.0.0 |int64|`Max size in bytes of the zip archive the archiver can create.`|1073741824|
|`OC_INSECURE`<br/>`FRONTEND_ARCHIVER_INSECURE`| 1.0.0 |bool|`Allow insecure connections to the archiver.`|false|
|`FRONTEND_DATA_GATEWAY_PREFIX`| 1.0.0 |string|`Path prefix for the data gateway.`|data|
|`FRONTEND_OCS_PREFIX`| 1.0.0 |string|`URL path prefix for the OCS service. Note that the string must not start with '/'.`|ocs|
|`FRONTEND_OCS_SHARE_PREFIX`| 1.0.0 |string|`Path prefix for shares as part of a CS3 resource. Note that the path must start with '/'.`|/Shares|
|`FRONTEND_OCS_PERSONAL_NAMESPACE`| 1.0.0 |string|`Home namespace identifier.`|/users/{{.Id.OpaqueId}}|
|`FRONTEND_OCS_ADDITIONAL_INFO_ATTRIBUTE`| 1.0.0 |string|`Additional information attribute for the user like {{.Mail}}.`|{{.Mail}}|
|`OC_CACHE_STORE`<br/>`FRONTEND_OCS_STAT_CACHE_STORE`| 1.0.0 |string|`The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.`|memory|
|`OC_CACHE_STORE_NODES`<br/>`FRONTEND_OCS_STAT_CACHE_STORE_NODES`| 1.0.0 |[]string|`A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.`|[127.0.0.1:9233]|
|`OC_CACHE_DATABASE`| 1.0.0 |string|`The database name the configured store should use.`|cache-stat|
|`FRONTEND_OCS_STAT_CACHE_TABLE`| 1.0.0 |string|`The database table the store should use.`||
|`OC_CACHE_TTL`<br/>`FRONTEND_OCS_STAT_CACHE_TTL`| 1.0.0 |Duration|`Default time to live for user info in the cache. Only applied when access tokens has no expiration. See the Environment Variable Types description for more details.`|5m0s|
|`OC_CACHE_DISABLE_PERSISTENCE`<br/>`FRONTEND_OCS_STAT_CACHE_DISABLE_PERSISTENCE`| 1.0.0 |bool|`Disable persistence of the cache. Only applies when using the 'nats-js-kv' store type. Defaults to false.`|false|
|`OC_CACHE_AUTH_USERNAME`<br/>`FRONTEND_OCS_STAT_CACHE_AUTH_USERNAME`| 1.0.0 |string|`The username to use for authentication. Only applies when using the 'nats-js-kv' store type.`||
|`OC_CACHE_AUTH_PASSWORD`<br/>`FRONTEND_OCS_STAT_CACHE_AUTH_PASSWORD`| 1.0.0 |string|`The password to use for authentication. Only applies when using the 'nats-js-kv' store type.`||
|`FRONTEND_OCS_ENABLE_DENIALS`| 1.0.0 |bool|`EXPERIMENTAL: enable the feature to deny access on folders.`|false|
|`OC_ENABLE_OCM`<br/>`FRONTEND_OCS_LIST_OCM_SHARES`| 1.0.0 |bool|`Include OCM shares when listing shares. See the OCM service documentation for more details.`|true|
|`OC_ENABLE_OCM`<br/>`FRONTEND_OCS_INCLUDE_OCM_SHAREES`| 1.0.0 |bool|`Include OCM sharees when listing sharees.`|false|
|`OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD`<br/>`FRONTEND_OCS_PUBLIC_SHARE_MUST_HAVE_PASSWORD`| 1.0.0 |bool|`Set this to true if you want to enforce passwords on all public shares.`|true|
|`OC_SHARING_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD`<br/>`FRONTEND_OCS_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD`| 1.0.0 |bool|`Set this to true if you want to enforce passwords for writable shares. Only effective if the setting for 'passwords on all public shares' is set to false.`|false|
|`OC_SHOW_USER_EMAIL_IN_RESULTS`| 1.0.0 |bool|`Include user email addresses in responses. If absent or set to false emails will be omitted from results. Please note that admin users can always see all email addresses.`|false|
|`FRONTEND_CHECKSUMS_SUPPORTED_TYPES`| 1.0.0 |[]string|`A list of checksum types that indicate to clients which hashes the server can use to verify upload integrity. Supported types are 'sha1', 'md5' and 'adler32'. See the Environment Variable Types description for more details.`|[sha1 md5 adler32]|
|`FRONTEND_CHECKSUMS_PREFERRED_UPLOAD_TYPE`| 1.0.0 |string|`The supported checksum type for uploads that indicates to clients supporting multiple hash algorithms which one is preferred by the server. Must be one out of the defined list of SUPPORTED_TYPES.`|sha1|
|`FRONTEND_READONLY_USER_ATTRIBUTES`| 1.0.0 |[]string|`A list of user attributes to indicate as read-only. Supported values: 'user.onPremisesSamAccountName' (username), 'user.displayName', 'user.mail', 'user.passwordProfile' (password), 'user.appRoleAssignments' (role), 'user.memberOf' (groups), 'user.accountEnabled' (login allowed), 'drive.quota' (quota). See the Environment Variable Types description for more details.`|[]|
|`OC_LDAP_SERVER_WRITE_ENABLED`<br/>`FRONTEND_LDAP_SERVER_WRITE_ENABLED`| 1.0.0 |bool|`Allow creating, modifying and deleting LDAP users via the GRAPH API. This can only be set to 'true' when keeping default settings for the LDAP user and group attribute types (the 'OC_LDAP_USER_SCHEMA_* and 'OC_LDAP_GROUP_SCHEMA_* variables).`|true|
|`FRONTEND_EDIT_LOGIN_ALLOWED_DISABLED`| 3.4.0 |bool|`Used to set if login is allowed/forbidden for for User.`|false|
|`FRONTEND_FULL_TEXT_SEARCH_ENABLED`| 1.0.0 |bool|`Set to true to signal the web client that full-text search is enabled.`|false|
|`FRONTEND_CHECK_FOR_UPDATES`| 3.6.0 |bool|`Enable automatic checking for updates. Defaults to true.`|true|
|`OC_EVENTS_ENDPOINT`<br/>`FRONTEND_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`FRONTEND_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|opencloud-cluster|
|`OC_INSECURE`<br/>`FRONTEND_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|false|
|`FRONTEND_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`OCS_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided NOTIFICATIONS_EVENTS_TLS_INSECURE will be seen as false.`||
|`OC_EVENTS_ENABLE_TLS`<br/>`FRONTEND_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`FRONTEND_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`FRONTEND_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`FRONTEND_AUTO_ACCEPT_SHARES`| 1.0.0 |bool|`Defines if shares should be auto accepted by default. Users can change this setting individually in their profile.`|true|
|`OC_SERVICE_ACCOUNT_ID`<br/>`FRONTEND_SERVICE_ACCOUNT_ID`| 1.0.0 |string|`The ID of the service account the service should use. See the 'auth-service' service description for more details.`||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`FRONTEND_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|`The service account secret.`||
|`OC_PASSWORD_POLICY_DISABLED`<br/>`FRONTEND_PASSWORD_POLICY_DISABLED`| 1.0.0 |bool|`Disable the password policy. Defaults to false if not set.`|false|
|`OC_PASSWORD_POLICY_MIN_CHARACTERS`<br/>`FRONTEND_PASSWORD_POLICY_MIN_CHARACTERS`| 1.0.0 |int|`Define the minimum password length. Defaults to 8 if not set.`|8|
|`OC_PASSWORD_POLICY_MIN_LOWERCASE_CHARACTERS`<br/>`FRONTEND_PASSWORD_POLICY_MIN_LOWERCASE_CHARACTERS`| 1.0.0 |int|`Define the minimum number of uppercase letters. Defaults to 1 if not set.`|1|
|`OC_PASSWORD_POLICY_MIN_UPPERCASE_CHARACTERS`<br/>`FRONTEND_PASSWORD_POLICY_MIN_UPPERCASE_CHARACTERS`| 1.0.0 |int|`Define the minimum number of lowercase letters. Defaults to 1 if not set.`|1|
|`OC_PASSWORD_POLICY_MIN_DIGITS`<br/>`FRONTEND_PASSWORD_POLICY_MIN_DIGITS`| 1.0.0 |int|`Define the minimum number of digits. Defaults to 1 if not set.`|1|
|`OC_PASSWORD_POLICY_MIN_SPECIAL_CHARACTERS`<br/>`FRONTEND_PASSWORD_POLICY_MIN_SPECIAL_CHARACTERS`| 1.0.0 |int|`Define the minimum number of characters from the special characters list to be present. Defaults to 1 if not set.`|1|
|`OC_PASSWORD_POLICY_BANNED_PASSWORDS_LIST`<br/>`FRONTEND_PASSWORD_POLICY_BANNED_PASSWORDS_LIST`| 1.0.0 |string|`Path to the 'banned passwords list' file. This only impacts public link password validation. See the documentation for more details.`||
|`FRONTEND_CONFIGURABLE_NOTIFICATIONS`| 1.0.0 |bool|`Allow configuring notifications via web client.`|false|
|`FRONTEND_GROUPWARE_ENABLED`| 3.7.0 |bool|`Enable groupware features. Defaults to false.`|false|
