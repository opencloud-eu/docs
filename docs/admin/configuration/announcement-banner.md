---
sidebar_position: 130
id: announcement-banner
title: Announcement Banner
description: Notify users in OpenCloud with a global announcement banner.
draft: false
---

# Announcement Banner

OpenCloud 7.4.0 includes an announcement banner feature.

Administrators can use the announcement banner to notify all users about important information, for example upcoming maintenance windows, service interruptions, or other system-wide announcements.

The banner is displayed at the top of the OpenCloud web interface.

## Open Admin Settings

To configure the announcement banner, open the **Admin Settings** app.

1. Click the app switcher icon in the top-right corner.
2. Select **Admin Settings**.

<img src={require("./img/announcement-banner/admin-settings-button.png").default} alt="Admin Settings button" width="1920"/>

## Configure the announcement banner

In **Admin Settings**, open the **General** section.

In the **Announcement banner** area, you can configure the banner that will be shown to users.

1. Enable **Show banner**.
2. Enter a short title in the **Banner** field.
3. Optionally, enter additional message text in the **Banner details** field if you want to provide more information.
4. Click **Save**.

<img src={require("./img/announcement-banner/announcement-banner-option.png").default} alt="Announcement banner settings" width="1920"/>

:::important

The announcement banner is visible to users. Do not include sensitive information such as passwords, access tokens, private URLs, or confidential internal details.

:::

## Preview the banner

Before saving the announcement, you can click **Preview** to check how the message will be displayed to users.

<img src={require("./img/announcement-banner/announcement-banner-save.png").default} alt="Preview and save announcement banner" width="1920"/>

## User view

After saving the configuration, the announcement banner is displayed at the top of the OpenCloud web interface.

<img src={require("./img/announcement-banner/announcement-banner-on-top.png").default} alt="Announcement banner displayed at the top" width="1920"/>

Users can open the banner to view the full announcement text in a pop-up dialog.

<img src={require("./img/announcement-banner/announcement-banner-pop-up.png").default} alt="Announcement banner pop-up" width="1920"/>

## Disable the announcement banner

To hide the announcement banner again:

1. Open **Admin Settings**.
2. Go to **General**.
3. Disable **Show banner**.
4. Click **Save**.

The banner is then removed from the OpenCloud web interface.

:::note

The announcement banner is useful for temporary information that should be visible to all users, such as planned maintenance or short-term service notices.

:::
