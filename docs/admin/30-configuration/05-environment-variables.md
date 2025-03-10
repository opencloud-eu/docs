---
sidebar_position: 1
id: env-variables
title: Environment Variables
draft: true
---

## Environment Variables Overview

This document provides a detailed overview of the environment variables used in OpenCloud. 
These variables allow for the configuration of various aspects of the system, including logging, storage, authentication, and additional services. 
Proper configuration ensures a secure and optimized setup tailored to your specific requirements.

### Basic Settings
| Variable                        | Type    | Description                                                            | Default Value                                        |
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
