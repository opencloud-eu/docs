---
sidebar_position: 5
id: logging
title: Collect Logfiles
---

# Logging to a Temporary Directory in OpenCloud Desktop

If you need to generate logs for troubleshooting, follow these steps:

## 1. Open the OpenCloud Desktop

## 2. Access Log Settings

Click on **Settings → Advanced → Log Settings**

<img src={require("./img/logging/logging-access.png").default} alt="logging access" width="400"/>

## 3. Enable Logging

- In the **Log Output** window, check the box for **Enable logging to temporary folder**
- To help the Support-Team and the developers, it is helpful to enable the **Log Http traffic**

<img src={require("./img/logging/logging-enable.png").default} alt="enable logging" width="400"/>

## 4. Find the Log Files

- Click **Open folder** to access the logs.

<img src={require("./img/logging/logging-open-folder.png").default} alt="open logfile folder" width="400"/>

- Select the log files for the time frame when the issue occurred.

<img src={require("./img/logging/logging-logfiles.png").default} alt="logfiles overview" width="400"/>

These logs can help diagnose and fix any issues with your OpenCloud Desktop Client.

### Log Content Description

`25-02-17 09:02:35:174 [ info sync.httplogger ]:	REQUEST 3710cc12-7391-4793-8e89-00499dc11983 {"request":{"body":{"length":0},"header":{"accept":"*/*","accept-language":"en_DE","original-request-id":"3710cc12-7391-4793-8e89-00499dc11983","user-agent":"Mozilla/5.0 (Macintosh) mirall/1.0.0-git (OpenCloud, macos-24.3.0 ClientArchitecture: x86_64 OsArchitecture: arm64)","x-request-id":"3710cc12-7391-4793-8e89-00499dc11983"},"info":{"cached":false,"id":"3710cc12-7391-4793-8e89-00499dc11983","method":"GET","url":"https://cloud.opencloud.test/.well-known/openid-configuration"}}}`

| Log Content                              | Description                                       |
| ---------------------------------------- | ------------------------------------------------- |
| **25-02-17 09:02:35:174**                | Timestamp of the request                          |
| **[ info sync.httplogger ]**             | Log category label                                |
| **3710cc12-7391-4793-8e89-00499dc11983** | X-REQUEST-ID (used to match requests & responses) |
| **Header: { }**                          | List of HTTP headers                              |
| **Data: []**                             | HTTP bodies (JSON, XML)                           |
| **(112ms)**                              | Response time (since the request was sent)        |

### Using X-REQUEST-ID for Debugging

- The OpenCloud desktop app sends an **X-REQUEST-ID** header with every request.
- This ID helps in finding corresponding requests and responses in logs.
- You can configure your web server to add the **X-REQUEST-ID** to its logs for deeper analysis.

This feature is useful for debugging sync issues, monitoring network activity, and troubleshooting connectivity problems.
