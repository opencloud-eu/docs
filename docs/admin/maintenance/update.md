---
sidebar_position: 6
id: update
title: Update OpenCloud
description: Tutorial about updating the OpenCloud.
draft: false
---

# Update OpenCloud

This guide describes how to update OpenCloud to the stable version
**v2.0.5** using the Git repository and how to set up **opencloud_full**
with externalized data and config directories.



## 1. Clone the OpenCloud Repository

Clone the official OpenCloud repository onto your server:

``` bash
git clone https://github.com/opencloudeu/opencloud.git
cd opencloud
```

Checkout the latest stable release:

``` bash
git checkout "latest OpenCloud Version"
```



## 2. Stop the Current OpenCloud Instance

Stop OpenCloud if it is running.

### docker

``` bash
docker stop opencloud
```

### docker compose

``` bash
docker compose down
```



## 3. Backup Config and Data

Create backups before upgrading:

``` bash
cp -r /mnt/opencloud/config /mnt/opencloud/config-backup
cp -r /mnt/opencloud/data /mnt/opencloud/data-backup
```



## 4. Prepare opencloud_full (Version 2.0.5)

Set up **opencloud_full** using version **2.0.5** and mounted
config/data directories.

### Create directories

``` bash
sudo mkdir -p /mnt/opencloud/config
sudo mkdir -p /mnt/opencloud/data
```

Copy old data if necessary:

``` bash
sudo cp -r opencloud-config/* /mnt/opencloud/config/
sudo cp -r opencloud-data/* /mnt/opencloud/data/
```



## 5. Configure opencloud_full

Navigate to the full deployment:

``` bash
cd deployments/opencloud_full
```

Ensure your compose file uses version:

``` yaml
image: opencloudeu/opencloud:v2.0.5
```

Use external volumes:

``` yaml
volumes:
  - /mnt/opencloud/config:/etc/opencloud
  - /mnt/opencloud/data:/var/lib/opencloud
```



## 6. Start OpenCloud (v2.0.5)

### docker

``` bash
docker run   --name opencloud   -p 9200:9200   -v /mnt/opencloud/config:/etc/opencloud   -v /mnt/opencloud/data:/var/lib/opencloud   -e OC_INSECURE=true   -e PROXY_HTTP_ADDR=0.0.0.0:9200   -e OC_URL=https://localhost:9200   opencloudeu/opencloud:v2.0.5
```

### docker compose

``` bash
docker compose up -d
```



## 7. Verify Configuration

Check for configuration changes:

``` bash
opencloud init --diff
```

Update `opencloud.yaml` if required.



## Conclusion

Your OpenCloud instance should now be running on **v2.0.5** using
externalized config and data directories. Verify:

-   Users\
-   Shared folders\
-   Public links\
-   All data availability
