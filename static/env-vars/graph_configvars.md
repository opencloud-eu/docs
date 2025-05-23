Environment variables for the **graph** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`GRAPH_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`GRAPH_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`GRAPH_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`GRAPH_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`GRAPH_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`GRAPH_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`GRAPH_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`GRAPH_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`OC_CACHE_STORE`<br/>`GRAPH_CACHE_STORE`| 1.0.0 |string|The type of the cache store. Supported values are: 'memory', 'redis-sentinel', 'nats-js-kv', 'noop'. See the text description for details.|memory|
|`OC_CACHE_STORE_NODES`<br/>`GRAPH_CACHE_STORE_NODES`| 1.0.0 |[]string|A list of nodes to access the configured store. This has no effect when 'memory' store are configured. Note that the behaviour how nodes are used is dependent on the library of the configured store. See the Environment Variable Types description for more details.|[127.0.0.1:9233]|
|`GRAPH_CACHE_STORE_DATABASE`| 1.0.0 |string|The database name the configured store should use.|cache-roles|
|`GRAPH_CACHE_STORE_TABLE`| 1.0.0 |string|The database table the store should use.||
|`OC_CACHE_TTL`<br/>`GRAPH_CACHE_TTL`| 1.0.0 |Duration|Time to live for cache records in the graph. Defaults to '336h' (2 weeks). See the Environment Variable Types description for more details.|336h0m0s|
|`OC_CACHE_DISABLE_PERSISTENCE`<br/>`GRAPH_CACHE_DISABLE_PERSISTENCE`| 1.0.0 |bool|Disables persistence of the cache. Only applies when store type 'nats-js-kv' is configured. Defaults to false.|false|
|`OC_CACHE_AUTH_USERNAME`<br/>`GRAPH_CACHE_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured.||
|`OC_CACHE_AUTH_PASSWORD`<br/>`GRAPH_CACHE_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the cache. Only applies when store type 'nats-js-kv' is configured.||
|`GRAPH_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9124|
|`GRAPH_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`GRAPH_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`GRAPH_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`GRAPH_HTTP_ADDR`| 1.0.0 |string|The bind address of the HTTP service.|127.0.0.1:9120|
|`GRAPH_HTTP_ROOT`| 1.0.0 |string|Subdirectory that serves as the root for this HTTP service.|/graph|
|`OC_HTTP_TLS_ENABLED`| 1.0.0 |bool|Activates TLS for the http based services using the server certifcate and key configured via OC_HTTP_TLS_CERTIFICATE and OC_HTTP_TLS_KEY. If OC_HTTP_TLS_CERTIFICATE is not set a temporary server certificate is generated - to be used with PROXY_INSECURE_BACKEND=true.|false|
|`OC_HTTP_TLS_CERTIFICATE`| 1.0.0 |string|Path/File name of the TLS server certificate (in PEM format) for the http services.||
|`OC_HTTP_TLS_KEY`| 1.0.0 |string|Path/File name for the TLS certificate key (in PEM format) for the server certificate to use for the http services.||
|`GRAPH_HTTP_API_TOKEN`| 1.0.0 |string|An optional API bearer token||
|`OC_CORS_ALLOW_ORIGINS`<br/>`GRAPH_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.|[*]|
|`OC_CORS_ALLOW_METHODS`<br/>`GRAPH_CORS_ALLOW_METHODS`| 1.0.0 |[]string|A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.|[GET POST PUT PATCH DELETE OPTIONS]|
|`OC_CORS_ALLOW_HEADERS`<br/>`GRAPH_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.|[Authorization Origin Content-Type Accept X-Requested-With X-Request-Id Purge Restore]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`GRAPH_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.|true|
|`GRAPH_GROUP_MEMBERS_PATCH_LIMIT`| 1.0.0 |int|The amount of group members allowed to be added with a single patch request.|20|
|`GRAPH_USERNAME_MATCH`| 1.0.0 |string|Apply restrictions to usernames. Supported values are 'default' and 'none'. When set to 'default', user names must not start with a number and are restricted to ASCII characters. When set to 'none', no restrictions are applied. The default value is 'default'.|default|
|`GRAPH_ASSIGN_DEFAULT_USER_ROLE`| 1.0.0 |bool|Whether to assign newly created users the default role 'User'. Set this to 'false' if you want to assign roles manually, or if the role assignment should happen at first login. Set this to 'true' (the default) to assign the role 'User' when creating a new user.|true|
|`GRAPH_IDENTITY_SEARCH_MIN_LENGTH`| 1.0.0 |int|The minimum length the search term needs to have for unprivileged users when searching for users or groups.|3|
|`OC_SHOW_USER_EMAIL_IN_RESULTS`| 1.0.0 |bool|Include user email addresses in responses. If absent or set to false emails will be omitted from results. Please note that admin users can always see all email addresses.|false|
|`OC_REVA_GATEWAY`| 1.0.0 |string|The CS3 gateway endpoint.|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.||
|`OC_JWT_SECRET`<br/>`GRAPH_JWT_SECRET`| 1.0.0 |string|The secret to mint and validate jwt tokens.||
|`GRAPH_APPLICATION_ID`| 1.0.0 |string|The OpenCloud application ID shown in the graph. All app roles are tied to this ID.||
|`GRAPH_APPLICATION_DISPLAYNAME`| 1.0.0 |string|The OpenCloud application name.|OpenCloud|
|`OC_URL`<br/>`GRAPH_SPACES_WEBDAV_BASE`| 1.0.0 |string|The public facing URL of WebDAV.|https://localhost:9200|
|`GRAPH_SPACES_WEBDAV_PATH`| 1.0.0 |string|The WebDAV sub-path for spaces.|/dav/spaces/|
|`GRAPH_SPACES_DEFAULT_QUOTA`| 1.0.0 |string|The default quota in bytes.|1000000000|
|`GRAPH_SPACES_EXTENDED_SPACE_PROPERTIES_CACHE_TTL`| 1.0.0 |int|Max TTL in seconds for the spaces property cache.|60000000000|
|`GRAPH_SPACES_USERS_CACHE_TTL`| 1.0.0 |int|Max TTL in seconds for the spaces users cache.|60000000000|
|`GRAPH_SPACES_GROUPS_CACHE_TTL`| 1.0.0 |int|Max TTL in seconds for the spaces groups cache.|60000000000|
|`GRAPH_SPACES_STORAGE_USERS_ADDRESS`| 1.0.0 |string|The address of the storage-users service.|eu.opencloud.api.storage-users|
|`OC_DEFAULT_LANGUAGE`| 1.0.0 |string|The default language used by services and the WebUI. If not defined, English will be used as default. See the documentation for more details.||
|`OC_TRANSLATION_PATH`<br/>`GRAPH_TRANSLATION_PATH`| 1.0.0 |string|(optional) Set this to a path with custom translations to overwrite the builtin translations. Note that file and folder naming rules apply, see the documentation for more details.||
|`GRAPH_IDENTITY_BACKEND`| 1.0.0 |string|The user identity backend to use. Supported backend types are 'ldap' and 'cs3'.|ldap|
|`OC_LDAP_URI`<br/>`GRAPH_LDAP_URI`| 1.0.0 |string|URI of the LDAP Server to connect to. Supported URI schemes are 'ldaps://' and 'ldap://'|ldaps://localhost:9235|
|`OC_LDAP_CACERT`<br/>`GRAPH_LDAP_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the LDAP service. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm.|/home/chaser/.opencloud/idm/ldap.crt|
|`OC_LDAP_INSECURE`<br/>`GRAPH_LDAP_INSECURE`| 1.0.0 |bool|Disable TLS certificate validation for the LDAP connections. Do not set this in production environments.|false|
|`OC_LDAP_BIND_DN`<br/>`GRAPH_LDAP_BIND_DN`| 1.0.0 |string|LDAP DN to use for simple bind authentication with the target LDAP server.|uid=libregraph,ou=sysusers,o=libregraph-idm|
|`OC_LDAP_BIND_PASSWORD`<br/>`GRAPH_LDAP_BIND_PASSWORD`| 1.0.0 |string|Password to use for authenticating the 'bind_dn'.||
|`GRAPH_LDAP_SERVER_UUID`| 1.0.0 |bool|If set to true, rely on the LDAP Server to generate a unique ID for users and groups, like when using 'entryUUID' as the user ID attribute.|false|
|`GRAPH_LDAP_SERVER_USE_PASSWORD_MODIFY_EXOP`| 1.0.0 |bool|Use the 'Password Modify Extended Operation' for updating user passwords.|true|
|`OC_LDAP_SERVER_WRITE_ENABLED`<br/>`GRAPH_LDAP_SERVER_WRITE_ENABLED`| 1.0.0 |bool|Allow creating, modifying and deleting LDAP users via the GRAPH API. This can only be set to 'true' when keeping default settings for the LDAP user and group attribute types (the 'OC_LDAP_USER_SCHEMA_* and 'OC_LDAP_GROUP_SCHEMA_* variables).|true|
|`GRAPH_LDAP_REFINT_ENABLED`| 1.0.0 |bool|Signals that the server has the refint plugin enabled, which makes some actions not needed.|false|
|`OC_LDAP_USER_BASE_DN`<br/>`GRAPH_LDAP_USER_BASE_DN`| 1.0.0 |string|Search base DN for looking up LDAP users.|ou=users,o=libregraph-idm|
|`OC_LDAP_USER_SCOPE`<br/>`GRAPH_LDAP_USER_SCOPE`| 1.0.0 |string|LDAP search scope to use when looking up users. Supported scopes are 'base', 'one' and 'sub'.|sub|
|`OC_LDAP_USER_FILTER`<br/>`GRAPH_LDAP_USER_FILTER`| 1.0.0 |string|LDAP filter to add to the default filters for user search like '(objectclass=openCloudUser)'.||
|`OC_LDAP_USER_OBJECTCLASS`<br/>`GRAPH_LDAP_USER_OBJECTCLASS`| 1.0.0 |string|The object class to use for users in the default user search filter ('inetOrgPerson').|inetOrgPerson|
|`OC_LDAP_USER_SCHEMA_MAIL`<br/>`GRAPH_LDAP_USER_EMAIL_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for the email address of users.|mail|
|`OC_LDAP_USER_SCHEMA_DISPLAYNAME`<br/>`GRAPH_LDAP_USER_DISPLAYNAME_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for the display name of users.|displayName|
|`OC_LDAP_USER_SCHEMA_USERNAME`<br/>`GRAPH_LDAP_USER_NAME_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for username of users.|uid|
|`OC_LDAP_USER_SCHEMA_ID`<br/>`GRAPH_LDAP_USER_UID_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use as the unique ID for users. This should be a stable globally unique ID like a UUID.|openCloudUUID|
|`OC_LDAP_USER_SCHEMA_ID_IS_OCTETSTRING`<br/>`GRAPH_LDAP_USER_SCHEMA_ID_IS_OCTETSTRING`| 1.0.0 |bool|Set this to true if the defined 'ID' attribute for users is of the 'OCTETSTRING' syntax. This is required when using the 'objectGUID' attribute of Active Directory for the user ID's.|false|
|`OC_LDAP_USER_SCHEMA_USER_TYPE`<br/>`GRAPH_LDAP_USER_TYPE_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to distinguish between 'Member' and 'Guest' users. Default is 'openCloudUserType'.|openCloudUserType|
|`OC_LDAP_USER_ENABLED_ATTRIBUTE`<br/>`GRAPH_USER_ENABLED_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use as a flag telling if the user is enabled or disabled.|openCloudUserEnabled|
|`OC_LDAP_DISABLE_USER_MECHANISM`<br/>`GRAPH_DISABLE_USER_MECHANISM`| 1.0.0 |string|An option to control the behavior for disabling users. Supported options are 'none', 'attribute' and 'group'. If set to 'group', disabling a user via API will add the user to the configured group for disabled users, if set to 'attribute' this will be done in the ldap user entry, if set to 'none' the disable request is not processed. Default is 'attribute'.|attribute|
|`OC_LDAP_DISABLED_USERS_GROUP_DN`<br/>`GRAPH_DISABLED_USERS_GROUP_DN`| 1.0.0 |string|The distinguished name of the group to which added users will be classified as disabled when 'disable_user_mechanism' is set to 'group'.|cn=DisabledUsersGroup,ou=groups,o=libregraph-idm|
|`OC_LDAP_GROUP_BASE_DN`<br/>`GRAPH_LDAP_GROUP_BASE_DN`| 1.0.0 |string|Search base DN for looking up LDAP groups.|ou=groups,o=libregraph-idm|
|`GRAPH_LDAP_GROUP_CREATE_BASE_DN`| 1.0.0 |string|Parent DN under which new groups are created. This DN needs to be subordinate to the 'GRAPH_LDAP_GROUP_BASE_DN'. This setting is only relevant when 'GRAPH_LDAP_SERVER_WRITE_ENABLED' is 'true'. It defaults to the value of 'GRAPH_LDAP_GROUP_BASE_DN'. All groups outside of this subtree are treated as readonly groups and cannot be updated.|ou=groups,o=libregraph-idm|
|`OC_LDAP_GROUP_SCOPE`<br/>`GRAPH_LDAP_GROUP_SEARCH_SCOPE`| 1.0.0 |string|LDAP search scope to use when looking up groups. Supported scopes are 'base', 'one' and 'sub'.|sub|
|`OC_LDAP_GROUP_FILTER`<br/>`GRAPH_LDAP_GROUP_FILTER`| 1.0.0 |string|LDAP filter to add to the default filters for group searches.||
|`OC_LDAP_GROUP_OBJECTCLASS`<br/>`GRAPH_LDAP_GROUP_OBJECTCLASS`| 1.0.0 |string|The object class to use for groups in the default group search filter ('groupOfNames').|groupOfNames|
|`OC_LDAP_GROUP_SCHEMA_GROUPNAME`<br/>`GRAPH_LDAP_GROUP_NAME_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for the name of groups.|cn|
|`OC_LDAP_GROUP_SCHEMA_MEMBER`<br/>`GRAPH_LDAP_GROUP_MEMBER_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute that is used for group members.|member|
|`OC_LDAP_GROUP_SCHEMA_ID`<br/>`GRAPH_LDAP_GROUP_ID_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use as the unique id for groups. This should be a stable globally unique ID like a UUID.|openCloudUUID|
|`OC_LDAP_GROUP_SCHEMA_ID_IS_OCTETSTRING`<br/>`GRAPH_LDAP_GROUP_SCHEMA_ID_IS_OCTETSTRING`| 1.0.0 |bool|Set this to true if the defined 'ID' attribute for groups is of the 'OCTETSTRING' syntax. This is required when using the 'objectGUID' attribute of Active Directory for the group ID's.|false|
|`GRAPH_LDAP_EDUCATION_RESOURCES_ENABLED`| 1.0.0 |bool|Enable LDAP support for managing education related resources.|false|
|`GRAPH_LDAP_SCHOOL_BASE_DN`| 1.0.0 |string|Search base DN for looking up LDAP schools.||
|`GRAPH_LDAP_SCHOOL_SEARCH_SCOPE`| 1.0.0 |string|LDAP search scope to use when looking up schools. Supported scopes are 'base', 'one' and 'sub'.||
|`GRAPH_LDAP_SCHOOL_FILTER`| 1.0.0 |string|LDAP filter to add to the default filters for school searches.||
|`GRAPH_LDAP_SCHOOL_OBJECTCLASS`| 1.0.0 |string|The object class to use for schools in the default school search filter.||
|`GRAPH_LDAP_SCHOOL_NAME_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for the name of a school.||
|`GRAPH_LDAP_SCHOOL_NUMBER_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use for the number of a school.||
|`GRAPH_LDAP_SCHOOL_ID_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to use as the unique id for schools. This should be a stable globally unique ID like a UUID.||
|`GRAPH_LDAP_SCHOOL_TERMINATION_MIN_GRACE_DAYS`| 1.0.0 |int|When setting a 'terminationDate' for a school, require the date to be at least this number of days in the future.|0|
|`OC_ENABLE_OCM`<br/>`GRAPH_INCLUDE_OCM_SHAREES`| 1.0.0 |bool|Include OCM sharees when listing users.|false|
|`OC_EVENTS_ENDPOINT`<br/>`GRAPH_EVENTS_ENDPOINT`| 1.0.0 |string|The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Set to a empty string to disable emitting events.|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`GRAPH_EVENTS_CLUSTER`| 1.0.0 |string|The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.|opencloud-cluster|
|`OC_INSECURE`<br/>`GRAPH_EVENTS_TLS_INSECURE`| 1.0.0 |bool|Whether to verify the server TLS certificates.|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`GRAPH_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|The root CA certificate used to validate the server's TLS certificate. If provided GRAPH_EVENTS_TLS_INSECURE will be seen as false.||
|`OC_EVENTS_ENABLE_TLS`<br/>`GRAPH_EVENTS_ENABLE_TLS`| 1.0.0 |bool|Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`GRAPH_EVENTS_AUTH_USERNAME`| 1.0.0 |string|The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`GRAPH_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.||
|`GRAPH_AVAILABLE_ROLES`| 1.0.0 |[]string|A comma separated list of roles that are available for assignment.|[b1e2218d-eef8-4d4c-b82d-0f1a1b48f3b5 a8d5fe5e-96e3-418d-825b-534dbdf22b99 fb6c3e19-e378-47e5-b277-9732f9de6e21 58c63c02-1d89-4572-916a-870abc5a1b7d 2d00ce52-1fc2-4dbc-8b95-a73b73395f5a 1c996275-f1c9-4e71-abdf-a42f6495e960 312c0871-5ef7-4b3a-85b6-0e4074c64049]|
|`OC_MAX_CONCURRENCY`<br/>`GRAPH_MAX_CONCURRENCY`| 1.0.0 |int|The maximum number of concurrent requests the service will handle.|20|
|`OC_KEYCLOAK_BASE_PATH`<br/>`GRAPH_KEYCLOAK_BASE_PATH`| 1.0.0 |string|The URL to access keycloak.||
|`OC_KEYCLOAK_CLIENT_ID`<br/>`GRAPH_KEYCLOAK_CLIENT_ID`| 1.0.0 |string|The client id to authenticate with keycloak.||
|`OC_KEYCLOAK_CLIENT_SECRET`<br/>`GRAPH_KEYCLOAK_CLIENT_SECRET`| 1.0.0 |string|The client secret to use in authentication.||
|`OC_KEYCLOAK_CLIENT_REALM`<br/>`GRAPH_KEYCLOAK_CLIENT_REALM`| 1.0.0 |string|The realm the client is defined in.||
|`OC_KEYCLOAK_USER_REALM`<br/>`GRAPH_KEYCLOAK_USER_REALM`| 1.0.0 |string|The realm users are defined.||
|`OC_KEYCLOAK_INSECURE_SKIP_VERIFY`<br/>`GRAPH_KEYCLOAK_INSECURE_SKIP_VERIFY`| 1.0.0 |bool|Disable TLS certificate validation for Keycloak connections. Do not set this in production environments.|false|
|`OC_SERVICE_ACCOUNT_ID`<br/>`GRAPH_SERVICE_ACCOUNT_ID`| 1.0.0 |string|The ID of the service account the service should use. See the 'auth-service' service description for more details.||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`GRAPH_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|The service account secret.||