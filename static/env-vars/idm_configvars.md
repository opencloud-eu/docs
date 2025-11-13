Environment variables for the **idm** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|:---|
|`OC_TRACING_ENABLED`<br/>`IDM_TRACING_ENABLED`| 1.0.0 |bool|`Activates tracing.`|`false`|
|`OC_TRACING_TYPE`<br/>`IDM_TRACING_TYPE`| 1.0.0 |string|`The type of tracing. Defaults to '', which is the same as 'jaeger'. Allowed tracing types are 'jaeger' and '' as of now.`|``|
|`OC_TRACING_ENDPOINT`<br/>`IDM_TRACING_ENDPOINT`| 1.0.0 |string|`The endpoint of the tracing agent.`|``|
|`OC_TRACING_COLLECTOR`<br/>`IDM_TRACING_COLLECTOR`| 1.0.0 |string|`The HTTP endpoint for sending spans directly to a collector, i.e. \http://jaeger-collector:14268/api/traces. Only used if the tracing endpoint is unset.`|``|
|`OC_LOG_LEVEL`<br/>`IDM_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|``|
|`OC_LOG_PRETTY`<br/>`IDM_LOG_PRETTY`| 1.0.0 |bool|`Activates pretty log output.`|`false`|
|`OC_LOG_COLOR`<br/>`IDM_LOG_COLOR`| 1.0.0 |bool|`Activates colorized log output.`|`false`|
|`OC_LOG_FILE`<br/>`IDM_LOG_FILE`| 1.0.0 |string|`The path to the log file. Activates logging to this file if set.`|``|
|`IDM_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|`127.0.0.1:9239`|
|`IDM_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`|``|
|`IDM_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|`false`|
|`IDM_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|`false`|
|`IDM_LDAPS_ADDR`| 1.0.0 |string|`Listen address for the LDAPS listener (ip-addr:port).`|`127.0.0.1:9235`|
|`IDM_LDAPS_CERT`| 1.0.0 |string|`File name of the TLS server certificate for the LDAPS listener. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm.`|`/Users/t.schweiger/.opencloud/idm/ldap.crt`|
|`IDM_LDAPS_KEY`| 1.0.0 |string|`File name for the TLS certificate key for the server certificate. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm.`|`/Users/t.schweiger/.opencloud/idm/ldap.key`|
|`IDM_DATABASE_PATH`| 1.0.0 |string|`Full path to the IDM backend database. If not defined, the root directory derives from $OC_BASE_DATA_PATH/idm.`|`/Users/t.schweiger/.opencloud/idm/idm.boltdb`|
|`IDM_CREATE_DEMO_USERS`| 1.0.0 |bool|`Flag to enable or disable the creation of the demo users.`|`false`|
|`OC_URL`<br/>`OC_OIDC_ISSUER`| 1.0.0 |string|`The OIDC issuer URL to assign to the demo users.`|`https://localhost:9200`|
|`IDM_ADMIN_PASSWORD`| 1.0.0 |string|`Password to set for the OpenCloud 'admin' user. Either cleartext or an argon2id hash.`|``|
|`IDM_SVC_PASSWORD`| 1.0.0 |string|`Password to set for the 'idm' service user. Either cleartext or an argon2id hash.`|``|
|`IDM_REVASVC_PASSWORD`| 1.0.0 |string|`Password to set for the 'reva' service user. Either cleartext or an argon2id hash.`|``|
|`IDM_IDPSVC_PASSWORD`| 1.0.0 |string|`Password to set for the 'idp' service user. Either cleartext or an argon2id hash.`|``|
|`OC_ADMIN_USER_ID`<br/>`IDM_ADMIN_USER_ID`| 1.0.0 |string|`ID of the user that should receive admin privileges. Consider that the UUID can be encoded in some LDAP deployment configurations like in .ldif files. These need to be decoded beforehand.`|``|
