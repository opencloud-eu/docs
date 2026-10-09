---
sidebar_position: 40
id: opencloud-mesh
title: OpenCloud Mesh
description: Connect with users on another OpenCloud instance and share files or folders with them.
draft: false
---

# Connect and share through OpenCloud Mesh

OpenCloud Mesh, abbreviated as OCM, lets you connect with users on another OpenCloud instance and share files or folders with them.

Before you begin, an administrator must configure OCM on both participating instances. For configuration instructions, see [Configure OpenCloud Mesh](../../admin/configuration/ocm.md).

## Open the ScienceMesh application

1. Sign in to OpenCloud Web.
2. Open the application switcher.
3. Select the ScienceMesh application.

The ScienceMesh application provides the interface for creating and accepting OCM invitations.

<img src={require("./img/opencloud-mesh/open-ocm-application.png").default} alt="Application switcher with the ScienceMesh application" width="1920" />

## Connect with a user

Before you can share resources with a user on another instance, you must establish an OCM connection.

:::important

Create the invitation on one OpenCloud instance and accept it on the other OpenCloud instance.

Do not accept an invitation on the same instance where it was created.

:::

### Create an invitation on your instance

1. In the Invite users section, select Generate invitation.

   <img src={require("./img/opencloud-mesh/generate-invitation.png").default} alt="Invite users section with the Generate invitation button" width="1640" />

2. In the Generate new invitation dialog, optionally enter a description that helps you identify the invitation later.
3. Select Generate.

   <img src={require("./img/opencloud-mesh/generate-invitation-dialog.png").default} alt="Generate new invitation dialog with a description" width="1008" />

4. The invitation token is generated and copied to your clipboard automatically.
5. Send the complete copied token to the user on the other instance.

If you need to copy the token again, find the invitation in the Invite users section and use the Copy base64 token action.

<img src={require("./img/opencloud-mesh/copy-invitation-token.png").default} alt="Generated invitation and controls for copying the invitation token" width="1640" />

### Accept the invitation on the other instance

The invited user completes the following steps on their OpenCloud instance:

1. Sign in to OpenCloud Web.
2. Open the ScienceMesh application.

   <img src={require("./img/opencloud-mesh/open-accept-invitations.png").default} alt="Accept invitations section in the ScienceMesh application" width="1608" />

3. In the Accept invitations section, paste the complete token into Enter invite token.
4. Check that Institution displays the domain of the inviting OpenCloud instance.
5. Select Accept invitation.

   <img src={require("./img/opencloud-mesh/accept-invitation.png").default} alt="Invitation token with the detected institution and the Accept invitation button" width="1608" />

After the invitation has been accepted, the remote user becomes available as an OCM connection.

<img src={require("./img/opencloud-mesh/federated-connection.png").default} alt="New federated connection in the ScienceMesh application" width="1920" />

:::note

Send the complete token that was copied automatically or use the Copy base64 token action. Do not manually copy the shortened token text displayed in the invitation table.

By default, invitation tokens expire after 24 hours. If an invitation has expired, create a new invitation.

:::

## Share a file or folder

After both users are connected:

1. Open the Files application.
2. Select a file or folder.
3. Open the sharing panel.
4. From Share type, select External.

   <img src={require("./img/opencloud-mesh/select-external-share-type.png").default} alt="Share type menu with External users selected" width="452" />

5. Enter all or part of the connected remote user's name in the search field.
6. Select the matching user marked as External.

   <img src={require("./img/opencloud-mesh/find-external-user.png").default} alt="Search results with an external federated user" width="452" />

7. Configure the permissions.
8. Select Share.

   <img src={require("./img/opencloud-mesh/share-with-external-user.png").default} alt="External user selected with permissions and the Share button" width="452" />

The remote user should now receive the shared resource on the other OpenCloud instance.

### Open the shared resource on the other instance

The invited user completes the following steps on their OpenCloud instance:

1. Open the Files application.
2. Select Shares in the left sidebar.
3. Open Shared with me.
4. Verify that the shared file or folder is listed.

<img src={require("./img/opencloud-mesh/received-federated-share.png").default} alt="Federated folder under Shared with me on the receiving OpenCloud instance" width="1920" />

## Troubleshooting

### The ScienceMesh application is not visible

Sign out of OpenCloud Web and reload the page without using the browser cache, or open a private browser window. Sign in again and check the application switcher.

If the ScienceMesh application is still unavailable, contact your administrator.

### A user is not shown in the sharing dialog

Make sure that Share type is set to External and that both users completed the invitation process successfully. Remote users only appear as sharing recipients after the OCM connection has been established.

If the connection exists but the user is not shown, contact your administrator.

### An invitation cannot be accepted

Check that:

- The invitation has not expired.
- You are signed in to the receiving OpenCloud instance.
- You are accepting the invitation on the other instance, not on the instance where it was created.
- The full invitation link or token was copied.

If the invitation has expired, ask the inviting user to create a new one. If it still cannot be accepted, contact your administrator.
