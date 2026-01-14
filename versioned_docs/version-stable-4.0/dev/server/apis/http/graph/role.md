---
title: Role
sidebar_position: 60
---

## Role API

The Roles API is implementing a subset of the functionality of the
[MS Graph Role Management](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement?view=graph-rest-1.0).

## Role Management

### List roleDefinitions `GET /v1beta1/roleManagement/permissions/roleDefinitions`

[ListPermissionRoleDefinitions](https://docs.opencloud.eu/swagger/libre-graph-api/#/roleManagement/ListPermissionRoleDefinitions)

### Get unifiedRoleDefinition `GET /drives/{drive-id}/items/{item-id}/permissions/{perm-id}`

[GetPermissionRoleDefinition](https://docs.opencloud.eu/swagger/libre-graph-api/#/roleManagement/GetPermissionRoleDefinition)

## Role Assignment

### Get appRoleAssignments of a user `GET /v1.0/users/{user-id}/appRoleAssignments`

[ListAppRoleAssignments](https://docs.opencloud.eu/swagger/libre-graph-api/#/user.appRoleAssignment/user.ListAppRoleAssignments)

### Grant an appRoleAssignment to a user `POST /v1.0/users/{user-id}/appRoleAssignments`

[CreateAppRoleAssignments](https://docs.opencloud.eu/swagger/libre-graph-api/#/user.appRoleAssignment/user.CreateAppRoleAssignments)

### Delete the appRoleAssignment from a user `DELETE /v1.0/users/{user-id}/appRoleAssignments/{appRoleAssignment-id}`

[DeleteAppRoleAssignments](https://docs.opencloud.eu/swagger/libre-graph-api/#/user.appRoleAssignment/user.DeleteAppRoleAssignments)
