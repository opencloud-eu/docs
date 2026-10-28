---
sidebar_position: 1
id: guest-feature
title: Guest Feature
description: Invite external guests by email address, manage their permissions, and access shared content as a guest.
draft: true
---

# Guest Feature in OpenCloud

The **Guest Feature** lets you collaborate with external people who do not have an OpenCloud account.

You invite a guest with their email address and grant access to a specific file or folder. The guest receives an invitation email, opens the link in a web browser, and can access only the content you shared with them.

:::note
The Guest Feature must be enabled by your administrator. If you cannot invite guests, contact your administrator.
:::

## How the Guest Feature Works

1. You select a file or folder and open the sharing panel.
2. You enter the external email address and choose a permission level.
3. OpenCloud sends an invitation email with a link to the guest.
4. The guest opens the link in a web browser.
5. The guest accesses the shared content with the permissions you assigned.
6. You can change or remove the guest's access at any time.

A guest invitation applies only to the shared file or folder. It does not grant access to any other content in OpenCloud.

## Invite a Guest

- Log in to OpenCloud.
- Select the file or folder you want to share.
- Open the **Share** panel in the right sidebar.
- Enter the guest's email address in the **Share with people** field.
- Select the entry marked **(Guest)**.

<img src={require("./img/guest-feature/invite-guest.png").default} alt="Invite a guest using an email address" width="900"/>

- Choose the permission level, see [Set Guest Permissions](#set-guest-permissions).
- Click **Share**.

OpenCloud sends an invitation email to the guest's address.

:::note
If an email address belongs to an existing OpenCloud user, OpenCloud suggests that user instead of a guest.
:::

## Set Guest Permissions

Guest permissions determine what the guest can do with the shared content.

| Permission            | Description                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Can view**          | The guest can view and download the shared content.                                                                         |
| **Can view (secure)** | The guest can only view documents, images, and PDFs in the browser. Downloading is not possible and watermarks are applied. |
| **Can upload**        | The guest can view and download the shared content and upload new files.                                                    |
| **Can edit**          | The guest can view, download, upload, edit, add, and delete content.                                                        |

The available permission levels depend on the type of the shared resource. For example, **Can upload** is available for folders only.

To choose a permission level, open the permission selector below the email address field before you click **Share**.

<img src={require("./img/guest-feature/guest-permissions.png").default} alt="Select permissions for an external guest" width="900"/>

:::tip
Grant only the permissions required for the collaboration. Use **Can view** when the guest does not need to make changes, and **Can view (secure)** when the guest must not download the content.
:::

## Open a Guest Invitation

This section describes the steps for the invited guest.

- Open the invitation email sent by OpenCloud.
- Click the link in the email.
- The link opens OpenCloud in your web browser.
- OpenCloud verifies the invitation automatically. You do not need to sign in.
- The shared file or folder is displayed.

:::important
The invitation link is personal. Do not forward it to other people.
:::

### Invitation Link and Guest Session

- **Invitation link:** The link in the invitation email can be used **only once** and is valid for a **limited time**. Open it soon after you receive the email.
- **Guest session:** After you open the link, you can work with the shared content in this browser for a limited time, by default **24 hours**.

If you open an invitation link that has already been used in the same browser while your guest session is still valid, you can continue working.

When your guest session has expired or the link is no longer valid, ask the person who shared the content with you to invite you again.

## Access Shared Content as a Guest

As a guest, you work in the OpenCloud web interface. You can access only the file or folder that was shared with you.

Depending on the permissions you have been granted, you can:

- Open and view shared files.
- Browse shared folders.
- Download files.
- Upload files.
- Edit, add, and delete content.

<img src={require("./img/guest-feature/guest-access.png").default} alt="Guest accessing a shared resource" width="1000"/>

:::note
Guest access is available in the web browser only. Guests cannot use the OpenCloud Desktop Client or the mobile apps.
:::

## Manage Existing Guest Access

You can review and change guest access at any time.

- Select the shared file or folder.
- Open the **Share** panel in the right sidebar.
- Find the guest in the **Shared with** list.
- To change the permission level, use the permission selector below the guest's email address.
- Open the action menu (**⋮**) next to the guest for further options:
  - **Access details** – Shows details about the guest's access.
  - **Set expiration date** – Defines a date after which the guest's access ends automatically.
  - **Remove share** – Revokes the guest's access.

<img src={require("./img/guest-feature/manage-guest.png").default} alt="Manage guest access and permissions" width="900"/>

### Remove Guest Access

- Select the shared file or folder.
- Open the **Share** panel in the right sidebar.
- Open the action menu (**⋮**) next to the guest.
- Select **Remove share**.

<img src={require("./img/guest-feature/remove-guest.png").default} alt="Remove an external guest from a shared resource" width="900"/>

After you remove the share, the guest can no longer access the content, even if they still have the invitation link or an active guest session.

:::important
Removing access does not delete copies of files that the guest has already downloaded.
:::

## Guest Feature Compared with Other Ways of Sharing

| Sharing method       | Use case                                               | Access                                                                                       |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| **Guest Feature**    | Share with a specific external person by email address | Personal invitation link, access limited to the shared content and to a limited session time |
| **Public link**      | Share content with anyone who has the link             | Anyone with the link, optionally protected by a password and expiration date                 |
| **Internal sharing** | Share with other users of your OpenCloud               | Users sign in with their own OpenCloud account                                               |

## Recommendations

- Check the guest's email address before you send the invitation.
- Choose the lowest permission level that is sufficient for the collaboration.
- Set an expiration date for guest access.
- Review your guest shares regularly.
- Remove guest access when the collaboration has ended.

## Troubleshooting

### The Guest Option Is Not Displayed

- Make sure you entered the complete email address.
- Check that you are allowed to share the selected file or folder.
- Ask your administrator whether the Guest Feature is enabled.

### The Guest Did Not Receive an Email

- Check the spelling of the email address.
- Ask the guest to check their spam folder.
- Remove the guest share and invite the guest again.
- If the problem persists, contact your administrator.

### The Invitation Link Does Not Work

- Make sure the complete link from the email was opened.
- The link may have been used already or may have expired. Ask the person who shared the content to invite you again.

### The Guest Cannot Edit a File

- Check that the guest has the **Can edit** permission.
- Check that the file type can be edited in OpenCloud.

## Good to Know

- Guests are invited by email address and do not need an OpenCloud account.
- A guest can access only the content that was shared with them.
- The permission level determines what a guest can do.
- Invitation links can be used only once and are valid for a limited time.
- Guest sessions are limited in time.
- Guest access works in the web browser only.
- You can change or remove guest access at any time.
