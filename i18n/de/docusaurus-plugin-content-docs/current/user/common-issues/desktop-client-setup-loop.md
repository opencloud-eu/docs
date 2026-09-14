---
sidebar_position: 4
id: desktop-client-setup-loop
title: Desktop-Client-Einrichtung wiederholt sich und Arbeitsspeichernutzung steigt
description: Fehlgeschlagene Desktop-Client-Einrichtung mit wiederholten Anmeldeversuchen beenden
draft: false
hide_table_of_contents: true
---

# Desktop-Client-Einrichtung wiederholt sich und Arbeitsspeichernutzung steigt

## Problem

Beim Hinzufügen eines Kontos in OpenCloud Desktop-Client 4.0.0 öffnet sich der Browser nicht zur Anmeldung. Das Einrichtungsfenster kann flackern und die Arbeitsspeichernutzung des Clients steigt weiter an.

## Ursache

Der Desktop-Client kann die Anfrage zur Servererkennung nicht abschließen. Wenn der Server oder ein Reverse Proxy diese Anfrage ablehnt, wiederholt Version 4.0.0 die Anfrage fortlaufend, anstatt einen Fehler anzuzeigen.

Eine bekannte Ursache ist eine Konfiguration in NGINX Proxy Manager, die die erforderliche WebFinger-Anfrage blockiert.

## Lösung

1. Beenden Sie den Desktop-Client. Wenn er nicht mehr reagiert, beenden Sie ihn über die Prozessverwaltung Ihres Betriebssystems.
2. Kontaktieren Sie Ihre OpenCloud-Administration und geben Sie die Serveradresse an.
3. Bitten Sie die Administration, die [WebFinger-Anfrage des Desktop-Clients zu prüfen](/docs/next/admin/resources/common-issues/desktop-client-setup-loop).
4. Starten Sie den Desktop-Client neu und fügen Sie das Konto erneut hinzu, nachdem die Server- oder Reverse-Proxy-Konfiguration korrigiert wurde.

Die Endlosschleife wurde für Desktop-Client 4.0.1 behoben. Der Server oder Reverse Proxy muss die WebFinger-Anfrage weiterhin zulassen, damit die Anmeldung gestartet werden kann.

Technische Details finden Sie im [Desktop-Issue #1077](https://github.com/opencloud-eu/desktop/issues/1077).
