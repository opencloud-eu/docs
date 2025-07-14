---
sidebar_position: 1
id: update
title: 'Upgrade'
description: '🔄 Keep your setup up to date with the latest features!'
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

This guide provides steps to upgrade OpenCloud for both [docker](docs/admin/getting-started/container/docker.md) and [docker compose](docs/admin/getting-started/container/docker-compose/docker-compose.md)

### 1. Stop OpenCloud

Stop the currently running OpenCloud instance:

<Tabs groupId="deployment">
  <TabItem value="docker" label="docker">
    ```Shell
    docker stop opencloud
    ```
  </TabItem>
  <TabItem value="docker-compose" label="docker compose">
    ```Shell
    docker compose stop
    ```
  </TabItem>
</Tabs>

---

### 2. Backup Config and Data

It is recommended to create a [backup](../backup.md) before proceeding with the upgrade.

---

### 3. Pull the new Opencloud version

```Shell
docker pull opencloudeu/opencloud:{tag}
```

---

### 4. Verify Configuration Changes

If upgrading from an older release, check for required configuration changes:

Go inside the container:

```Shell
docker run --rm -it --entrypoint /bin/sh -v $HOME/opencloud/opencloud-config:/etc/opencloud opencloudeu/opencloud:{tag}
```

```Shell
opencloud init --diff
```

If you see `no changes, your config is up to date`, no further action is needed. Otherwise, update your `opencloud.yaml` file accordingly and start OpenCloud.

<img src={require("../img/init-diff.png").default} alt="init -diff" width="1920"/>

---

### 5. Start OpenCloud with updated image

<Tabs groupId="deployment">
  <TabItem value="docker" label="docker">
    ```Shell
    docker run \
    --name opencloud \
    --rm \
    -it \
    -p 9200:9200 \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e OC_INSECURE=true \
    -e PROXY_HTTP_ADDR=0.0.0.0:9200 \
    -e OC_URL=https://localhost:9200 \
    opencloudeu/opencloud:{tag}
    ```
  </TabItem>
  <TabItem value="docker-compose" label="docker compose">
    ```Shell
    OC_DOCKER_IMAGE=opencloudeu/opencloud OC_DOCKER_TAG=tag docker compose up -d
    ```
  </TabItem>
</Tabs>

---

### 6. Conclusion

Make sure that all previously created data, users, shared files, public links exist.
