---
sidebar_position: 8
id: multiple-accounts
title: Set up multiple accounts
description: Using multiple Accounts in OpenCloud Desktop
draft: false
---

# Using Multiple Accounts in OpenCloud Desktop

You can synchronize multiple accounts from different OpenCloud servers to your local machine. This allows you to manage files from different instances within the same desktop client.

## How to Add a New Account

- Open **OpenCloud Desktop**
- Click on **Add Account**

  <img src={require("./img/multiple-accounts/multiple-accounts-add-account.png").default} alt="add accounts" width="400"/>

- Follow the [standard setup process](./set-up):
  - Enter the server URL
  - Log in with your credentials
  - Authorize access

## Switching Between Accounts

- After adding multiple accounts, they will appear in the **account overview** in the settings menu
- You can easily switch between them to manage synchronization settings for each account separately

  <img src={require("./img/multiple-accounts/multiple-accounts-switch-accounts.png").default} alt="switch accounts" width="400"/>

## How Files are Stored Locally

- In your **File Explorer**, each account will have a separate folder
- By default, the folders are named:
  - **OpenCloud** (for the first account)
  - **OpenCloud (2)** (for the second account)
  - **OpenCloud (3)** (for the third account), and so on

    <img src={require("./img/multiple-accounts/multiple-accounts-locally.png").default} alt="multiple accounts in explorer or finder" width="400"/>

This setup ensures that files from different accounts remain **organized and do not mix**.
