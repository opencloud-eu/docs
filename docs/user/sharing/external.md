---
sidebar_position: 2
id: external
title: External
description: External sharing of files and folder in OpenCloud
draft: false
---

# Public links - external sharing of files and folders in OpenCloud

With public links, you can share files and/or folders across organizations.

## Steps to create public link

- Click on the “three dot menu” next to the file or folder name you want to share.
  <img src={require("./img/extern/three-dot-menu.png").default} alt="Three dot menu" width="1920"/>

- Select “Share” from the drop-down menu.
  <img src={require("./img/extern/share-drop-down-menu.png").default} alt="Select share" width="400"/>

- A sidebar window will open on the right side of the screen.
  <img src={require("./img/extern/sidebar-window.png").default} alt="Sidebar window" width="1920"/>

- Scroll down in the sidebar window and click on “Add link”.
  <img src={require("./img/extern/public-link-section.png").default} alt="Click on add link" width="400"/>  
  <img src={require("./img/extern/add-link-button.png").default} alt="Add link button" width="400"/>

- A pop-up window will open where you can configure the following options:
  <img src={require("./img/extern/public-link-option-pop-up.png").default} alt="Pop up window" width="400"/>
  <img src={require("./img/extern/public-link-option-button.png").default} alt="Options" width="400"/>

## Options in the pop-up window

- Select the desired access rights for the recipients:
  - “Can view":
    The link recipient can view and download the file, but cannot edit or upload files.
  - “Can edit":
    The link recipient can view, download, edit and delete the file, as well as upload files to the folder.
  - “File Drop (secret)":
    The link recipient can only upload files, but cannot view or edit the content.

    <img src={require("./img/extern/access-rights.png").default} alt="Access rights" width="400"/>

- Activate the password by entering it in the input field under “Password”.
- The password requirements appear below the input field.
  <img src={require("./img/extern/password-section.png").default} alt="Password section" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>
- Here are three icons:
  - One icon displays the password unencrypted to verify your entry.
    <img src={require("./img/extern/password-icon-1.png").default} alt="Unencrypt password" width="400"/>
  - The next icon copies the password to the clipboard.
    <img src={require("./img/extern/password-icon-2.png").default} alt="Copy password" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>
  - The last icon generates a random password automatically.
    <img src={require("./img/extern/password-icon-3.png").default} alt="Generate random password" width="400"/>

- Enter a date under “Expiry date” to set a time limit for the link. Once the date has expired, the link is no longer accessible.

  <img src={require("./img/extern/expiration-date.png").default} alt="Expiration date" width="400"/>

- If you do not enter a date, the link will not expire.

## Create link

- Once all options have been set, click on “Copy link” to generate the public link.
  <img src={require("./img/extern/copy-link-button.png").default} alt="Copy link" width="400"/>
- The link is now created and can be shared with the recipients.

Now you know how you can share files and folders securely and individually with external users.
