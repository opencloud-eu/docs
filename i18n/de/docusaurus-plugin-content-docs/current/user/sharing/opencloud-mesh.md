---
sidebar_position: 40
id: opencloud-mesh
title: ScienceMesh
description: Verbinden Sie sich mit Benutzern einer anderen OpenCloud-Instanz und teilen Sie Dateien oder Ordner mit ihnen.
draft: false
---

# Mit ScienceMesh verbinden und teilen

Mit der ScienceMesh-Anwendung können Sie sich mit Benutzern einer anderen OpenCloud-Instanz verbinden und Dateien oder Ordner mit ihnen teilen. Für Verbindungen zwischen Instanzen verwendet sie das OpenCloud-Mesh-Protokoll (OCM).

Bevor Sie beginnen, muss ein Administrator OCM auf beiden beteiligten Instanzen konfigurieren. Eine Anleitung finden Sie unter [OpenCloud Mesh konfigurieren](../../admin/configuration/ocm).

## ScienceMesh-Anwendung öffnen

1. Melden Sie sich bei OpenCloud Web an.
2. Öffnen Sie den Anwendungsumschalter.
3. Wählen Sie die ScienceMesh-Anwendung aus.

Die ScienceMesh-Anwendung stellt die Oberfläche zum Erstellen und Annehmen von OCM-Einladungen bereit.

<img src={require("./img/opencloud-mesh/open-ocm-application.png").default} alt="Anwendungsumschalter mit der ScienceMesh-Anwendung" width="1920" />

## Mit einem Benutzer verbinden

Bevor Sie Inhalte mit einem Benutzer auf einer anderen Instanz teilen können, müssen Sie eine OCM-Verbindung herstellen.

:::important

Erstellen Sie die Einladung auf einer OpenCloud-Instanz und nehmen Sie sie auf der anderen OpenCloud-Instanz an.

Nehmen Sie eine Einladung nicht auf derselben Instanz an, auf der sie erstellt wurde.

:::

### Einladung auf Ihrer Instanz erstellen

1. Wählen Sie im Bereich Benutzer einladen die Option Einladung erstellen aus.

   <img src={require("./img/opencloud-mesh/generate-invitation.png").default} alt="Bereich Benutzer einladen mit der Schaltfläche Einladung erstellen" width="1640" />

2. Geben Sie im Dialog Neue Einladung erstellen optional eine Beschreibung ein, anhand derer Sie die Einladung später erkennen können.
3. Wählen Sie Erstellen aus.

   <img src={require("./img/opencloud-mesh/generate-invitation-dialog.png").default} alt="Dialog Neue Einladung erstellen mit einer Beschreibung" width="1008" />

4. Der Einladungstoken wird erstellt und automatisch in Ihre Zwischenablage kopiert.
5. Senden Sie den vollständigen kopierten Token an den Benutzer auf der anderen Instanz.

Wenn Sie den Token erneut kopieren müssen, suchen Sie die Einladung im Bereich Benutzer einladen und verwenden Sie die Aktion Base64-Token kopieren.

<img src={require("./img/opencloud-mesh/copy-invitation-token.png").default} alt="Erstellte Einladung und Aktionen zum Kopieren des Einladungstokens" width="1640" />

### Einladung auf der anderen Instanz annehmen

Der eingeladene Benutzer führt auf seiner OpenCloud-Instanz folgende Schritte aus:

1. Melden Sie sich bei OpenCloud Web an.
2. Öffnen Sie die ScienceMesh-Anwendung.

   <img src={require("./img/opencloud-mesh/open-accept-invitations.png").default} alt="Bereich Einladungen annehmen in der ScienceMesh-Anwendung" width="1608" />

3. Fügen Sie im Bereich Einladungen annehmen den vollständigen Token in das Feld Einladungstoken eingeben ein.
4. Prüfen Sie, ob unter Institution die Domain der einladenden OpenCloud-Instanz angezeigt wird.
5. Wählen Sie Einladung annehmen aus.

   <img src={require("./img/opencloud-mesh/accept-invitation.png").default} alt="Einladungstoken mit erkannter Institution und der Schaltfläche Einladung annehmen" width="1608" />

Nachdem die Einladung angenommen wurde, ist der Benutzer der anderen Instanz als OCM-Verbindung verfügbar.

<img src={require("./img/opencloud-mesh/federated-connection.png").default} alt="Neue föderierte Verbindung in der ScienceMesh-Anwendung" width="1920" />

:::note

Senden Sie den vollständigen Token, der automatisch kopiert wurde, oder verwenden Sie die Aktion Base64-Token kopieren. Kopieren Sie nicht den verkürzten Token-Text, der in der Einladungstabelle angezeigt wird.

Einladungstokens laufen standardmäßig nach 24 Stunden ab. Erstellen Sie eine neue Einladung, wenn ein Token abgelaufen ist.

:::

## Datei oder Ordner teilen

Nachdem beide Benutzer verbunden sind:

1. Öffnen Sie die Dateien-Anwendung.
2. Wählen Sie eine Datei oder einen Ordner aus.
3. Öffnen Sie den Freigabebereich.
4. Wählen Sie unter Freigabetyp die Option Extern aus.

   <img src={require("./img/opencloud-mesh/select-external-share-type.png").default} alt="Menü Freigabetyp mit ausgewählten externen Benutzern" width="452" />

5. Geben Sie den vollständigen Namen oder einen Teil des Namens des verbundenen Benutzers in das Suchfeld ein.
6. Wählen Sie den passenden, als Extern gekennzeichneten Benutzer aus.

   <img src={require("./img/opencloud-mesh/find-external-user.png").default} alt="Suchergebnis mit einem externen föderierten Benutzer" width="452" />

7. Konfigurieren Sie die Berechtigungen.
8. Wählen Sie Teilen aus.

   <img src={require("./img/opencloud-mesh/share-with-external-user.png").default} alt="Ausgewählter externer Benutzer mit Berechtigungen und der Schaltfläche Teilen" width="452" />

Der Benutzer auf der anderen OpenCloud-Instanz sollte die freigegebene Ressource jetzt erhalten.

### Freigegebene Ressource auf der anderen Instanz öffnen

Der eingeladene Benutzer führt auf seiner OpenCloud-Instanz folgende Schritte aus:

1. Öffnen Sie die Dateien-Anwendung.
2. Wählen Sie in der linken Seitenleiste Freigaben aus.
3. Öffnen Sie Mit mir geteilt.
4. Prüfen Sie, ob die freigegebene Datei oder der freigegebene Ordner aufgeführt ist.

<img src={require("./img/opencloud-mesh/received-federated-share.png").default} alt="Föderierter Ordner unter Mit mir geteilt auf der empfangenden OpenCloud-Instanz" width="1920" />

## Fehlerbehebung

### Die ScienceMesh-Anwendung ist nicht sichtbar

Melden Sie sich von OpenCloud Web ab und laden Sie die Seite ohne Browsercache neu oder öffnen Sie ein privates Browserfenster. Melden Sie sich erneut an und prüfen Sie den Anwendungsumschalter.

Wenn die ScienceMesh-Anwendung weiterhin nicht verfügbar ist, wenden Sie sich an Ihren Administrator.

### Ein Benutzer wird im Freigabedialog nicht angezeigt

Prüfen Sie, ob Freigabetyp auf Extern gesetzt ist und beide Benutzer den Einladungsprozess erfolgreich abgeschlossen haben. Benutzer anderer Instanzen werden erst als Empfänger angezeigt, nachdem die OCM-Verbindung hergestellt wurde.

Wenn die Verbindung besteht, der Benutzer aber nicht angezeigt wird, wenden Sie sich an Ihren Administrator.

### Eine Einladung kann nicht angenommen werden

Prüfen Sie Folgendes:

- Die Einladung ist nicht abgelaufen.
- Sie sind bei der empfangenden OpenCloud-Instanz angemeldet.
- Sie nehmen die Einladung auf der anderen Instanz an und nicht auf der Instanz, auf der sie erstellt wurde.
- Der vollständige Einladungslink oder Token wurde kopiert.

Wenn die Einladung abgelaufen ist, bitten Sie den einladenden Benutzer, eine neue Einladung zu erstellen. Wenn sie weiterhin nicht angenommen werden kann, wenden Sie sich an Ihren Administrator.
