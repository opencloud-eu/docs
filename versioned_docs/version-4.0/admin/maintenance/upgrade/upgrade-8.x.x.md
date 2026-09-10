---
sidebar_position: 15
id: upgrade-8.x.x
title: Upgrade 8.x.x
description: Upgrading to OpenCloud 8.x.x
draft: false
---

# Upgrading to OpenCloud 8.x.x

This guide describes how to upgrade an existing OpenCloud deployment to OpenCloud 8.x.x.

It covers the search index migration introduced with OpenCloud 8.x.x. For the general upgrade steps (backup, stopping OpenCloud, pulling the new image, applying configuration changes and starting again), follow the [Standard Upgrade Guide](./upgrade.md).

## Migrating the Search Index

A version that changes how resources are indexed builds a **new index** and leaves the old one untouched. The service starts normally.

**What to expect after updating to 8.0.0:**

- You get a **new, empty** index (e.g. `search/bleve-v4`); the old one stays around until you remove it.
- The new index **starts filling on its own** from live activity: any file you upload, move or change from now on is indexed right away, so search finds those.
- Files that existed before and are not touched are **not found** yet.
- To make everything searchable again, run a full re-index (see below).

:::note

The `search index` command reaches the search service over its internal gRPC endpoint. That transport is not TLS-encrypted by default (`OC_GRPC_CLIENT_TLS_MODE` defaults to `off`), so `--insecure` is needed; drop it only if you run gRPC with TLS. This is safe here — the command just triggers a rescan, the re-indexing runs inside the OpenCloud process.

:::

## v7.x.x → 8.x.x

### bleve (default)

The new index is a directory next to the old one, both under `$OC_BASE_DATA_PATH/search` by default (`SEARCH_ENGINE_BLEVE_DATA_PATH`). A bleve index cannot be copied — re-index all spaces:

```bash
opencloud search index --all-spaces --force-rescan --insecure
```

:::note

Before deleting, check that search works (search for older, untouched files).

:::

Once it is filled and verified, every directory except the one with the highest `bleve-v<N>` suffix can go (indexes up to 7.4 have no suffix):

```bash
rm -r "$OC_BASE_DATA_PATH/search/bleve"
```

### OpenSearch

Re-index all spaces (the service keeps running while it happens). Run this in the **OpenCloud** container:

```bash
opencloud search index --all-spaces --force-rescan --insecure
```

:::note

Before deleting, check that search works (search for older, untouched files).

:::

Once it is filled and verified, every index except the one with the highest `-v<N>` suffix can go (indexes up to 7.4 have no suffix). Run the following `curl` commands in the **OpenSearch** container (or from any host that can reach the OpenSearch API).

List the indexes:

```bash
curl "http://localhost:9200/_cat/indices/opencloud-resources*?v"
```

```text
health status index                  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   opencloud-resources-v4 h3DtDe7VQUGzoNPKh0yt6Q   1   1       1142          104    160.1mb        160.1mb
yellow open   opencloud-resources    DRDfEtFqS9ufYHaz-YU-3A   1   1       1142           51    145.2mb        145.2mb
```

Here `opencloud-resources-v4` is the newest, so delete the old `opencloud-resources`:

```bash
curl -X DELETE "http://localhost:9200/opencloud-resources"
```

Adjust the host and index names to match your deployment.

## Running It in Docker Compose

```bash
docker compose exec opencloud opencloud search index --all-spaces --insecure
```
