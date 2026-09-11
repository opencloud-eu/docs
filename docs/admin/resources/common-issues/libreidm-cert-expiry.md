---
sidebar_position: 6
id: libreidm-cert-expiry
title: Internal LibreIDM certificate expires
description: Handle expired internal LibreIDM certificates
draft: false
hide_table_of_contents: true
---

# Internal LibreIDM certificate expires

## Problem

In OpenCloud releases earlier than 7.3, an expired internal LibreIDM certificate can interrupt communication with the directory service.

## Cause

These older releases do not automatically renew the internal LibreIDM certificate before it expires.

## Solution

Starting with OpenCloud 7.3, internal LibreIDM certificates are renewed automatically before they expire. No manual certificate removal or container restart is required.

For affected older releases, see the remediation instructions for [OpenCloud 7.2](/docs/admin/resources/common-issues/libreidm-cert-expiry) or [OpenCloud 4.0](/docs/4.0/admin/resources/common-issues/#internal-libreidm-cert-expires).
