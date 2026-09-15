---
sidebar_position: 15
id: upgrade-8.x.x
title: Upgrade 8.x.x
description: Upgrading to OpenCloud 8.x.x
draft: false
---

# Upgrading to OpenCloud 8.x.x

OpenCloud 8.x.x changes how resources are indexed and builds a **new search index**. For the general upgrade steps (backup, image pull, config, restart), follow the [Standard Upgrade Guide](./upgrade.md).

## Commands

### bleve (default)

```bash
# 1. Re-index all spaces (OpenCloud container)
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure

# 2. Verify search works in the web UI (search for an older file), then remove the old index
docker compose exec opencloud sh -c 'rm -r "$OC_BASE_DATA_PATH/search/bleve"'
```

### OpenSearch

```bash
# 1. Re-index all spaces (OpenCloud container)
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure

# 2. Verify search works in the web UI (search for an older file), then list and delete the old index (OpenSearch container)
curl "http://localhost:9200/_cat/indices/opencloud-resources*?v"
curl -X DELETE "http://localhost:9200/opencloud-resources"
```

## What this does

- The new, empty index (e.g. `bleve-v4` / `opencloud-resources-v4`) is created automatically. The old one stays until you remove it.
- New activity is indexed right away, but files that existed before and are not touched are not found until you re-index.
- Re-indexing runs while the service keeps working.
- After it finishes, delete every index except the one with the highest `-v<N>` suffix (indexes up to 7.4 have no suffix). Verify search first.

:::note

`--insecure` is needed because the internal gRPC transport is not TLS-encrypted by default (`OC_GRPC_CLIENT_TLS_MODE` defaults to `off`). Drop it only if you run gRPC with TLS. This is safe here — the command just triggers a rescan; the re-indexing happens inside the OpenCloud process.

:::
