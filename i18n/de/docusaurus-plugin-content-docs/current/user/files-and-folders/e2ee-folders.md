---
sidebar_position: 130
id: e2ee-folders
title: Ende-zu-Ende-verschlüsselte Ordner
description: Ende-zu-Ende-Verschlüsselung für Ordner in OpenCloud anzeigen
draft: false
---

# Ende-zu-Ende-verschlüsselte Ordner

Ende-zu-Ende-verschlüsselte Ordner bieten eine zusätzliche Schutzebene für sensible Dateien in OpenCloud.

Beim Erstellen eines Ende-zu-Ende-verschlüsselten Ordners legen Sie ein separates Passwort für diesen Ordner fest. Dieses Passwort wird benötigt, um den Ordner zu entsperren und auf dessen Inhalte zuzugreifen.

:::danger

Sie müssen sich das Passwort für einen Ende-zu-Ende-verschlüsselten Ordner unbedingt merken.

OpenCloud kann dieses Passwort nicht zurücksetzen, ändern, wiederherstellen oder neu vergeben. Wenn das Passwort verloren geht, ist der Zugriff auf den Ordner dauerhaft verloren. Das bedeutet auch, dass die Daten in diesem Ordner nicht wiederhergestellt werden können.

Kein Passwort bedeutet kein Zugriff. Wenn das Passwort verloren geht, ist der Datenverlust für diesen Ordner endgültig.

:::

## Ende-zu-Ende-verschlüsselten Ordner erstellen

So erstellen Sie einen Ende-zu-Ende-verschlüsselten Ordner:

1. Gehen Sie zu dem Speicherort, an dem Sie den verschlüsselten Ordner erstellen möchten.
2. Klicken Sie auf **Neu**.
3. Wählen Sie **Ordner** aus.

<img src={require("./img/e2ee-folders/create-folder-menu.png").default} alt="Neuen Ordner über das Menü Neu erstellen" width="1920"/>

## Ende-zu-Ende-Verschlüsselung aktivieren

Im Dialog **Neuen Ordner erstellen**:

1. Geben Sie einen Ordnernamen ein.
2. Aktivieren Sie **Diesen Ordner Ende-zu-Ende verschlüsseln**.

<img src={require("./img/e2ee-folders/create-folder-name.png").default} alt="Dialog zum Erstellen eines neuen Ordners" width="400"/>

Wenn die Ende-zu-Ende-Verschlüsselung aktiviert ist, fügt OpenCloud dem Ordnernamen automatisch die Endung `.vault` hinzu.

<img src={require("./img/e2ee-folders/encryption-enabled.png").default} alt="Ende-zu-Ende-Verschlüsselung für den neuen Ordner aktiviert" width="400"/>

Klicken Sie auf **Fortfahren**, um fortzufahren.

## Ordnerpasswort festlegen

Nach dem Aktivieren der Ende-zu-Ende-Verschlüsselung müssen Sie ein Passwort für den Ordner festlegen.

Dieses Passwort entsperrt den verschlüsselten Ordner und wird benötigt, um auf die darin enthaltenen Dateien zuzugreifen.

<img src={require("./img/e2ee-folders/set-password.png").default} alt="Passwort für den verschlüsselten Ordner festlegen" width="400"/>

Während der Passworteingabe können Sie folgende Funktionen verwenden:

- **Passwort anzeigen** – Zeigt das eingegebene Passwort an.

<img src={require("./img/e2ee-folders/show-password.png").default} alt="Schaltfläche Passwort anzeigen" width="400"/>

- **Passwort kopieren** – Kopiert das eingegebene Passwort in die Zwischenablage.

<img src={require("./img/e2ee-folders/copy-password.png").default} alt="Schaltfläche Passwort kopieren" width="400"/>

:::important

Speichern Sie das Passwort an einem sicheren Ort, zum Beispiel in einem Passwortmanager.

OpenCloud kann den Zugriff nicht wiederherstellen, wenn das Passwort vergessen wurde. Das Passwort kann später nicht zurückgesetzt, geändert oder neu vergeben werden.

:::

Klicken Sie auf **Erstellen**, um den verschlüsselten Ordner zu erstellen.

## Verschlüsselter Ordner in der Dateiliste

Nachdem der Ordner erstellt wurde, wird er in der Dateiliste mit einem Schloss-Symbol angezeigt.

<img src={require("./img/e2ee-folders/encrypted-folder-created.png").default} alt="Verschlüsselter Ordner in OpenCloud erstellt" width="1920"/>

Das Schloss-Symbol zeigt an, dass der Ordner Ende-zu-Ende verschlüsselt ist.

## Verschlüsselten Ordner entsperren

Beim Öffnen eines verschlüsselten Ordners werden Sie aufgefordert, das Ordnerpasswort einzugeben.

<img src={require("./img/e2ee-folders/unlock-folder.png").default} alt="Ende-zu-Ende-verschlüsselten Ordner entsperren" width="400"/>

Geben Sie das Passwort ein und klicken Sie auf **Entsperren**.

Nach dem Entsperren des Ordners können Sie auf dessen Inhalte auf diesem Gerät zugreifen.

<img src={require("./img/e2ee-folders/unlocked-folder.png").default} alt="Entsperrter verschlüsselter Ordner" width="1920"/>

:::note

Das Passwort wird benötigt, um die Dateien im verschlüsselten Ordner auf dem jeweiligen Gerät zu entschlüsseln.

Ohne Passwort kann nicht auf die Ordnerinhalte zugegriffen werden.

:::

## Dateien in einen verschlüsselten Ordner hochladen

Nachdem Sie den verschlüsselten Ordner entsperrt haben, können Sie Dateien in diesen Ordner hochladen.

1. Öffnen Sie den verschlüsselten Ordner.
2. Klicken Sie auf **Neu**.
3. Wählen Sie **Dateien hochladen** aus.
4. Wählen Sie die Datei von Ihrem Gerät aus.

<img src={require("./img/e2ee-folders/upload-file.png").default} alt="Datei in einen verschlüsselten Ordner hochladen" width="1920"/>

Die hochgeladene Datei wird im verschlüsselten Ordner gespeichert.

## Verhalten bei Vorschau und Download

Einige Dateien in Ende-zu-Ende-verschlüsselten Ordnern können möglicherweise nicht direkt im Browser als Vorschau angezeigt werden.

In diesem Fall zeigt OpenCloud eine Meldung an, dass keine Vorschau verfügbar ist, und bietet stattdessen den Download der Datei an.

<img src={require("./img/e2ee-folders/no-preview-available.png").default} alt="Keine Vorschau für eine Datei in einem verschlüsselten Ordner verfügbar" width="1920"/>

## Einschränkungen

Ende-zu-Ende-verschlüsselte Ordner sind für die Speicherung sensibler Daten vorgesehen.

Da die Inhalte verschlüsselt sind, können einige OpenCloud-Funktionen eingeschränkt sein. Dazu gehören unter anderem Funktionen zur Zusammenarbeit und Vorschauen direkt im Browser.

:::danger

Bewahren Sie das Passwort sicher auf.

OpenCloud kann das Passwort für einen Ende-zu-Ende-verschlüsselten Ordner nicht zurücksetzen, ändern, wiederherstellen oder neu vergeben. Wenn das Passwort verloren geht, kann der Ordner nicht mehr entsperrt werden und die darin enthaltenen Daten sind dauerhaft verloren.

:::
