---
sidebar_position: 1
id: config-options
title: Configuration Options
draft: true
---

## Configuration Options Overview

The configuration of OpenCloud is mainly done via environment variables. These variables are always written in capital letters, with words connected by underscores. They start with the name of the service. If the service name consists of several words separated by a hyphen, this is replaced by an underscore. Example: 'auth-basic' becomes 'AUTH_BASIC_XXX'.

There are also global environment variables that begin with 'OC_'. These have a global scope and their setting applies to all services unless they are explicitly overwritten by a corresponding service variable.

Environment variables can also be used within YAML configuration files. This makes it possible to use dynamic values in static configuration files, which increases the flexibility and customizability of the configuration.

### Basic Settings
| env Variable                          |  Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| LOG_DRIVER                      | String  | Defines the Docker Compose log driver used.                            | local                                               |
| INSECURE                        | Boolean | Skips certificate validation for OpenCloud parts when using self-signed certificates. | true (should be commented out on internet-facing servers) |

### Traefik Settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| TRAEFIK_DASHBOARD               | Boolean | Enables serving the Traefik dashboard.                             | false                                               |
| TRAEFIK_DOMAIN                  | String  | Sets the domain for the Traefik dashboard.                         | traefik.opencloud.test                              |
| TRAEFIK_BASIC_AUTH_USERS        | String  | Configures basic authentication for the Traefik dashboard.         | admin:admin (user "admin", password "admin")        |
| TRAEFIK_ACME_MAIL               | String  | Specifies the email address for obtaining Let's Encrypt certificates. | None                          |
| TRAEFIK_ACME_CASERVER           | String  | Used for testing the certificate process.                          | None                            |

### OpenCloud Settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| OPENCLOUD                       | String | Enables the core OpenCloud service.                                | :opencloud.yml                                      |
| OC_DOCKER_IMAGE                 | String  | Defines the OpenCloud container image.                             | opencloudeu/opencloud-rolling                      |
| OC_DOCKER_TAG                   | String  | Specifies the OpenCloud container version.                         | latest                                             |
| OC_DOMAIN                       | String  | Sets the domain for the OpenCloud frontend.                        | cloud.opencloud.test                               |
| ADMIN_PASSWORD                  | String  | Sets the OpenCloud admin user password.                            | admin                                              |
| DEMO_USERS                      | Boolean | Determines whether demo users are created.                         | false                                              |
| LOG_LEVEL                       | String  | Defines the OpenCloud log level.                                   | None                           |
| OC_CONFIG_DIR                   | String  | Defines the OpenCloud configuration storage location.              | /your/local/opencloud/config (example path)        |
| OC_DATA_DIR                     | String  | Defines the OpenCloud data storage location.                       | /your/local/opencloud/data (example path)         |


### S3 Storage configuration - optional

| Variable                   | Env Variable(s)                                                 | YAML Variable                          | Type    | Description                                                                                                                                      | Default Value |
|----------------------------------|----------------------------------------------------------------|----------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Root                             | STORAGE_USERS_DECOMPOSEDS3_ROOT                                | root                                   | string  | The directory where the filesystem storage will store metadata for blobs. If not defined, the root directory derives from $OC_BASE_DATA_PATH/storage/users. |              |
| UserLayout                       | STORAGE_USERS_DECOMPOSEDS3_USER_LAYOUT                        | user_layout                            | string  | Template string for the user storage layout in the user directory.                                         |              |
| PermissionsEndpoint              | STORAGE_USERS_PERMISSION_ENDPOINT;STORAGE_USERS_DECOMPOSEDS3_PERMISSIONS_ENDPOINT | permissions_endpoint                  | string  | Endpoint of the permissions service. The endpoints can differ for 'decomposed' and 'decomposeds3'        |              |
| Region                           | STORAGE_USERS_DECOMPOSEDS3_REGION                             | region                                 | string  | Region of the S3 bucket.                                                                                     |              |
| AccessKey                        | STORAGE_USERS_DECOMPOSEDS3_ACCESS_KEY                         | access_key                             | string  | Access key for the S3 bucket.                                                                               |              |
| SecretKey                        | STORAGE_USERS_DECOMPOSEDS3_SECRET_KEY                         | secret_key                             | string  | Secret key for the S3 bucket.                                                                               |              |
| Endpoint                         | STORAGE_USERS_DECOMPOSEDS3_ENDPOINT                           | endpoint                               | string  | Endpoint for the S3 bucket.                                                                                 |              |
| Bucket                           | STORAGE_USERS_DECOMPOSEDS3_BUCKET                             | bucket                                 | string  | Name of the S3 bucket.                                                                                      |              |
| DisableContentSha256             | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_DISABLE_CONTENT_SHA256  | put_object_disable_content_sha256      | bool    | Disable sending content sha256 when copying objects to S3.                                                 |              |
| DisableMultipart                 | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_DISABLE_MULTIPART       | put_object_disable_multipart           | bool    | Disable multipart uploads when copying objects to S3.                                                      |              |
| SendContentMd5                   | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_SEND_CONTENT_MD5        | put_object_send_content_md5            | bool    | Send a Content-MD5 header when copying objects to S3.                                                      |              |
| ConcurrentStreamParts            | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_CONCURRENT_STREAM_PARTS | put_object_concurrent_stream_parts     | bool    | Always precreate parts when copying objects to S3.                                                         |              |
| NumThreads                       | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_NUM_THREADS             | put_object_num_threads                 | uint    | Number of concurrent uploads to use when copying objects to S3.                                            |              |
| PartSize                         | STORAGE_USERS_DECOMPOSEDS3_PUT_OBJECT_PART_SIZE               | put_object_part_size                   | uint64  | Part size for concurrent uploads to S3. If no value or 0 is set, the default is 16MB (min 5MB, max 5GB).   |              |
| PersonalSpaceAliasTemplate       | STORAGE_USERS_DECOMPOSEDS3_PERSONAL_SPACE_ALIAS_TEMPLATE      | personalspacealias_template            | string  | Template string to construct personal space aliases.                                                       |              |
| PersonalSpacePathTemplate        | STORAGE_USERS_DECOMPOSEDS3_PERSONAL_SPACE_PATH_TEMPLATE       | personalspacepath_template             | string  | Template string to construct the paths of the personal space roots.                                        |              |
| GeneralSpaceAliasTemplate        | STORAGE_USERS_DECOMPOSEDS3_GENERAL_SPACE_ALIAS_TEMPLATE       | generalspacealias_template             | string  | Template string to construct general space aliases.                                                        |              |
| GeneralSpacePathTemplate         | STORAGE_USERS_DECOMPOSEDS3_GENERAL_SPACE_PATH_TEMPLATE        | generalspacepath_template              | string  | Template string to construct the paths of the project space roots.                                         |              |
| ShareFolder                      | STORAGE_USERS_DECOMPOSEDS3_SHARE_FOLDER                       | share_folder                           | string  | Name of the folder jailing all shares.                                                                     |              |
| MaxAcquireLockCycles             | STORAGE_USERS_DECOMPOSEDS3_MAX_ACQUIRE_LOCK_CYCLES            | max_acquire_lock_cycles                | int     | Number of retries when acquiring a file lock before failing. Default is 20.                                | 20           |
| LockCycleDurationFactor          | STORAGE_USERS_DECOMPOSEDS3_LOCK_CYCLE_DURATION_FACTOR         | lock_cycle_duration_factor             | int     | Factor used to multiply lock cycle duration in milliseconds. Default is 30.                                | 30           |
| MaxConcurrency                   | OC_MAX_CONCURRENCY;STORAGE_USERS_DECOMPOSEDS3_MAX_CONCURRENCY | max_concurrency                     | int     | Maximum number of concurrent goroutines. Default is 100.                                                   | 100          |
| AsyncUploads                     | OC_ASYNC_UPLOADS                                              | async_uploads                          | bool    | Enable asynchronous file uploads.                                                                          |              |
| DisableVersioning                | OC_DISABLE_VERSIONING                                         | disable_versioning                     | bool    | Disables file versioning. When true, new uploads overwrite existing files instead of creating new versions. |              |






| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| DECOMPOSEDS3                    | String | Enables S3 storage.                                                | :decomposeds3.yml                                  |
| DECOMPOSEDS3_ENDPOINT           | String  | Configures the S3 storage endpoint.                                | http://minio:9000                                  |
| DECOMPOSEDS3_REGION             | String  | Sets the S3 region.                                                | default                                            |
| DECOMPOSEDS3_ACCESS_KEY         | String  | Specifies the S3 access key.                                       | opencloud                                          |
| DECOMPOSEDS3_SECRET_KEY         | String  | Defines the S3 secret key.                                         | opencloud-secret-key                               |
| DECOMPOSEDS3_BUCKET             | String  | Sets the S3 bucket.                                                | opencloud                                          |
| DECOMPOSEDS3_MINIO              | String | Adds local Minio S3 storage.                                       | :minio.yml                                         |
| MINIO_DOMAIN                    | String  | Sets the Minio domain.                                             | minio.opencloud.test                               |

### POSIX Storage configuration - optional
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| POSIX                           | String | Enables POSIX storage.                                             | :posix.yml                                         |

### SMTP settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| SMTP_HOST                       | String  | Specifies the SMTP host to connect to.                            | None                           |
| SMTP_PORT                       | Integer | Sets the port of the SMTP host.                                   | None                           |
| SMTP_SENDER                     | String  | Defines the email address used for sending OpenCloud notification emails. | None                  |
| SMTP_USERNAME                   | String  | Sets the username for the SMTP host.                              | None                           |
| SMTP_PASSWORD                   | String  | Defines the password for the SMTP host.                           | None                           |
| SMTP_AUTHENTICATION             | String  | Configures the authentication method for SMTP communication.      | None                           |
| SMTP_INSECURE                   | Boolean | Allows insecure connections to the SMTP server.                   | false                                              |

### Additional services
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| START_ADDITIONAL_SERVICES       | String  | Defines additional services to start on OpenCloud startup.       | notifications                                      |

### OpenCloud Web Extensions
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| EXTENSIONS                      | String | Enables the creation of a new named volume for web extensions.    | :web_extensions/extensions.yml                     |

### Collabora
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| COLLABORA                       | String | Enables Collabora web office.                                    | :collabora.yml                                     |
| COLLABORA_DOMAIN                | String  | Sets the domain for Collabora.                                   | collabora.opencloud.test                           |
| COLLABORA_SSL_ENABLE            | Boolean | Enables SSL for Collabora Online.                               | false                                              |
| COLLABORA_SSL_VERIFICATION      | Boolean | Enables SSL verification for Collabora Online.                  | false                                              |

### Monitoring
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| MONITORING                      | String | Enables monitoring.                                              | :monitoring_tracing/monitoring.yml                 |

### Virusscanner Settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| CLAMAV                          | String | Enables the ClamAV virus scanner.                               | :clamav.yml                                        |

### Inbucket Settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
|---------------------------------|---------|------------------------------------------------------------------------|------------------------------------------------------|
| INBUCKET                        | String | Enables Inbucket, a mail catcher tool.                          | :inbucket.yml                                      |
| INBUCKET_DOMAIN                 | String  | Sets the domain for Inbucket.                                    | mail.opencloud.test                                |
