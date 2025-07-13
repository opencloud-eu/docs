---
sidebar_position: 3
id: migrate
title: "Migrate"
description:: "Guide to migrating data using rclone."
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

## 🚀 Migrate Personal Space Data to OpenCloud Using rclone

This guide will help you migrate personal space data from `NextCloud` and `oCIS` to `OpenCloud` using `rclone`. Follow these steps carefully to ensure a smooth migration!

### 1. Generate users token using CLI or API

<Tabs>
<TabItem value="opencloud" label="OpenCloud">
    ### Run `OpenCloud` with following configuration:

    Modify `.env` file:
    ```sh
    START_ADDITIONAL_SERVICES="auth-app"
    ```

    Enable `auth-app` service:
    ```sh
    PROXY_ENABLE_APP_AUTH: "true"
    ```

    ### Generate user token using CLI:

    Enter the OpenCloud container:
    ```sh
    docker exec -it opencloud_full-opencloud-1 sh
    ```

    Generate an authentication token for a user (e.g, `Alan`) with expiration (`h, m, s`):
    ```sh
    opencloud auth-app create --user-name=alan --expiration=72h
    ```

    ---

    ### Generate user token using API:

    Requires additional configuration! Start the server with:
    ```sh
    AUTH_APP_ENABLE_IMPERSONATION=true
    ```

    Then generate a token via API:
    ```sh
    curl -vk -XPOST 'https://opencloud_url/auth-app/tokens?expiry=72h&userName=alan' -uadmin:admin
    ```

</TabItem>

<TabItem value="ocis" label="oCIS">
    ### Run `oCIS` with following configuration:

    Modify `.env` file:
    ```sh
    START_ADDITIONAL_SERVICES="auth-app"
    ```

    Enable `auth-app` service:
    ```sh
    PROXY_ENABLE_APP_AUTH: "true"
    ```

    ### Generate user token using CLI:

    Enter the oCIS container:
    ```sh
    docker exec -it ocis_full-ocis-1 sh
    ```

    Generate an authentication token for a user (e.g, `Einstein`) with expiration (`h, m, s`):
    ```sh
    ocis auth-app create --user-name=einstein --expiration=72h
    ```

    ---

    ### Generate user token using API:

    Requires Additional Configuration. Need to run server with additional configuration
    ```sh
    AUTH_APP_ENABLE_IMPERSONATION=true
    ```

    Then generate a token via API:
    ```sh
    curl -vk -XPOST 'https://ocis_url/auth-app/tokens?expiry=72h&userName=einstein' -uadmin:admin
    ```

</TabItem>
<TabItem value="nc" label="Nextcloud">
    ### 
    Go to `Settings` → `Security`

    Create a new `App Password`

    🖼 Example:
    <img src={require("./img/generate-pass-nc.png").default} alt="init -diff" width="1920"/>

</TabItem>
</Tabs>
    
---

### 2. Install rclone

Download and install rclone by following the official guide: 🔗[**rclone.org/install**](https://rclone.org/install/)

---

### 3. Encrypt Authentication Tokens 🔒

```sh
rclone obscure <token>
```

---

### 4. Create the rclone Configuration 🛠️

Edit the rclone configuration file:

```sh
nano ~/.config/rclone/rclone.conf
```

📌 Example Configuration:

```sh
[opencloud-admin]
type = webdav
url = https://opencloud_url/remote.php/webdav
vendor = opencloud
owncloud_exclude_shares = true
user = admin
pass = sQOM4mn2DdR9ihRGkyAMcd50W6mniaSqSfx2qVOdBJs
description = opencloud-admin

[opencloud-alan]
type = webdav
url = https://opencloud_url/remote.php/webdav
vendor = opencloud
owncloud_exclude_shares = true
user = alan
pass = sQOM4mn2DdR9ihRGkyAMcd50W6mniaSqSfx2qVOdBJs
description = opencloud-alan

[ocis-admin]
type = webdav
url = https://ocis_url/remote.php/webdav
vendor = ocis
owncloud_exclude_shares = true
user = admin
pass = Sav5354nRTgBHyItQeCZp9tCBidX2BxbuMx_dDLwxqs
description = ocis-admin

[ocis-einstein]
type = webdav
url = https://ocis_url/remote.php/webdav
vendor = ocis-einstein
owncloud_exclude_shares = true
user = einstein
pass = dcYsf3PNvBxaIi7MMq-bqg74KMWWWS8p3uFT-WD17SA
description = ocis-einstein

[nc-admin]
type = webdav
url = http://nc_url/remote.php/webdav
vendor = nc
owncloud_exclude_shares = true
user = admin
pass = IBSkhC1wCDdS2Gt9iBV-C9IqlGek
description = nc-admin

[nc-bob]
type = webdav
url = http://localhost:8080/remote.php/webdav
vendor = nc-bob
owncloud_exclude_shares = true
user = bob
pass = ufOK3zPDjR4meEwwy3cWUVA18Lf8TpubBRyPL5m9KC508PkMiEVAXTxg6olu
description = nc-bob

```

---

### 5. Copy Data to OpenCloud

Use `rclone copy` to transfer data from `oCIS` and `Nextcloud` to `OpenCloud`:

```sh
rclone copy ocis-admin:/ opencloud-admin:/ --no-check-certificate -P  # Copy oCIS admin personal space to OpenCloud admin space
rclone copy ocis-einstein:/ opencloud-alan:/ --no-check-certificate -P  # Copy oCIS bob's personal space to OpenCloud admin space
rclone copy nc-bob:/ opencloud-alan:/ --no-check-certificate -P  # Copy Nextcloud admin personal space to OpenCloud admin space

```

---

### 6. Migration Results and Limitations

🎉 Congratulations! You have successfully migrated personal space data to OpenCloud! 🚀

✅ Successfully Migrated:

- Personal space files

❌ Not Migrated:

- Shared files
- Public links
- Project spaces
- Trash-bin contents
- File versions
- Metadata

### 7. Security Step: Delete Tokens

Once the migration is complete, please delete tokens to prevent unauthorized access!
