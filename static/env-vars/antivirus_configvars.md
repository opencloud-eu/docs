Environment variables for the **antivirus** service

| Name | Introduction Version | Type | Description | Default Value |
|---|---|---|---|---|
|`OC_LOG_LEVEL`<br/>`ANTIVIRUS_LOG_LEVEL`| 1.0.0 |string|`The log level. Valid values are: 'panic', 'fatal', 'error', 'warn', 'info', 'debug', 'trace'.`|error|
|`ANTIVIRUS_DEBUG_ADDR`| 1.0.0 |string|`Bind address of the debug server, where metrics, health, config and debug endpoints will be exposed.`|127.0.0.1:9277|
|`ANTIVIRUS_DEBUG_TOKEN`| 1.0.0 |string|`Token to secure the metrics endpoint.`||
|`ANTIVIRUS_DEBUG_PPROF`| 1.0.0 |bool|`Enables pprof, which can be used for profiling.`|false|
|`ANTIVIRUS_DEBUG_ZPAGES`| 1.0.0 |bool|`Enables zpages, which can be used for collecting and viewing in-memory traces.`|false|
|`ANTIVIRUS_INFECTED_FILE_HANDLING`| 1.0.0 |string|`Defines the behaviour when a virus has been found. Supported options are: 'delete', 'continue' and 'abort '. Delete will delete the file. Continue will mark the file as infected but continues further processing. Abort will keep the file in the uploads folder for further admin inspection and will not move it to its final destination.`|delete|
|`OC_EVENTS_ENDPOINT`<br/>`ANTIVIRUS_EVENTS_ENDPOINT`| 1.0.0 |string|`The address of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture.`|127.0.0.1:9233|
|`OC_EVENTS_CLUSTER`<br/>`ANTIVIRUS_EVENTS_CLUSTER`| 1.0.0 |string|`The clusterID of the event system. The event system is the message queuing service. It is used as message broker for the microservice architecture. Mandatory when using NATS as event system.`|opencloud-cluster|
|`OC_INSECURE`<br/>`OC_EVENTS_TLS_INSECURE`<br/>`ANTIVIRUS_EVENTS_TLS_INSECURE`| 1.0.0 |bool|`Whether to verify the server TLS certificates.`|false|
|`OC_EVENTS_TLS_ROOT_CA_CERTIFICATE`<br/>`ANTIVIRUS_EVENTS_TLS_ROOT_CA_CERTIFICATE`| 1.0.0 |string|`The root CA certificate used to validate the server's TLS certificate. If provided ANTIVIRUS_EVENTS_TLS_INSECURE will be seen as false.`||
|`OC_EVENTS_ENABLE_TLS`<br/>`ANTIVIRUS_EVENTS_ENABLE_TLS`| 1.0.0 |bool|`Enable TLS for the connection to the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`|false|
|`OC_EVENTS_AUTH_USERNAME`<br/>`ANTIVIRUS_EVENTS_AUTH_USERNAME`| 1.0.0 |string|`The username to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`OC_EVENTS_AUTH_PASSWORD`<br/>`ANTIVIRUS_EVENTS_AUTH_PASSWORD`| 1.0.0 |string|`The password to authenticate with the events broker. The events broker is the OpenCloud service which receives and delivers events between the services.`||
|`ANTIVIRUS_WORKERS`| 1.0.0 |int|`The number of concurrent go routines that fetch events from the event queue.`|10|
|`ANTIVIRUS_SCANNER_TYPE`| 1.0.0 |ScannerType|`The antivirus scanner to use. Supported values are 'clamav' and 'icap'.`|clamav|
|`ANTIVIRUS_CLAMAV_SOCKET`| 1.0.0 |string|`The socket clamav is running on. Note the default value is an example which needs adaption according your OS.`|/run/clamav/clamd.ctl|
|`ANTIVIRUS_CLAMAV_SCAN_TIMEOUT`| 2.1.0 |Duration|`Scan timeout for the ClamAV client. Defaults to '5m' (5 minutes). See the Environment Variable Types description for more details.`|5m0s|
|`ANTIVIRUS_ICAP_SCAN_TIMEOUT`| 1.0.0 |Duration|`Scan timeout for the ICAP client. Defaults to '5m' (5 minutes). See the Environment Variable Types description for more details.`|5m0s|
|`ANTIVIRUS_ICAP_URL`| 1.0.0 |string|`URL of the ICAP server.`|icap://127.0.0.1:1344|
|`ANTIVIRUS_ICAP_SERVICE`| 1.0.0 |string|`The name of the ICAP service.`|avscan|
|`ANTIVIRUS_MAX_SCAN_SIZE`| 1.0.0 |string|`The maximum scan size the virus scanner can handle.0 means unlimited. Usable common abbreviations: [KB, KiB, MB, MiB, GB, GiB, TB, TiB, PB, PiB, EB, EiB], example: 2GB.`|100MB|
|`ANTIVIRUS_MAX_SCAN_SIZE_MODE`| 2.1.0 |MaxScanSizeMode|`Defines the mode of handling files that exceed the maximum scan size. Supported options are: 'skip', which skips files that are bigger than the max scan size, and 'truncate' (default), which only uses the file up to the max size.`|partial|
|`ANTIVIRUS_DEBUG_SCAN_OUTCOME`| 1.0.0 |string|`A predefined outcome for virus scanning, FOR DEBUG PURPOSES ONLY! (example values: 'found,infected')`||
