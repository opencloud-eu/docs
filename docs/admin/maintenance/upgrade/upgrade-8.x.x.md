---
sidebar_position: 15
id: upgrade-8.x.x
title: Upgrade 8.x.x
description: Upgrading to OpenCloud 8.x.x
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Upgrading to OpenCloud 8.x.x

OpenCloud 8.x.x changes how resources are indexed and creates a new search index. Complete the regular upgrade first by following the [Standard Upgrade Guide](./upgrade.md).

:::important

OpenCloud 8.x.x is a Rolling release and is not intended for production environments. For more information, see the [Release Lifecycle](../../resources/lifecycle.md).

:::

## External proxy

Should you be using Nginx as an external proxy, then you need to upgrade your [Nginx configuration](../../getting-started/container/docker-compose/docker-external-proxy.md). You need to add an extra `location` block to the configuration of your main *OpenCloud* server:

```
    # WebSocket route for the yjs server (collaborative editing).
    # Only needed if yjs/yjs.yml is part of COMPOSE_FILE.
    location ^~ /yjs {
        proxy_pass http://127.0.0.1:9200;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
```

## Quick upgrade

After OpenCloud has been upgraded, rebuild the search index using the commands for your search backend. This creates a new, versioned index (e.g. `bleve-v5` / `opencloud-resources-v5`) and leaves the old one in place until you remove it.

<Tabs groupId="search-backend">
  <TabItem value="bleve" label="Bleve (default)" default>

```bash
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure
```

Verify that older files can be found in the Web Client. Then remove the old, unversioned Bleve index:

```bash
docker compose exec opencloud rm -r /var/lib/opencloud/search/bleve
```

This command removes only the old `bleve` index.

If you configured a custom `SEARCH_ENGINE_BLEVE_DATA_PATH`, replace `/var/lib/opencloud/search` with the configured path.

  </TabItem>
  <TabItem value="opensearch" label="OpenSearch">

```bash
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure
```

Verify that older files can be found in the Web Client. Then list the existing indexes and remove the old one:

```bash
curl "http://localhost:9200/_cat/indices/opencloud-resources*?v"
curl -X DELETE "http://localhost:9200/opencloud-resources"
```

This command removes only the old `opencloud-resources` index.

  </TabItem>
</Tabs>

## What this does

- The new, empty index (e.g. `bleve-v5` / `opencloud-resources-v5`) is created automatically. The old one stays until you remove it.
- New activity is indexed right away, but files that existed before and are not touched are not found until you re-index.
- Re-indexing runs while the service keeps working.
- After it finishes, delete every index except the one with the highest version suffix (indexes up to 7.4 have no suffix). Verify search first.

:::note

`--insecure` is needed because the internal gRPC transport is not TLS-encrypted by default (`OC_GRPC_CLIENT_TLS_MODE` defaults to `off`). Drop it only if you run gRPC with TLS. This is safe here — the command just triggers a rescan; the re-indexing happens inside the OpenCloud process.

:::
