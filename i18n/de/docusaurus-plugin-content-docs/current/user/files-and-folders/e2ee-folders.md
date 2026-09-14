---
sidebar_position: 130
id: e2ee-folders
title: Ende-zu-Ende-verschlüsselte Ordner
description: Ende-zu-Ende-verschlüsselte Ordner in OpenCloud erstellen, entsperren und verwenden
draft: false
---

# Ende-zu-Ende-verschlüsselte Ordner

Ende-zu-Ende-verschlüsselte Ordner bieten eine zusätzliche Schutzebene für sensible Inhalte in OpenCloud.

Beim Erstellen eines Ende-zu-Ende-verschlüsselten Ordners legen Sie ein separates Passwort dafür fest. Sie benötigen dieses Passwort jedes Mal, wenn Sie den Ordner auf einem Gerät entsperren und auf seine Inhalte zugreifen.

:::danger

Bewahren Sie das Passwort für einen Ende-zu-Ende-verschlüsselten Ordner an einem sicheren Ort auf. OpenCloud kann es nicht zurücksetzen oder wiederherstellen. Wenn Sie das Passwort verlieren, verlieren Sie dauerhaft den Zugriff auf den Ordner und seine Inhalte.

:::

## Ende-zu-Ende-verschlüsselten Ordner erstellen

So erstellen Sie einen Ende-zu-Ende-verschlüsselten Ordner:

1. Gehen Sie zu dem Speicherort, an dem Sie den verschlüsselten Ordner erstellen möchten.
2. Öffnen Sie das Menü „+ Neu“.
3. Wählen Sie „Ordner“ aus.

<img src={require("./img/e2ee-folders/create-folder-menu.png").default} alt="Neuen Ordner über das Menü Neu erstellen" width="1920"/>

## Ende-zu-Ende-Verschlüsselung aktivieren

Im Dialog „Neuen Ordner erstellen“:

1. Geben Sie einen Ordnernamen ein.
2. Aktivieren Sie „Diesen Ordner Ende-zu-Ende verschlüsseln“.

<img src={require("./img/e2ee-folders/create-folder-name.png").default} alt="Dialog zum Erstellen eines neuen Ordners" width="400"/>

Wenn die Ende-zu-Ende-Verschlüsselung aktiviert ist, fügt OpenCloud dem Ordnernamen automatisch die Endung `.vault` hinzu.

<img src={require("./img/e2ee-folders/encryption-enabled.png").default} alt="Ende-zu-Ende-Verschlüsselung für den neuen Ordner aktiviert" width="400"/>

Klicken Sie auf „Fortfahren“.

## Ordnerpasswort festlegen

Nach dem Aktivieren der Ende-zu-Ende-Verschlüsselung müssen Sie ein Passwort für den Ordner festlegen.

Dieses Passwort entsperrt den verschlüsselten Ordner und wird benötigt, um auf die darin enthaltenen Dateien zuzugreifen.

<img src={require("./img/e2ee-folders/set-password.png").default} alt="Passwort für den verschlüsselten Ordner festlegen" width="400"/>

Der Dialog bietet folgende Funktionen:

- „Passwort anzeigen“ zeigt das eingegebene Passwort an.
  <img src={require("./img/e2ee-folders/show-password.png").default} alt="Schaltfläche Passwort anzeigen" width="400"/>

- „Passwort kopieren“ kopiert das Passwort in die Zwischenablage.
  <img src={require("./img/e2ee-folders/copy-password.png").default} alt="Schaltfläche Passwort kopieren" width="400"/>

:::important

Speichern Sie das Passwort an einem sicheren Ort, beispielsweise in einem Passwortmanager.

:::

Klicken Sie auf „Erstellen“.

## Verschlüsselten Ordner erkennen

Der verschlüsselte Ordner wird in der Dateiliste mit einem Schlosssymbol angezeigt.

<img src={require("./img/e2ee-folders/encrypted-folder-created.png").default} alt="Verschlüsselter Ordner in OpenCloud erstellt" width="1920"/>

Das Schlosssymbol zeigt an, dass der Ordner Ende-zu-Ende verschlüsselt ist.

## Verschlüsselten Ordner entsperren

Beim Öffnen eines verschlüsselten Ordners werden Sie aufgefordert, das Ordnerpasswort einzugeben.

<img src={require("./img/e2ee-folders/unlock-folder.png").default} alt="Ende-zu-Ende-verschlüsselten Ordner entsperren" width="400"/>

Geben Sie das Passwort ein und klicken Sie auf „Entsperren“.

Nach dem Entsperren des Ordners können Sie auf dessen Inhalte auf diesem Gerät zugreifen.

<img src={require("./img/e2ee-folders/unlocked-folder.png").default} alt="Entsperrter verschlüsselter Ordner" width="1920"/>

:::note

Sie müssen das Passwort auf jedem Gerät eingeben, auf dem Sie auf den verschlüsselten Ordner zugreifen möchten.

:::

## Dateien zu einem verschlüsselten Ordner hinzufügen

Nach dem Entsperren eines verschlüsselten Ordners können Sie vorhandene Dateien hochladen oder unterstützte Dateitypen direkt im Ordner erstellen.

### Dateien hochladen

Sie können vorhandene Dateien oder Ordner genauso in einen verschlüsselten Ordner hochladen wie in jeden anderen Ordner.

Weitere Informationen finden Sie unter [Dateien oder Ordner hochladen](./upload-download-unzip.md#dateien-oder-ordner-hochladen).

### Dateien erstellen

Nur die folgenden Dateitypen können direkt in einem verschlüsselten Ordner erstellt werden:

- Markdown-Dateien
- OC-Notizen

Andere Dateitypen wie Textdokumente, Tabellen und Präsentationen können nicht direkt in verschlüsselten Ordnern erstellt werden.

<img
src={require("./img/e2ee-folders/create-file-menu.png").default}
alt="Menü Neu in einem verschlüsselten Ordner mit deaktivierten Optionen für Dokumente, Tabellen und Präsentationen"
width="1920"
/>

Weitere Informationen finden Sie unter [Dateien und Ordner erstellen](./create-rename-move.md#dateien-und-ordner-erstellen).

## Verhalten bei Vorschau und Download

Einige Dateien in Ende-zu-Ende-verschlüsselten Ordnern können nicht direkt im Browser als Vorschau angezeigt werden.

In diesem Fall zeigt OpenCloud eine Meldung an, dass keine Vorschau verfügbar ist, und bietet stattdessen den Download der Datei an.

<img src={require("./img/e2ee-folders/no-preview-available.png").default} alt="Keine Vorschau für eine Datei in einem verschlüsselten Ordner verfügbar" width="1920"/>

## Einschränkungen

Ende-zu-Ende-verschlüsselte Ordner sind für die Speicherung sensibler Daten vorgesehen. Da ihre Inhalte verschlüsselt sind, stehen einige OpenCloud-Funktionen nicht zur Verfügung.

Es gelten folgende Einschränkungen:

- Dateien und Ordner können nicht von einem anderen Speicherort in OpenCloud in einen verschlüsselten Ordner verschoben werden.
- Die gemeinsame Bearbeitung von Dateien in verschlüsselten Ordnern ist nicht verfügbar.
- Office-Dokumente können im Browser nicht mit Collabora geöffnet oder bearbeitet werden.
- Für verschlüsselte Dateien ist keine Vorschau im Browser verfügbar.

Sie können vorhandene Dateien weiterhin direkt in einen verschlüsselten Ordner hochladen.
