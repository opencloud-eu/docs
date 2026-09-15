---
sidebar_position: 4
id: desktop-client-setup-loop
title: Desktop-Client-Einrichtung wiederholt sich und Arbeitsspeichernutzung steigt
description: Hilfe, wenn sich bei der Desktop-Client-Einrichtung der Browser nicht öffnet
draft: false
hide_table_of_contents: true
---

# Desktop-Client-Einrichtung wiederholt sich und Arbeitsspeichernutzung steigt

## Problem

Beim Hinzufügen eines Kontos im OpenCloud Desktop-Client öffnet sich der Browser nicht zur Anmeldung. Das Einrichtungsfenster kann flackern und die Arbeitsspeichernutzung des Clients steigt weiter an.

## Ursache

Der Desktop-Client kann die Anfrage zur Servererkennung nicht abschließen. Die Server- oder Reverse-Proxy-Konfiguration muss möglicherweise von der Administration angepasst werden.

## Lösung

1. Beenden Sie den Desktop-Client. Wenn er nicht mehr reagiert, beenden Sie ihn über die Prozessverwaltung Ihres Betriebssystems.
2. Kontaktieren Sie Ihre OpenCloud-Administration und geben Sie die Serveradresse an.
3. Bitten Sie die Administration, der [Admin-Anleitung zur Desktop-Client-Einrichtung](/docs/next/admin/resources/common-issues/desktop-client-setup-loop) zu folgen.
4. Starten Sie den Desktop-Client neu und fügen Sie das Konto erneut hinzu, nachdem die Server- oder Reverse-Proxy-Konfiguration korrigiert wurde.
