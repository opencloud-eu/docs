---
sidebar_position: 3
id: self-signed-certificates
title: Browser rejects a self-signed certificate
description: Accept a self-signed certificate in the browser
draft: false
hide_table_of_contents: true
---

# Browser rejects a self-signed certificate

## Problem

The browser displays a security warning when you access a local OpenCloud environment.

## Cause

The local environment uses a self-signed certificate that the browser does not trust automatically.

## Solution

Accept the security risk in your browser. In Firefox, select **Advanced**:

<img src={require("../img/common-issues/quick-advanced.png").default} alt="Admin general" width="500"/>

Then select **Accept the Risk and Continue**:

<img src={require("../img/common-issues/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>
