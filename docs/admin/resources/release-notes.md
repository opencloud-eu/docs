---
sidebar_position: 3
id: release-notes
title: "Release Notes"
draft: false
---

# 📦 Release Notes: Migration from v2.x.x to v3.0.0

- Version: 3.0.0
- Type: Major Release (Breaking Changes)
- [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.0.0)

## Key Changes
### Performance Optimization (Breaking Change)
#### Old Behavior:

```
GET /drives/{drive-id}/root/permissions
```

👉 Automatically returned full permission details with all nested properties.


#### New Behavior:

```
GET /drives/{drive-id}/root/permissions?$select=@libre.graph.permissions.actions.allowedValues
```

👉 Now requires explicit selection of needed fields. 
