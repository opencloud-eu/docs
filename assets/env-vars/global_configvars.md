#Environment variables with global scope available in multiple services

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
`IDM_CREATE_DEMO_USERS` | 1.0.0 | bool | The default role assignments the demo users should be setup. | false |
`OC_ADMIN_USER_ID` | 1.0.0 | string | ID of the user that should receive admin privileges. Consider that the UUID can be encoded in some LDAP deployment configurations like in .ldif files. These need to be decoded beforehand. |  |
`OC_ASYNC_UPLOADS` | 1.0.0 | bool | Enable asynchronous file uploads. | true |
`OC_CACHE_AUTH_PASSWORD` | 1.0.0 | string | The password to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured. |  |
`OC_CACHE_AUTH_USERNAME` | 1.0.0 | string | The username to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured. |  |
`OC_CACHE_DATABASE` | 1.0.0 | string | The database name the configured store should use. | cache-userinfo |
`OC_CACHE_DISABLE_PERSISTENCE` | 1.0.0 | bool | Disables persistence of the cache. Only applies when store type 'nats-js-kv' is configured. Defaults to false. | false |
`OC_CACHE_STORE` | 1.0.0 | string | The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details. | memory |
`OC_CACHE_STORE_NODES` | 1.0.0 | []string | A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details. | [127.0.0.1:9233] |
`OC_CACHE_TTL` | 1.0.0 | Duration | Default time to live for user info in the user info cache. Only applied when access tokens has no expiration. See the Environment Variable Types description for more details. | 10s |
`OC_CORS_ALLOW_CREDENTIALS` | 1.0.0 | bool | Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials. | false |
`OC_CORS_ALLOW_HEADERS` | 1.0.0 | []string | A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details. | [Origin Accept Content-Type Depth Authorization Ocs-Apirequest If-None-Match If-Match Destination Overwrite X-Request-Id X-Requested-With Tus-Resumable Tus-Checksum-Algorithm Upload-Concat Upload-Length Upload-Metadata Upload-Defer-Length Upload-Expires Upload-Checksum Upload-Offset X-HTTP-Method-Override Cache-Control] |
`OC_CORS_ALLOW_METHODS` | 1.0.0 | []string | A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details. | [OPTIONS HEAD GET PUT POST DELETE MKCOL PROPFIND PROPPATCH MOVE COPY REPORT SEARCH] |
`OC_CORS_ALLOW_ORIGINS` | 1.0.0 | []string | A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details. | [https://localhost:9200] |
`OC_DECOMPOSEDFS_PROPAGATOR` | 1.0.0 | string | The propagator used for decomposedfs. At the moment, only 'sync' is fully supported, 'async' is available as an experimental option. | sync |
`OC_DEFAULT_LANGUAGE` | 1.0.0 | string | The default language used by services and the WebUI. If not defined, English will be used as default. See the documentation for more details. |  |
`OC_DISABLE_VERSIONING` | 1.0.0 | bool | Disables versioning of files. When set to true, new uploads with the same filename will overwrite existing files instead of creating a new version. | false |
`OC_EDITION` | 1.0.0 | string | Edition of OpenCloud. Used for branding purposes. |  |
`OC_ENABLE_OCM` | 1.0.0 | bool | Include OCM sharees when listing users. | false |
`OC_EVENTS_AUTH_PASSWORD` | 1.0.0 | string | The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services. |  |
`OC_EVENTS_AUTH_USERNAME` | 1.0.0 | string | The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services. |  |
`OC_EVENTS_CLUSTER` | 1.0.0 | string | The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system. | opencloud-cluster |
`OC_EVENTS_ENABLE_TLS` | 1.0.0 | bool | Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services. | false |
`OC_EVENTS_ENDPOINT` | 1.0.0 | string | The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. | 127.0.0.1:9233 |
`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE` | 1.0.0 | string | The root CA certificate used to validate the server's TLS certificate. If provided NOTIFICATIONS_EVENTS_TLS_INSECURE will be seen as false. |  |
`OC_GATEWAY_GRPC_ADDR` | 1.0.0 | string | The bind address of the gateway GRPC address. | 127.0.0.1:9142 |
`OC_GRPC_CLIENT_TLS_CACERT` | 1.0.0 | string | Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services. |  |
`OC_GRPC_CLIENT_TLS_MODE` | 1.0.0 | string | TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification. |  |
`OC_GRPC_PROTOCOL` | 1.0.0 | string | The transport protocol of the GRPC service. |  |
`OC_HTTP_TLS_CERTIFICATE` | 1.0.0 | string | Path/File name of the TLS server certificate (in PEM format) for the http services. |  |
`OC_HTTP_TLS_ENABLED` | 1.0.0 | bool | Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true. | false |
`OC_HTTP_TLS_KEY` | 1.0.0 | string | Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services. |  |
`OC_INSECURE` | 1.0.0 | bool | Whether the NATS server should skip the client certificate verification during the TLS handshake. | false |
`OC_JWT_SECRET` | 1.0.0 | string | The secret to mint and validate jwt tokens. |  |
`OC_KEYCLOAK_BASE_PATH` | 1.0.0 | string | The URL to access keycloak. |  |
`OC_KEYCLOAK_CLIENT_ID` | 1.0.0 | string | The client id to authenticate with keycloak. |  |
`OC_KEYCLOAK_CLIENT_REALM` | 1.0.0 | string | The realm the client is defined in. |  |
`OC_KEYCLOAK_CLIENT_SECRET` | 1.0.0 | string | The client secret to use in authentication. |  |
`OC_KEYCLOAK_INSECURE_SKIP_VERIFY` | 1.0.0 | bool | Disable TLS certificate validation for Keycloak connections. Do not set this in production environments. | false |
`OC_KEYCLOAK_USER_REALM` | 1.0.0 | string | The realm users are defined. |  |
`OC_LDAP_BIND_DN` | 1.0.0 | string | LDAP DN to use for simple bind authentication with the target LDAP server. | uid=reva,ou=sysusers,o=libregraph-idm |
`OC_LDAP_BIND_PASSWORD` | 1.0.0 | string | Password to use for authenticating the 'bind_dn'. |  |
`OC_LDAP_CACERT` | 1.0.0 | string | Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the LDAP service. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm. | /home/opencloud/.opencloud/idm/ldap.crt |
`OC_LDAP_DISABLED_USERS_GROUP_DN` | 1.0.0 | string | The distinguished name of the group to which added users will be classified as disabled when 'disable_user_mechanism' is set to 'group'. | cn=DisabledUsersGroup,ou=groups,o=libregraph-idm |
`OC_LDAP_DISABLE_USER_MECHANISM` | 1.0.0 | string | An option to control the behavior for disabling users. Supported options are 'none', 'attribute' and 'group'. If set to 'group', disabling a user via API will add the user to the configured group for disabled users, if set to 'attribute' this will be done in the ldap user entry, if set to 'none' the disable request is not processed. Default is 'attribute'. | attribute |
`OC_LDAP_GROUP_BASE_DN` | 1.0.0 | string | Search base DN for looking up LDAP groups. | ou=groups,o=libregraph-idm |
`OC_LDAP_GROUP_FILTER` | 1.0.0 | string | LDAP filter to add to the default filters for group searches. |  |
`OC_LDAP_GROUP_OBJECTCLASS` | 1.0.0 | string | The object class to use for groups in the default group search filter ('groupOfNames'). | groupOfNames |
`OC_LDAP_GROUP_SCHEMA_DISPLAYNAME` | 1.0.0 | string | LDAP Attribute to use for the displayname of groups (often the same as groupname attribute). | cn |
`OC_LDAP_GROUP_SCHEMA_GROUPNAME` | 1.0.0 | string | LDAP Attribute to use for the name of groups. | cn |
`OC_LDAP_GROUP_SCHEMA_ID` | 1.0.0 | string | LDAP Attribute to use as the unique id for groups. This should be a stable globally unique ID like a UUID. | openCloudUUID |
`OC_LDAP_GROUP_SCHEMA_ID_IS_OCTETSTRING` | 1.0.0 | bool | Set this to true if the defined 'id' attribute for groups is of the 'OCTETSTRING' syntax. This is e.g. required when using the 'objectGUID' attribute of Active Directory for the group ID's. | false |
`OC_LDAP_GROUP_SCHEMA_MAIL` | 1.0.0 | string | LDAP Attribute to use for the email address of groups (can be empty). | mail |
`OC_LDAP_GROUP_SCHEMA_MEMBER` | 1.0.0 | string | LDAP Attribute that is used for group members. | member |
`OC_LDAP_GROUP_SCOPE` | 1.0.0 | string | LDAP search scope to use when looking up groups. Supported scopes are 'base', 'one' and 'sub'. | sub |
`OC_LDAP_INSECURE` | 1.0.0 | bool | Disable TLS certificate validation for the LDAP connections. Do not set this in production environments. | false |
`OC_LDAP_SERVER_WRITE_ENABLED` | 1.0.0 | bool | Allow creating, modifying and deleting LDAP users via the GRAPH API. This can only be set to 'true' when keeping default settings for the LDAP user and group attribute types (the 'OC_LDAP_USER_SCHEMA_* and 'OC_LDAP_GROUP_SCHEMA_* variables). | true |
`OC_LDAP_URI` | 1.0.0 | string | URI of the LDAP Server to connect to. Supported URI schemes are 'ldaps://' and 'ldap://' | ldaps://localhost:9235 |
`OC_LDAP_USER_BASE_DN` | 1.0.0 | string | Search base DN for looking up LDAP users. | ou=users,o=libregraph-idm |
`OC_LDAP_USER_ENABLED_ATTRIBUTE` | 1.0.0 | string | LDAP Attribute to use as a flag telling if the user is enabled or disabled. | openCloudUserEnabled |
`OC_LDAP_USER_FILTER` | 1.0.0 | string | LDAP filter to add to the default filters for user search like '(objectclass=openCloudUser)'. |  |
`OC_LDAP_USER_OBJECTCLASS` | 1.0.0 | string | The object class to use for users in the default user search filter ('inetOrgPerson'). | inetOrgPerson |
`OC_LDAP_USER_SCHEMA_DISPLAYNAME` | 1.0.0 | string | LDAP Attribute to use for the displayname of users. | displayname |
`OC_LDAP_USER_SCHEMA_ID` | 1.0.0 | string | LDAP Attribute to use as the unique id for users. This should be a stable globally unique id like a UUID. | openCloudUUID |
`OC_LDAP_USER_SCHEMA_ID_IS_OCTETSTRING` | 1.0.0 | bool | Set this to true if the defined 'ID' attribute for users is of the 'OCTETSTRING' syntax. This is e.g. required when using the 'objectGUID' attribute of Active Directory for the user ID's. | false |
`OC_LDAP_USER_SCHEMA_MAIL` | 1.0.0 | string | LDAP Attribute to use for the email address of users. | mail |
`OC_LDAP_USER_SCHEMA_USERNAME` | 1.0.0 | string | LDAP Attribute to use for username of users. | uid |
`OC_LDAP_USER_SCHEMA_USER_TYPE` | 1.0.0 | string | LDAP Attribute to distinguish between 'Member' and 'Guest' users. Default is 'openCloudUserType'. | openCloudUserType |
`OC_LDAP_USER_SCOPE` | 1.0.0 | string | LDAP search scope to use when looking up users. Supported scopes are 'base', 'one' and 'sub'. | sub |
`OC_LOG_COLOR` | 1.0.0 | bool | Activates colorized log output. | false |
`OC_LOG_FILE` | 1.0.0 | string | The path to the log file. Activates logging to this file if set. |  |
`OC_LOG_LEVEL` | 1.0.0 | string | The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'. |  |
`OC_LOG_PRETTY` | 1.0.0 | bool | Activates pretty log output. | false |
`OC_MACHINE_AUTH_API_KEY` | 1.0.0 | string | Machine auth API key used to validate internal requests necessary to access resources from other services. |  |
`OC_MAX_CONCURRENCY` | 1.0.0 | int | The maximum number of concurrent requests the service will handle. | 20 |
`OC_OIDC_ISSUER` | 1.0.0 | string | URL of the OIDC issuer. It defaults to URL of the builtin IDP. | https://localhost:9200 |
`OC_PASSWORD_POLICY_BANNED_PASSWORDS_LIST` | 1.0.0 | string | Path to the 'banned passwords list' file. This only impacts public link password validation. See the documentation for more details. |  |
`OC_PASSWORD_POLICY_DISABLED` | 1.0.0 | bool | Disable the password policy. Defaults to false if not set. | false |
`OC_PASSWORD_POLICY_MIN_CHARACTERS` | 1.0.0 | int | Define the minimum password length. Defaults to 8 if not set. | 8 |
`OC_PASSWORD_POLICY_MIN_DIGITS` | 1.0.0 | int | Define the minimum number of digits. Defaults to 1 if not set. | 1 |
`OC_PASSWORD_POLICY_MIN_LOWERCASE_CHARACTERS` | 1.0.0 | int | Define the minimum number of uppercase letters. Defaults to 1 if not set. | 1 |
`OC_PASSWORD_POLICY_MIN_SPECIAL_CHARACTERS` | 1.0.0 | int | Define the minimum number of characters from the special characters list to be present. Defaults to 1 if not set. | 1 |
`OC_PASSWORD_POLICY_MIN_UPPERCASE_CHARACTERS` | 1.0.0 | int | Define the minimum number of lowercase letters. Defaults to 1 if not set. | 1 |
`OC_PERSISTENT_STORE` | 1.0.0 | string | The type of the store. Supported values are: 'memory', 'nats-js-kv', 'redis-sentinel', 'noop'. See the text description for details. | nats-js-kv |
`OC_PERSISTENT_STORE_AUTH_PASSWORD` | 1.0.0 | string | The password to authenticate with the store. Only applies when store type 'nats-js-kv' is configured. |  |
`OC_PERSISTENT_STORE_AUTH_USERNAME` | 1.0.0 | string | The username to authenticate with the store. Only applies when store type 'nats-js-kv' is configured. |  |
`OC_PERSISTENT_STORE_NODES` | 1.0.0 | []string | A list of nodes to access the configured store. This has no effect when 'memory' store is configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details. | [127.0.0.1:9233] |
`OC_PERSISTENT_STORE_TTL` | 1.0.0 | Duration | Time to live for notifications in the store. Defaults to '336h' (2 weeks). See the Environment Variable Types description for more details. | 336h0m0s |
`OC_REVA_GATEWAY` | 1.0.0 | string | CS3 gateway used to look up user metadata | eu.opencloud.api.gateway |
`OC_SERVICE_ACCOUNT_ID` | 1.0.0 | string | The ID of the service account the service should use. See the 'auth-service' service description for more details. |  |
`OC_SERVICE_ACCOUNT_SECRET` | 1.0.0 | string | The service account secret. |  |
`OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD` | 1.0.0 | bool | Set this to true if you want to enforce passwords on all public shares. | true |
`OC_SHARING_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD` | 1.0.0 | bool | Set this to true if you want to enforce passwords for writable shares. Only effective if the setting for 'passwords on all public shares' is set to false. | false |
`OC_SHOW_USER_EMAIL_IN_RESULTS` | 1.0.0 | bool | Include user email addresses in responses. If absent or set to false emails will be omitted from results. Please note that admin users can always see all email addresses. | false |
`OC_SPACES_MAX_QUOTA` | 1.0.0 | uint64 | Set the global max quota value in bytes. A value of 0 equals unlimited. The value is provided via capabilities. | 0 |
`OC_SYSTEM_USER_API_KEY` | 1.0.0 | string | API key for the STORAGE-SYSTEM system user. |  |
`OC_SYSTEM_USER_ID` | 1.0.0 | string | ID of the OpenCloud STORAGE-SYSTEM system user. Admins need to set the ID for the STORAGE-SYSTEM system user in this config option which is then used to reference the user. Any reasonable long string is possible, preferably this would be an UUIDv4 format. |  |
`OC_SYSTEM_USER_IDP` | 1.0.0 | string | IDP of the OpenCloud STORAGE-SYSTEM system user. | internal |
`OC_TRACING_COLLECTOR` | 1.0.0 | string | The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset. |  |
`OC_TRACING_ENABLED` | 1.0.0 | bool | Activates tracing. | false |
`OC_TRACING_ENDPOINT` | 1.0.0 | string | The endpoint of the tracing agent. |  |
`OC_TRACING_TYPE` | 1.0.0 | string | The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now. |  |
`OC_TRANSFER_SECRET` | 1.0.0 | string | Transfer secret for signing file up- and download requests. |  |
`OC_TRANSLATION_PATH` | 1.0.0 | string | (optional) Set this to a path with custom translations to overwrite the builtin translations. Note that file and folder naming rules apply, see the documentation for more details. |  |
`OC_URL` | 1.0.0 | string | The public facing URL of the OpenCloud Web UI, used e.g. when sending notification eMails | https://localhost:9200 |
`OC_WOPI_DISABLE_CHAT` | 1.0.0 | bool | Disable the chat functionality of the office app. | false |
`STORAGE_USERS_ASYNC_PROPAGATOR_PROPAGATION_DELAY` | 1.0.0 | Duration | The delay between a change made to a tree and the propagation start on treesize and treetime. Multiple propagations are computed to a single one. See the Environment Variable Types description for more details. | 0s |
`STORAGE_USERS_PERMISSION_ENDPOINT` | 1.0.0 | string | Endpoint of the permissions service. The endpoints can differ for 'decomposed' and 'decomposeds3'. | eu.opencloud.api.settings |