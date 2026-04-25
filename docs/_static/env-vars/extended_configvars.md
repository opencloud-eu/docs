# Environment variables with extended scope not included in a service

| Name | Type | Default Value | Description |
|---|---|---|---|
`CS3_GATEWAY` |  |  | Adress of the CS3 backend |
`CS3_MACHINE_AUTH_API_KEY` |  |  | Authentication API-Key for CS3 backend |
`EXPERIMENTAL_REGISTER_INTERVAL` | duration | 25s | The interval at which services will re-register themselves with the registry to prevent expiry. Only change on supervision of openCloud Support. |
`EXPERIMENTAL_REGISTER_TTL` | duration | 30s | The time-to-live for a service registration in the registry. Services must re-register before this time to prevent expiry. Only change on supervision of openCloud Support. |
`GRPC_MAX_CONNECTION_AGE` | duration | 9223372036854775807 | Timeout for GRPC connections. After timeout, a new connection will be established automatically. The default value is in ns and is about 2.5 mio h. |
`MICRO_LOG_LEVEL` | string | Error | Set the log level for the internal go micro framework. Only change on supervision of openCloud Support. |
`MICRO_REGISTRY` | string | nats-js-kv | The type of registry to use. Only change on supervision of openCloud Support. |
`MICRO_REGISTRY_ADDRESS` | string | 127.0.0.1:9233 | The bind address of the internal natsjs registry. Only change on supervision of openCloud Support. |
`MICRO_REGISTRY_AUTH_PASSWORD` | string |  | Optional when using nats to authenticate with the nats cluster. |
`MICRO_REGISTRY_AUTH_USERNAME` | string |  | Optional when using nats to authenticate with the nats cluster. |
`OC_BASE_DATA_PATH` | string |  | The base directory location used by several services and for user data. See the General Info section in the documentation for more details on defaults. Services can have, if available, an individual setting with an own environment variable. |
`OC_CI_ENVIRONMENT` |  |  |  |
`OC_CONFIG_DIR` | string |  | The default directory location for config files. See the General Info section in the documentation for more details on defaults. |
`OC_GRPC_MAX_RECEIVED_MESSAGE_SIZE` | integer | 10240000 | Sets the maximum message size in bytes the GRPC client can receive. |