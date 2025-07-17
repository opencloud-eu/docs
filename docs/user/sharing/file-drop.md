---
sidebar_position: 3
id: file-drop
title: File Drop
description: File Drop (secret)
draft: false
---

# File Drop (secret) - This is how it works

The **“File Drop”** allows people who receive a specific link (the so-called **“link recipients”**) to upload files to a shared folder.
**The trick:** The **“link recipients” cannot see the files already** in the folder.

## Create a **"File Drop"**

- Click on the **“three dot menu”** next to the file or folder name you want to share.
  <img src={require("./img/file-drop/three-dot-menu.png").default} alt="Three dot menu" width="1920"/>
- Select **“Share”** from the drop-down menu.
  <img src={require("./img/file-drop/share-drop-down-menu.png").default} alt="Drop down menu" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>
- A sidebar window will open on the right-hand side of the screen.
  <img src={require("./img/file-drop/sidebar-window.png").default} alt="Sidebar window" width="1920"/>
- At the sidebar window, you will find the area for **“Public links”**. There click on the **"Add link"** button.
  <img src={require("./img/file-drop/add-link-button.png").default} alt="Add link button" width="400"/>
- Select the option for **"Secret File Drop"**.
  <img src={require("./img/file-drop/file-drop-button.png").default} alt="Select file drop" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>
- Type a **password** and confirm the entries with click on **"copy link"**.
- You can also set an **"Expiry date"**, if you want the link to expire. [External Sharing](./external), if you want to know how to set the Expiry date.
  <img src={require("./img/file-drop/password-and-copy-link-button.png").default} alt="Enter password and copy link" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>
- Now you send the **link** and the **password** to a **"link recipient"**.

## To do's for the **"link recipient"**

- The **“link recipient”** opens the received link in a browser.
  <img src={require("./img/file-drop/file-drop-website.png").default} alt="File drop website" width="1920"/>
- The **“link recipient”** enters the password and then clicks on “Continue”.
  <img src={require("./img/file-drop/password-and-continue.png").default} alt="Enter password and continue" width="400"/>
- Upload files:<br/>
  - The “File drop folder” is opened. The “link recipient” can upload their files here without being able to view the existing contents of the folder.
    <img src={require("./img/file-drop/file-drop-area.png").default} alt="File drop area" width="1920"/>
  - As confirmation that the upload was successful, a pop-up window appears in the lower right corner.
    <img src={require("./img/file-drop/upload-confirmation.png").default} alt="Upload confirmation" width="1920"/>

:::important
The **“link recipient”** does not have access to existing files - **they can only add new files**.
:::

Now you know how you can share a file drop link
