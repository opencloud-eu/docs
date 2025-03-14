---
sidebar_position: 3
id: common-issues
title: Common Issues & Help
---

---

### Check whether the containers are running

```Shell
docker ps
```

<img src={require("./img/common-issues/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed here, e.g., for opencloud, traefik, etc.

---

### Accept Self-Signed Certificates:

As the local environment is self-signed, you must accept the security risk in your browser.

For Firefox:

You need to click on **Advanced**

<img src={require("./img/common-issues/quick-advanced.png").default} alt="Admin general" width="500"/>

Confirm the risk with **Accept the risk and Continue**

<img src={require("./img/common-issues/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>

