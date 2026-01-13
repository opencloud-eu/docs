Environment variables for the **ocm** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_LOG_LEVEL`<br/>`OCM_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|error|
|`OCM_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9281|
|`OCM_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`OCM_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`OCM_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`OCM_HTTP_ADDR`| 1.0.0 |string|`The bind address of the HTTP service.`|127.0.0.1:9280|
|`OCM_HTTP_PROTOCOL`| 1.0.0 |string|`The transport protocol of the HTTP service.`|tcp|
|`OCM_HTTP_PREFIX`| 1.0.0 |string|`The path prefix where OCM can be accessed (defaults to /).`||
|`OC_CORS_ALLOW_ORIGINS`<br/>`OCM_CORS_ALLOW_ORIGINS`| 1.0.0 |[]string|`A list of allowed CORS origins. See following chapter for more details: *Access-Control-Allow-Origin* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin. See the Environment Variable Types description for more details.`|[https://localhost:9200]|
|`OC_CORS_ALLOW_METHODS`<br/>`OCM_CORS_ALLOW_METHODS`| 1.0.0 |[]string|`A list of allowed CORS methods. See following chapter for more details: *Access-Control-Request-Method* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method. See the Environment Variable Types description for more details.`|[OPTIONS HEAD GET PUT POST DELETE MKCOL PROPFIND PROPPATCH MOVE COPY REPORT SEARCH]|
|`OC_CORS_ALLOW_HEADERS`<br/>`OCM_CORS_ALLOW_HEADERS`| 1.0.0 |[]string|`A list of allowed CORS headers. See following chapter for more details: *Access-Control-Request-Headers* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers. See the Environment Variable Types description for more details.`|[Origin Accept Content-Type Depth Authorization Ocs-Apirequest If-None-Match If-Match Destination Overwrite X-Request-Id X-Requested-With Tus-Resumable Tus-Checksum-Algorithm Upload-Concat Upload-Length Upload-Metadata Upload-Defer-Length Upload-Expires Upload-Checksum Upload-Offset X-HTTP-Method-Override Cache-Control]|
|`OC_CORS_ALLOW_CREDENTIALS`<br/>`OCM_CORS_ALLOW_CREDENTIALS`| 1.0.0 |bool|`Allow credentials for CORS.See following chapter for more details: *Access-Control-Allow-Credentials* at \https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials.`|false|
|`OCM_GRPC_ADDR`| 1.0.0 |string|`The bind address of the GRPC service.`|127.0.0.1:9282|
|`OC_GRPC_PROTOCOL`<br/>`OCM_GRPC_PROTOCOL`| 1.0.0 |string|`The transport protocol of the GRPC service.`||
|`OC_SERVICE_ACCOUNT_ID`<br/>`OCM_SERVICE_ACCOUNT_ID`| 1.0.0 |string|`The ID of the service account the service should use. See the 'auth-service' service description for more details.`||
|`OC_SERVICE_ACCOUNT_SECRET`<br/>`OCM_SERVICE_ACCOUNT_SECRET`| 1.0.0 |string|`The service account secret.`||
|`OC_EVENTS_ENDPOINT`<br/>`OCM_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`OCM_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|opencloud-cluster|
|`OC_INSECURE`<br/>`OC_EVENTS_TLS_INSECURE`<br/>`OCM_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`OCM_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided OCM_EVENTS_TLS_INSECURE will be seen as false.`||
|`OC_EVENTS_ENABLE_TLS`<br/>`OCM_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`OCM_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`OCM_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_JWT_SECRET`<br/>`OCM_JWT_SECRET`| 1.0.0 |string|`The secret to mint and validate jwt tokens.`||
|`OC_REVA_GATEWAY`| 1.0.0 |string|`The CS3 gateway endpoint.`|eu.opencloud.api.gateway|
|`OC_GRPC_CLIENT_TLS_MODE`| 1.0.0 |string|`TLS mode for grpc connection to the go-micro based grpc services. Possible values are 'off', 'insecure' and 'on'. 'off': disables transport security for the clients. 'insecure' allows using transport security, but disables certificate verification (to be used with the autogenerated self-signed certificates). 'on' enables transport security, including server certificate verification.`||
|`OC_GRPC_CLIENT_TLS_CACERT`| 1.0.0 |string|`Path/File name for the root CA certificate (in PEM format) used to validate TLS server certificates of the go-micro based grpc services.`||
|`OCM_OCMD_PREFIX`| 1.0.0 |string|`URL path prefix for the OCMD service. Note that the string must not start with '/'.`|ocm|
|`OCM_OCMD_EXPOSE_RECIPIENT_DISPLAY_NAME`| 1.0.0 |bool|`Expose the display name of OCM share recipients.`|false|
|`OCM_SCIENCEMESH_PREFIX`| 1.0.0 |string|`URL path prefix for the ScienceMesh service. Note that the string must not start with '/'.`|sciencemesh|
|`OCM_MESH_DIRECTORY_URL`| 1.0.0 |string|`URL of the mesh directory service.`||
|`OCM_DIRECTORY_SERVICE_URLS`| 3.5.0 |string|`Space delimited URLs of the directory services.`||
|`OCM_INVITE_ACCEPT_DIALOG`| 3.5.0 |string|`/open-cloud-mesh/accept-invite;The frontend URL where to land when receiving an invitation`|/open-cloud-mesh/accept-invite|
|`OCM_OCM_INVITE_MANAGER_DRIVER`| 1.0.0 |string|`Driver to be used to persist OCM invites. Supported value is only 'json'.`|json|
|`OCM_OCM_INVITE_MANAGER_JSON_FILE`| 1.0.0 |string|`Path to the JSON file where OCM invite data will be stored. This file is maintained by the instance and must not be changed manually. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/ocm.`|/home/chaser/.opencloud/storage/ocm/ocminvites.json|
|`OCM_OCM_INVITE_MANAGER_TOKEN_EXPIRATION`| 1.0.0 |Duration|`Expiry duration for invite tokens.`|24h0m0s|
|`OCM_OCM_INVITE_MANAGER_TIMEOUT`| 1.0.0 |Duration|`Timeout specifies a time limit for requests made to OCM endpoints.`|30s|
|`OCM_OCM_INVITE_MANAGER_INSECURE`| 1.0.0 |bool|`Disable TLS certificate validation for the OCM connections. Do not set this in production environments.`|false|
|`SHARING_OCM_PROVIDER_AUTHORIZER_DRIVER`| 1.0.0 |string|`Driver to be used to persist ocm invites. Supported value is only 'json'.`|json|
|`OCM_OCM_PROVIDER_AUTHORIZER_PROVIDERS_FILE`| 1.0.0 |string|`Path to the JSON file where ocm invite data will be stored. Defaults to $OC_CONFIG_DIR/ocmproviders.json.`|/home/chaser/.opencloud/config/ocmproviders.json|
|`OCM_OCM_SHARE_PROVIDER_DRIVER`| 1.0.0 |string|`Driver to be used for the OCM share provider. Supported value is only 'json'.`|json|
|`OCM_OCM_SHAREPROVIDER_JSON_FILE`| 1.0.0 |string|`Path to the JSON file where OCM share data will be stored. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage.`|/home/chaser/.opencloud/storage/ocm/ocmshares.json|
|`OCM_OCM_SHARE_PROVIDER_INSECURE`| 1.0.0 |bool|`Disable TLS certificate validation for the OCM connections. Do not set this in production environments.`|false|
|`OCM_WEBAPP_TEMPLATE`| 1.0.0 |string|`Template for the webapp url.`||
|`OCM_OCM_CORE_DRIVER`| 1.0.0 |string|`Driver to be used for the OCM core. Supported value is only 'json'.`|json|
|`OCM_OCM_CORE_JSON_FILE`| 1.0.0 |string|`Path to the JSON file where OCM share data will be stored. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage.`|/home/chaser/.opencloud/storage/ocm/ocmshares.json|
|`OCM_OCM_STORAGE_PROVIDER_INSECURE`| 1.0.0 |bool|`Disable TLS certificate validation for the OCM connections. Do not set this in production environments.`|false|
|`OCM_OCM_STORAGE_PROVIDER_STORAGE_ROOT`| 1.0.0 |string|`Directory where the ocm storage provider persists its data like tus upload info files.`|/home/chaser/.opencloud/storage/ocm|
|`OCM_OCM_STORAGE_DATA_SERVER_URL`| 1.0.0 |string|`URL of the data server, needs to be reachable by the data gateway provided by the frontend service or the user if directly exposed.`|http://localhost:9280/data|
