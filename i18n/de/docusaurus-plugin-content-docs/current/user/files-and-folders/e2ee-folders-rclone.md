---
sidebar_position: 131
id: e2ee-folders-rclone
title: Mit rclone auf Ende-zu-Ende-verschlüsselte Ordner zugreifen
description: Einen Ende-zu-Ende-verschlüsselten OpenCloud-Ordner mit rclone crypt auf Ihrem Computer einbinden
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Mit rclone auf Ende-zu-Ende-verschlüsselte Ordner zugreifen

Der OpenCloud Web Client verschlüsselt Ende-zu-Ende-verschlüsselte Ordner im Format `rclone crypt`. Sie können einen solchen Ordner daher mit [rclone](https://rclone.org/) auf Ihrem Computer einbinden. Der eingebundene Ordner verhält sich wie ein lokaler Ordner: Sie können Dateien mit Ihren gewohnten Anwendungen öffnen, bearbeiten und hinzufügen, während die Dateiinhalte und -namen auf dem OpenCloud-Server verschlüsselt bleiben.

Dateien werden auf Ihrem Computer verschlüsselt, bevor rclone sie hochlädt. Dateien, die über die Einbindung erstellt wurden, können im OpenCloud Web Client geöffnet werden. Dateien, die im Web Client erstellt wurden, können über die Einbindung geöffnet werden.

Diese Anleitung basiert auf OpenCloud 9.0.0 und richtet sich an Benutzer, die mit der Kommandozeile vertraut sind.

## Übersicht

Die Einrichtung umfasst folgende Schritte:

1. Erstellen Sie im OpenCloud Web Client den [verschlüsselten Ordner](./e2ee-folders).
2. [Installieren Sie rclone](#rclone-installieren) auf Ihrem Computer.
3. [Erstellen Sie ein App-Token](#app-token-erstellen) in OpenCloud.
4. [Rufen Sie die WebDAV-URL](#webdav-url-abrufen) des verschlüsselten Ordners ab.
5. [Erstellen Sie ein WebDAV-Remote](#webdav-remote-konfigurieren) in rclone.
6. [Erstellen Sie ein crypt-Remote](#verschlüsseltes-remote-konfigurieren) zur Entschlüsselung.
7. [Binden Sie den verschlüsselten Ordner ein](#verschlüsselten-ordner-einbinden).

## Voraussetzungen

Sie benötigen:

- einen Ende-zu-Ende-verschlüsselten Ordner in OpenCloud und dessen Passwort
- ein OpenCloud App-Token
- die WebDAV-URL des verschlüsselten Ordners

Für die Einrichtung werden zwei aufeinander aufbauende rclone-Remotes verwendet:

| Remote-Typ | Beispielname          | Zweck                                                                      |
| ---------- | --------------------- | -------------------------------------------------------------------------- |
| WebDAV     | `opencloud-e2ee`      | Stellt die Verbindung zum verschlüsselten `.vault`-Ordner in OpenCloud her |
| `crypt`    | `opencloud-decrypted` | Ermöglicht den entschlüsselten Zugriff auf die Ordnerinhalte               |

`opencloud-e2ee` und `opencloud-decrypted` sind Beispielnamen. Sie können beliebige Namen für die Remotes wählen. Entscheidend ist, dass Sie die gewählten Namen in der gesamten Konfiguration und in allen Befehlen einheitlich verwenden.

:::danger

Bewahren Sie das Passwort des verschlüsselten Ordners sicher auf. OpenCloud kann es weder zurücksetzen noch wiederherstellen. Wenn Sie das Passwort verlieren, verlieren Sie dauerhaft den Zugriff auf den verschlüsselten Ordner und dessen Inhalte.

:::

Das App-Token und das Passwort des verschlüsselten Ordners sind separate Anmeldedaten für unterschiedliche Zwecke:

| Anmeldedaten                         | Zweck                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| OpenCloud App-Token                  | Authentifiziert die WebDAV-Verbindung                                          |
| Passwort des verschlüsselten Ordners | Wird von `rclone crypt` zum Ver- und Entschlüsseln der Ordnerinhalte verwendet |

Verwenden Sie weder das App-Token als `crypt`-Passwort noch das Passwort des verschlüsselten Ordners als WebDAV-Passwort.

<!-- Screenshot-Vorschlag:
Den E2EE-Ordner im OpenCloud Web Client zeigen.
Keine echten Anmeldedaten, URLs oder vertraulichen IDs anzeigen.
-->

## rclone installieren

Für die Einbindung benötigen Sie je nach Betriebssystem rclone und eine FUSE- oder NFS-Komponente.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

Installieren Sie rclone mit dem offiziellen Installationsskript:

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

Installieren Sie FUSE 3, beispielsweise unter Debian und Ubuntu:

```bash
sudo apt install fuse3
```

Weitere Installationsmethoden finden Sie in der [rclone-Installationsanleitung](https://rclone.org/install/).

</TabItem>
<TabItem value="macos" label="macOS">

Installieren Sie rclone mit dem offiziellen Installationsskript:

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

:::caution

Installieren Sie rclone nicht mit Homebrew. Die Homebrew-Version von rclone unterstützt das Einbinden nicht.

:::

Es ist keine zusätzliche Software erforderlich. Unter macOS verwendet diese Anleitung `rclone nfsmount`, das den Ordner über einen integrierten NFS-Server einbindet.

Weitere Installationsmethoden finden Sie in der [rclone-Installationsanleitung](https://rclone.org/install/).

</TabItem>
<TabItem value="windows" label="Windows">

Installieren Sie rclone und [WinFsp](https://winfsp.dev/) in PowerShell:

```powershell
winget install Rclone.Rclone
winget install WinFsp.WinFsp
```

WinFsp ist zum Einbinden von Ordnern unter Windows erforderlich. Öffnen Sie nach der Installation ein neues PowerShell-Fenster, damit der Befehl `rclone` verfügbar ist.

Weitere Installationsmethoden finden Sie in der [rclone-Installationsanleitung](https://rclone.org/install/).

</TabItem>
</Tabs>

Überprüfen Sie die Installation:

```bash
rclone version
```

## App-Token erstellen

Erstellen Sie in Ihren OpenCloud-Kontoeinstellungen ein eigenes App-Token für rclone. Kopieren Sie es, sobald es angezeigt wird, da es später nicht erneut angezeigt werden kann.

Eine ausführliche Anleitung finden Sie unter [App-Tokens](../admin/app-tokens).

Das App-Token wird als Passwort für das WebDAV-Remote verwendet. Es ist nicht das Passwort des verschlüsselten Ordners. Das Passwort Ihres OpenCloud-Kontos funktioniert nicht mit rclone.

<!-- Screenshot-Vorschlag:
Die Erstellung eines App-Tokens in den OpenCloud-Kontoeinstellungen zeigen.
Kein echtes Token und keine anderen Anmeldedaten anzeigen.
-->

## WebDAV-URL abrufen

Aktivieren Sie in Ihren OpenCloud-Kontoeinstellungen „WebDAV-Informationen in der Detailansicht anzeigen“, öffnen Sie das Detail-Panel des verschlüsselten Ordners und kopieren Sie dessen WebDAV-URL. Eine allgemeine Anleitung finden Sie unter [Über WebDAV mit einem Space verbinden](../admin/web-dav).

Die URL muss auf den verschlüsselten `.vault`-Ordner verweisen, zum Beispiel:

```text
https://cloud.example.com/dav/spaces/<space-id>/Encrypted.vault
```

<!-- Screenshot-Vorschlag:
Zeigen, wo die WebDAV-URL des verschlüsselten Ordners im Web Client kopiert werden kann.
Keine echten Anmeldedaten oder vertraulichen IDs anzeigen.
-->

## WebDAV-Remote konfigurieren

Führen Sie `rclone config` aus und erstellen Sie ein WebDAV-Remote. In dieser Anleitung wird `opencloud-e2ee` als Beispielname verwendet. Verwenden Sie:

- die WebDAV-URL des verschlüsselten Ordners als URL
- `infinitescale` als Anbieter
- Ihren OpenCloud-Benutzernamen als Benutzer
- Ihr OpenCloud App-Token als Passwort

Wenn rclone Passwörter in seine Konfiguration schreibt, speichert es sie in verschleierter Form. Wenn Sie die Konfiguration manuell bearbeiten, erstellen Sie den Wert für `pass` mit [`rclone obscure`](https://rclone.org/commands/rclone_obscure/). Führen Sie `rclone config file` aus, um die Konfigurationsdatei auf Ihrem System zu finden.

Die resultierende Konfiguration sollte ungefähr so aussehen:

```ini
[opencloud-e2ee]
type = webdav
url = https://cloud.example.com/dav/spaces/<space-id>/Encrypted.vault
vendor = infinitescale
user = <username>
pass = <obscured-app-token>
```

Weitere Informationen zu den Backend-Optionen finden Sie in der [rclone-WebDAV-Dokumentation](https://rclone.org/webdav/).

Testen Sie die WebDAV-Verbindung, bevor Sie fortfahren:

```bash
rclone ls opencloud-e2ee:
```

Ersetzen Sie `opencloud-e2ee` durch den Namen Ihres WebDAV-Remotes, falls Sie einen anderen Namen gewählt haben.

Wenn die Verbindung funktioniert, zeigt rclone möglicherweise verschlüsselte Dateinamen an. Beim WebDAV-Remote ist dies zu erwarten.

## Verschlüsseltes Remote konfigurieren

Das `crypt`-Remote stellt nicht direkt eine Verbindung zu OpenCloud her. Es ergänzt das vorhandene WebDAV-Remote um Ver- und Entschlüsselung. Erstellen und testen Sie zuerst das WebDAV-Remote.

Erstellen Sie ein zweites Remote mit dem `crypt`-Backend. In dieser Anleitung wird `opencloud-decrypted` als Beispielname verwendet. Konfigurieren Sie es wie folgt:

- Setzen Sie `remote` auf den exakten Namen Ihres WebDAV-Remotes, gefolgt von einem Doppelpunkt.
- Setzen Sie `filename_encryption` auf `standard`.
- Aktivieren Sie `directory_name_encryption`.
- Verwenden Sie das Passwort des verschlüsselten Ordners als `password`.
- Konfigurieren Sie keinen zusätzlichen Wert für `password2`.

Die resultierende Konfiguration sollte ungefähr so aussehen:

```ini
[opencloud-decrypted]
type = crypt
remote = opencloud-e2ee:
filename_encryption = standard
directory_name_encryption = true
password = <obscured-folder-password>
```

Der Wert `remote` besteht immer aus dem exakten Namen des WebDAV-Remotes, gefolgt von `:`. Geben Sie in diesem Feld nicht die WebDAV-URL ein.

Wenn Sie die Konfiguration manuell bearbeiten, erstellen Sie den Wert für `password` mit [`rclone obscure`](https://rclone.org/commands/rclone_obscure/). Weitere Informationen zu den Backend-Optionen finden Sie in der [rclone-crypt-Dokumentation](https://rclone.org/crypt/).

:::caution

Die in der rclone-Konfigurationsdatei gespeicherten Passwörter sind lediglich verschleiert und nicht sicher verschlüsselt. Schützen Sie die Konfigurationsdatei vor unbefugtem Zugriff.

:::

Testen Sie das verschlüsselte Remote:

```bash
rclone ls opencloud-decrypted:
```

Ersetzen Sie `opencloud-decrypted` durch den Namen Ihres `crypt`-Remotes, falls Sie einen anderen Namen gewählt haben.

rclone sollte die ursprünglichen Dateinamen anzeigen. Wenn verschlüsselte Dateinamen angezeigt werden, lesen Sie [Verschlüsselte Dateinamen werden angezeigt](#verschlüsselte-dateinamen-werden-angezeigt).

## Verschlüsselten Ordner einbinden

Binden Sie das `crypt`-Remote ein, nicht das WebDAV-Remote. Nur das `crypt`-Remote entschlüsselt die Ordnerinhalte.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

Erstellen Sie einen leeren Ordner als Einhängepunkt:

```bash
mkdir -p ~/OpenCloud-Encrypted
```

Binden Sie den verschlüsselten Ordner ein:

```bash
rclone mount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes
```

Der Ordner bleibt eingebunden, solange der Befehl ausgeführt wird. Lassen Sie das Terminal geöffnet, während Sie mit den Dateien arbeiten.

Fügen Sie `--daemon` hinzu, um die Einbindung im Hintergrund auszuführen:

```bash
rclone mount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes --daemon
```

</TabItem>
<TabItem value="macos" label="macOS">

Erstellen Sie einen leeren Ordner als Einhängepunkt:

```bash
mkdir -p ~/OpenCloud-Encrypted
```

Binden Sie den verschlüsselten Ordner ein:

```bash
rclone nfsmount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes
```

Der Ordner bleibt eingebunden, solange der Befehl ausgeführt wird. Lassen Sie das Terminal geöffnet, während Sie mit den Dateien arbeiten. Der eingebundene Ordner wird auch im Finder angezeigt.

Fügen Sie `--daemon` hinzu, um die Einbindung im Hintergrund auszuführen:

```bash
rclone nfsmount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes --daemon
```

</TabItem>
<TabItem value="windows" label="Windows">

Binden Sie den verschlüsselten Ordner in PowerShell als Laufwerk `X:` ein:

```powershell
rclone mount opencloud-decrypted: X: --vfs-cache-mode writes
```

Verwenden Sie einen noch nicht belegten Laufwerksbuchstaben. Soll rclone einen freien Laufwerksbuchstaben auswählen, verwenden Sie `*` anstelle von `X:`.

Das Laufwerk bleibt eingebunden, solange der Befehl ausgeführt wird. Lassen Sie das PowerShell-Fenster geöffnet, während Sie mit den Dateien arbeiten. Das Laufwerk wird im Datei-Explorer angezeigt.

</TabItem>
</Tabs>

Ersetzen Sie `opencloud-decrypted` durch den Namen Ihres `crypt`-Remotes, falls Sie einen anderen Namen gewählt haben.

:::note

Eine rclone-Einbindung ermöglicht den Zugriff auf Dateien über ein virtuelles Dateisystem. Sie erstellt keine vollständig synchronisierte lokale Kopie. Für den Zugriff auf noch nicht zwischengespeicherte Dateien ist eine aktive Verbindung zu OpenCloud erforderlich.

:::

`--vfs-cache-mode writes` puffert geänderte Dateien auf Ihrem Computer, bevor sie hochgeladen werden. Die meisten Anwendungen benötigen diese Option, um Dateien im eingebundenen Ordner zu bearbeiten. Außerdem wiederholt rclone fehlgeschlagene Uploads. Weitere Informationen finden Sie in der Dokumentation zu [`rclone mount`](https://rclone.org/commands/rclone_mount/).

Sie können nun mit den Dateien im eingebundenen Ordner arbeiten. Neue und geänderte Dateien werden auf Ihrem Computer verschlüsselt und zu OpenCloud hochgeladen.

### Einbindung überprüfen

1. Erstellen Sie eine kleine Testdatei im eingebundenen Ordner.
2. Prüfen Sie nach Abschluss des Uploads, ob die Datei im OpenCloud Web Client korrekt angezeigt wird.
3. Erstellen Sie im Web Client eine kleine Datei im verschlüsselten Ordner.
4. Prüfen Sie, ob die Datei über den eingebundenen Ordner zugänglich ist.

:::note

Änderungen aus dem OpenCloud Web Client können bis zu fünf Minuten benötigen, bevor sie im eingebundenen Ordner erscheinen, da rclone die Ordnerstruktur zwischenspeichert.

:::

## Verschlüsselten Ordner aushängen

Schließen Sie vor dem Aushängen alle geöffneten Dateien und stellen Sie sicher, dass ausstehende Uploads abgeschlossen sind. Bei aktiviertem VFS-Caching können Änderungen noch lokal gespeichert sein und auf den Upload zu OpenCloud warten. Prüfen Sie vor dem Beenden von rclone, ob kürzlich geänderte Dateien im Web Client korrekt angezeigt werden.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

Wenn die Einbindung im Terminal ausgeführt wird, drücken Sie <kbd>Strg</kbd>+<kbd>C</kbd>.

Wenn die Einbindung im Hintergrund ausgeführt wird, verwenden Sie:

```bash
fusermount3 -u ~/OpenCloud-Encrypted
```

Verwenden Sie auf Systemen mit FUSE 2 stattdessen `fusermount -u`.

</TabItem>
<TabItem value="macos" label="macOS">

Wenn die Einbindung im Terminal ausgeführt wird, drücken Sie <kbd>Strg</kbd>+<kbd>C</kbd>.

Wenn die Einbindung im Hintergrund ausgeführt wird, verwenden Sie:

```bash
pgrep -fl "rclone nfsmount opencloud-decrypted: $HOME/OpenCloud-Encrypted"
```

Vergewissern Sie sich, dass die Ausgabe ausschließlich den rclone-Prozess für diese Einbindung enthält. Notieren Sie die Prozess-ID am Anfang der Zeile und senden Sie anschließend SIGTERM an diesen Prozess:

```bash
kill -TERM <pid>
```

Wenn Sie einen anderen Remote-Namen oder Einhängepunkt gewählt haben, passen Sie das `pgrep`-Muster an. Verwenden Sie weder `killall` noch ein ungefiltertes `pkill`, da dadurch andere rclone-Prozesse beendet werden können.

</TabItem>
<TabItem value="windows" label="Windows">

Drücken Sie im PowerShell-Fenster, in dem die Einbindung ausgeführt wird, <kbd>Strg</kbd>+<kbd>C</kbd>.

</TabItem>
</Tabs>

## Fehlerbehebung

### Verschlüsselte Dateinamen werden angezeigt

Verschlüsselte Dateinamen sind zu erwarten, wenn Sie das WebDAV-Remote direkt verwenden, beispielsweise mit `rclone ls opencloud-e2ee:`.

Verwenden Sie das `crypt`-Remote zum Auflisten und Einbinden:

```bash
rclone ls opencloud-decrypted:
```

Wenn `rclone ls opencloud-decrypted:` keine Ausgabe zurückgibt, prüfen Sie zunächst, ob der verschlüsselte Ordner Dateien enthält. Der Befehl `rclone ls` listet Dateien auf, zeigt jedoch keine leeren Verzeichnisse an. Ein leeres Ergebnis weist daher nicht zwangsläufig auf einen Konfigurationsfehler hin.

Wenn der Ordner Dateien enthält und das `crypt`-Remote verschlüsselte Dateinamen oder keine Dateien anzeigt, prüfen Sie, ob das `crypt`-Passwort mit dem Passwort des verschlüsselten Ordners übereinstimmt und ob `filename_encryption` und `directory_name_encryption` wie unter [Verschlüsseltes Remote konfigurieren](#verschlüsseltes-remote-konfigurieren) beschrieben gesetzt sind.

### rclone findet den Konfigurationsabschnitt nicht

Der folgende Fehler weist darauf hin, dass das `crypt`-Remote die WebDAV-URL anstelle des Namens des WebDAV-Remotes enthält:

```text
didn't find section in config file ("https")
```

Die Option `remote` in der `crypt`-Konfiguration muss den Namen des WebDAV-Remotes gefolgt von einem Doppelpunkt enthalten:

Richtig:

```ini
remote = opencloud-e2ee:
```

Falsch:

```ini
remote = https://cloud.example.com/dav/...
```

Aktualisieren Sie den Wert `remote` und führen Sie den Test erneut aus.

### Der Ordner kann nicht eingebunden werden

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

- Prüfen Sie, ob FUSE 3 installiert ist.
- Prüfen Sie, ob der Einhängepunkt vorhanden und leer ist.
- Auf aktuellen Ubuntu-Versionen kann AppArmor FUSE-Einbindungen blockieren. Weitere Informationen finden Sie in der Dokumentation zu [`rclone mount`](https://rclone.org/commands/rclone_mount/).

</TabItem>
<TabItem value="macos" label="macOS">

- Prüfen Sie, ob rclone nicht mit Homebrew installiert wurde. Führen Sie `which rclone` aus und installieren Sie rclone bei Bedarf mit dem Installationsskript neu.
- Prüfen Sie, ob der Einhängepunkt vorhanden und leer ist.
- Wenn macOS rclone mit der Meldung blockiert, dass der Entwickler nicht verifiziert werden kann, lesen Sie die [rclone-Installationsanleitung](https://rclone.org/install/).

</TabItem>
<TabItem value="windows" label="Windows">

- Prüfen Sie, ob WinFsp installiert ist.
- Prüfen Sie, ob der Laufwerksbuchstabe bereits verwendet wird.

</TabItem>
</Tabs>
