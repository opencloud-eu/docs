Environment variables for the **users** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_TRACING_ENABLED`<br/>`USERS_TRACING_ENABLED`| 1.0.0 |bool|Activates tracing.|false|
|`OC_TRACING_TYPE`<br/>`USERS_TRACING_TYPE`| 1.0.0 |string|The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.||
|`OC_TRACING_ENDPOINT`<br/>`USERS_TRACING_ENDPOINT`| 1.0.0 |string|The endpoint of the tracing agent.||
|`OC_TRACING_COLLECTOR`<br/>`USERS_TRACING_COLLECTOR`| 1.0.0 |string|The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.||
|`OC_LOG_LEVEL`<br/>`USERS_LOG_LEVEL`| 1.0.0 |string|The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.||
|`OC_LOG_PRETTY`<br/>`USERS_LOG_PRETTY`| 1.0.0 |bool|Activates pretty log output.|false|
|`OC_LOG_COLOR`<br/>`USERS_LOG_COLOR`| 1.0.0 |bool|Activates colorized log output.|false|
|`OC_LOG_FILE`<br/>`USERS_LOG_FILE`| 1.0.0 |string|The path to the log file. Activates logging to this file if set.||
|`USERS_DEBUG_ADDR`| 1.0.0 |string|Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.|127.0.0.1:9145|
|`USERS_DEBUG_TOKEN`| 1.0.0 |string|Token to secure the metrics endpoint.||
|`USERS_DEBUG_PPROF`| 1.0.0 |bool|Enables pprof, which can be used for profiling.|false|
|`USERS_DEBUG_ZPAGES`| 1.0.0 |bool|Enables zpages, which can be used for collecting and viewing in-memory traces.|false|
|`USERS_GRPC_ADDR`| 1.0.0 |string|The bind address of the GRPC service.|127.0.0.1:9144|
|`OC_GRPC_PROTOCOL`<br/>`USERS_GRPC_PROTOCOL`| 1.0.0 |string|The transport protocol of the GPRC service.|tcp|
|`OC_JWT_SECRET`<br/>`USERS_JWT_SECRET`| 1.0.0 |string|The secret to mint and validate jwt tokens.||
|`OC_REVA_GATEWAY`| 1.0.0 |string|The CS3 gateway endpoint.|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.||
|`USERS_SKIP_USER_GROUPS_IN_TOKEN`| 1.0.0 |bool|Disables the loading of user's group memberships from the reva access token.|false|
|`USERS_DRIVER`| 1.0.0 |string|The driver which should be used by the users service. Supported values are 'ldap' and 'owncloudsql'.|ldap|
|`OC_LDAP_URI`<br/>`USERS_LDAP_URI`| 1.0.0 |string|URI of the LDAP Server to connect to. Supported URI schemes are 'ldaps://' and 'ldap://'|ldaps://localhost:9235|
|`OC_LDAP_CACERT`<br/>`USERS_LDAP_CACERT`| 1.0.0 |string|Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the LDAP service. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm.|/home/chaser/.opencloud/idm/ldap.crt|
|`OC_LDAP_INSECURE`<br/>`USERS_LDAP_INSECURE`| 1.0.0 |bool|Disable TLS certificate validation for the LDAP connections. Do not set this in production environments.|false|
|`OC_LDAP_BIND_DN`<br/>`USERS_LDAP_BIND_DN`| 1.0.0 |string|LDAP DN to use for simple bind authentication with the target LDAP server.|uid=reva,ou=sysusers,o=libregraph-idm|
|`OC_LDAP_BIND_PASSWORD`<br/>`USERS_LDAP_BIND_PASSWORD`| 1.0.0 |string|Password to use for authenticating the 'bind_dn'.||
|`OC_LDAP_USER_BASE_DN`<br/>`USERS_LDAP_USER_BASE_DN`| 1.0.0 |string|Search base DN for looking up LDAP users.|ou=users,o=libregraph-idm|
|`OC_LDAP_GROUP_BASE_DN`<br/>`USERS_LDAP_GROUP_BASE_DN`| 1.0.0 |string|Search base DN for looking up LDAP groups.|ou=groups,o=libregraph-idm|
|`OC_LDAP_USER_SCOPE`<br/>`USERS_LDAP_USER_SCOPE`| 1.0.0 |string|LDAP search scope to use when looking up users. Supported values are 'base', 'one' and 'sub'.|sub|
|`OC_LDAP_GROUP_SCOPE`<br/>`USERS_LDAP_GROUP_SCOPE`| 1.0.0 |string|LDAP search scope to use when looking up groups. Supported values are 'base', 'one' and 'sub'.|sub|
|`LDAP_USER_SUBSTRING_FILTER_TYPE`<br/>`USERS_LDAP_USER_SUBSTRING_FILTER_TYPE`| 1.0.0 |string|Type of substring search filter to use for substring searches for users. Possible values: 'initial' for doing prefix only searches, 'final' for doing suffix only searches or 'any' for doing full substring searches|any|
|`OC_LDAP_USER_FILTER`<br/>`USERS_LDAP_USER_FILTER`| 1.0.0 |string|LDAP filter to add to the default filters for user search like '(objectclass=openCloudUser)'.||
|`OC_LDAP_GROUP_FILTER`<br/>`USERS_LDAP_GROUP_FILTER`| 1.0.0 |string|LDAP filter to add to the default filters for group searches.||
|`OC_LDAP_USER_OBJECTCLASS`<br/>`USERS_LDAP_USER_OBJECTCLASS`| 1.0.0 |string|The object class to use for users in the default user search filter like 'inetOrgPerson'.|inetOrgPerson|
|`OC_LDAP_GROUP_OBJECTCLASS`<br/>`USERS_LDAP_GROUP_OBJECTCLASS`| 1.0.0 |string|The object class to use for groups in the default group search filter like 'groupOfNames'.|groupOfNames|
|`OC_URL`<br/>`OC_OIDC_ISSUER`<br/>`USERS_IDP_URL`| 1.0.0 |string|The identity provider value to set in the userids of the CS3 user objects for users returned by this user provider.|https://localhost:9200|
|`OC_LDAP_DISABLE_USER_MECHANISM`<br/>`USERS_LDAP_DISABLE_USER_MECHANISM`| 1.0.0 |string|An option to control the behavior for disabling users. Valid options are 'none', 'attribute' and 'group'. If set to 'group', disabling a user via API will add the user to the configured group for disabled users, if set to 'attribute' this will be done in the ldap user entry, if set to 'none' the disable request is not processed.|attribute|
|`OC_LDAP_USER_SCHEMA_USER_TYPE`<br/>`USERS_LDAP_USER_TYPE_ATTRIBUTE`| 1.0.0 |string|LDAP Attribute to distinguish between 'Member' and 'Guest' users. Default is 'openCloudUserType'.|openCloudUserType|
|`OC_LDAP_DISABLED_USERS_GROUP_DN`<br/>`USERS_LDAP_DISABLED_USERS_GROUP_DN`| 1.0.0 |string|The distinguished name of the group to which added users will be classified as disabled when 'disable_user_mechanism' is set to 'group'.|cn=DisabledUsersGroup,ou=groups,o=libregraph-idm|
|`OC_LDAP_USER_SCHEMA_ID`<br/>`USERS_LDAP_USER_SCHEMA_ID`| 1.0.0 |string|LDAP Attribute to use as the unique ID for users. This should be a stable globally unique ID like a UUID.|openclouduuid|
|`OC_LDAP_USER_SCHEMA_ID_IS_OCTETSTRING`<br/>`USERS_LDAP_USER_SCHEMA_ID_IS_OCTETSTRING`| 1.0.0 |bool|Set this to true if the defined 'ID' attribute for users is of the 'OCTETSTRING' syntax. This is e.g. required when using the 'objectGUID' attribute of Active Directory for the user ID's.|false|
|`OC_LDAP_USER_SCHEMA_MAIL`<br/>`USERS_LDAP_USER_SCHEMA_MAIL`| 1.0.0 |string|LDAP Attribute to use for the email address of users.|mail|
|`OC_LDAP_USER_SCHEMA_DISPLAYNAME`<br/>`USERS_LDAP_USER_SCHEMA_DISPLAYNAME`| 1.0.0 |string|LDAP Attribute to use for the displayname of users.|displayname|
|`OC_LDAP_USER_SCHEMA_USERNAME`<br/>`USERS_LDAP_USER_SCHEMA_USERNAME`| 1.0.0 |string|LDAP Attribute to use for username of users.|uid|
|`OC_LDAP_USER_ENABLED_ATTRIBUTE`<br/>`USERS_LDAP_USER_ENABLED_ATTRIBUTE`| 1.0.0 |string|LDAP attribute to use as a flag telling if the user is enabled or disabled.|openclouduserenabled|
|`OC_LDAP_GROUP_SCHEMA_ID`<br/>`USERS_LDAP_GROUP_SCHEMA_ID`| 1.0.0 |string|LDAP Attribute to use as the unique ID for groups. This should be a stable globally unique ID like a UUID.|openclouduuid|
|`OC_LDAP_GROUP_SCHEMA_ID_IS_OCTETSTRING`<br/>`USERS_LDAP_GROUP_SCHEMA_ID_IS_OCTETSTRING`| 1.0.0 |bool|Set this to true if the defined 'id' attribute for groups is of the 'OCTETSTRING' syntax. This is e.g. required when using the 'objectGUID' attribute of Active Directory for the group ID's.|false|
|`OC_LDAP_GROUP_SCHEMA_MAIL`<br/>`USERS_LDAP_GROUP_SCHEMA_MAIL`| 1.0.0 |string|LDAP Attribute to use for the email address of groups (can be empty).|mail|
|`OC_LDAP_GROUP_SCHEMA_DISPLAYNAME`<br/>`USERS_LDAP_GROUP_SCHEMA_DISPLAYNAME`| 1.0.0 |string|LDAP Attribute to use for the displayname of groups (often the same as groupname attribute).|cn|
|`OC_LDAP_GROUP_SCHEMA_GROUPNAME`<br/>`USERS_LDAP_GROUP_SCHEMA_GROUPNAME`| 1.0.0 |string|LDAP Attribute to use for the name of groups.|cn|
|`OC_LDAP_GROUP_SCHEMA_MEMBER`<br/>`USERS_LDAP_GROUP_SCHEMA_MEMBER`| 1.0.0 |string|LDAP Attribute that is used for group members.|member|
|`USERS_OWNCLOUDSQL_DB_USERNAME`| 1.0.0 |string|Database user to use for authenticating with the owncloud database.|owncloud|
|`USERS_OWNCLOUDSQL_DB_PASSWORD`| 1.0.0 |string|Password for the database user.|secret|
|`USERS_OWNCLOUDSQL_DB_HOST`| 1.0.0 |string|Hostname of the database server.|mysql|
|`USERS_OWNCLOUDSQL_DB_PORT`| 1.0.0 |int|Network port to use for the database connection.|3306|
|`USERS_OWNCLOUDSQL_DB_NAME`| 1.0.0 |string|Name of the owncloud database.|owncloud|
|`USERS_OWNCLOUDSQL_IDP`| 1.0.0 |string|The identity provider value to set in the userids of the CS3 user objects for users returned by this user provider.|https://localhost:9200|
|`USERS_OWNCLOUDSQL_NOBODY`| 1.0.0 |int64|Fallback number if no numeric UID and GID properties are provided.|90|
|`USERS_OWNCLOUDSQL_JOIN_USERNAME`| 1.0.0 |bool|Join the user properties table to read usernames|false|
|`USERS_OWNCLOUDSQL_JOIN_OWNCLOUD_UUID`| 1.0.0 |bool|Join the user properties table to read user IDs.|false|
|`USERS_OWNCLOUDSQL_ENABLE_MEDIAL_SEARCH`| 1.0.0 |bool|Allow 'medial search' when searching for users instead of just doing a prefix search. This allows finding 'Alice' when searching for 'lic'.|false|