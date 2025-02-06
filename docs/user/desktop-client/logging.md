---
sidebar_position: 5
id: logging
title: Collect Logfiles
---

# Logging to a Temporary Directory in OpenCloud Desktop Client

If you need to generate logs for troubleshooting, follow these steps:

## 1. Open the OpenCloud Desktop App

## 2. Access Log Settings

Click on **Settings → Advanced → Log Settings**  
 
<img src={require("./img/logging/logging-access.png").default}  width="400"/>

## 3. Enable Logging

- In the **Log Output** window, check the box for **Enable logging to temporary folder**  
- To help the Support-Team and the developers, it is helpful to enable the **Log Http traffic**

<img src={require("./img/logging/logging-enable.png").default}  width="400"/>

## 4. Find the Log Files
- Click **Open folder** to access the logs.  

<img src={require("./img/logging/logging-open-folder.png").default}  width="400"/>

- Select the log files for the time frame when the issue occurred.  

<img src={require("./img/logging/logging-logfiles.png").default}  width="400"/>

These logs can help diagnose and fix any issues with your OpenCloud Desktop Client.


### Log Content Description


```25-02-06 15:20:47:217 [ info sync.httplogger ]:	REQUEST 0a1f7f31-5f01-4348-83ab-17a6fca64597 {"request":{"body":{"length":0},"header":{"accept":"*/*","accept-language":"en_DE","original-request-id":"0a1f7f31-5f01-4348-83ab-17a6fca64597","user-agent":"Mozilla/5.0 (Macintosh) mirall/6.0.0.15610-daily20250205 (ownCloud, macos-24.3.0 ClientArchitecture: arm64 OsArchitecture: arm64)","x-request-id":"0a1f7f31-5f01-4348-83ab-17a6fca64597"},"info":{"cached":false,"id":"0a1f7f31-5f01-4348-83ab-17a6fca64597","method":"GET","url":"https://cloud.opencloud.test/.well-known/openid-configuration"}}}```

| Log Content | Description |
|-------------|-------------|
| **23-09-01 16:31:14:031** | Timestamp of the request |
| **[ info sync.httplogger ]** | Log category label |
| **eca37889-6dea-42cf-81a2-c3826efbf146** | X-REQUEST-ID (used to match requests & responses) |
| **Header: { }** | List of HTTP headers |
| **Data: []** | HTTP bodies (JSON, XML) |
| **(112ms)** | Response time (since the request was sent) |


## Using X-REQUEST-ID for Debugging
- The OpenCloud desktop app sends an **X-REQUEST-ID** header with every request.  
- This ID helps in finding corresponding requests and responses in logs.  
- You can configure your web server to add the **X-REQUEST-ID** to its logs for deeper analysis.  

This feature is useful for debugging sync issues, monitoring network activity, and troubleshooting connectivity problems.
