---
sidebar_position: 40
id: guest-access
title: Gastzugang
description: Externe Gäste per E-Mail-Adresse einladen, ihre Berechtigungen verwalten und als Gast auf freigegebene Inhalte zugreifen.
draft: false
---

# Gastzugang in OpenCloud

Mit dem Gastzugang können Sie mit externen Personen zusammenarbeiten, die kein OpenCloud-Konto haben.

Sie laden einen Gast über seine E-Mail-Adresse ein und gewähren ihm Zugriff auf eine bestimmte Datei oder einen bestimmten Ordner. Der Gast erhält eine Einladungs-E-Mail, öffnet den Link in einem Webbrowser und kann nur auf die Inhalte zugreifen, die Sie für ihn freigegeben haben.

:::note
Der Gastzugang muss von Ihrem Administrator aktiviert werden. Wenn Sie keine Gäste einladen können, wenden Sie sich an Ihren Administrator.
:::

## So funktioniert der Gastzugang

1. Die teilende Person wählt eine Datei oder einen Ordner aus und öffnet den Freigabebereich.
2. Sie gibt die externe E-Mail-Adresse ein und wählt eine Berechtigung aus.
3. OpenCloud sendet dem Gast eine Einladungs-E-Mail mit einem Link.
4. Der Gast öffnet den Link in einem Webbrowser.
5. Der Gast greift mit den zugewiesenen Berechtigungen auf die freigegebenen Inhalte zu.
6. Die teilende Person kann den Gastzugang jederzeit ändern oder entfernen.

Eine Gasteinladung gilt nur für die freigegebenen Dateien oder Ordner. Sie gewährt keinen Zugriff auf andere Inhalte in OpenCloud.

Wenn Sie jemanden einladen möchten, fahren Sie mit [Für die Person, die Inhalte teilt](#für-die-person-die-inhalte-teilt) fort. Wenn Sie eine Einladung erhalten haben, lesen Sie unter [Für den eingeladenen Gast](#für-den-eingeladenen-gast) weiter.

## Für die Person, die Inhalte teilt

Die teilende Person legt fest, auf welche Inhalte der Gast zugreifen kann, und ist für die Verwaltung dieses Zugriffs verantwortlich.

### Gast einladen

- Melden Sie sich bei OpenCloud an.
- Wählen Sie die Datei oder den Ordner aus, die bzw. den Sie freigeben möchten.
- Öffnen Sie in der rechten Seitenleiste den Bereich „Teilen“.
- Geben Sie im Feld „Mit Personen teilen“ die E-Mail-Adresse des Gasts ein.
- Wählen Sie den mit „(Gast)“ gekennzeichneten Eintrag aus.

<img src={require("./img/guest-access/invite-guest.png").default} alt="Gast über eine E-Mail-Adresse einladen" width="900"/>

- Wählen Sie eine Berechtigung aus. Weitere Informationen finden Sie unter [Gastberechtigungen festlegen](#gastberechtigungen-festlegen).
- Klicken Sie auf „Teilen“.

OpenCloud sendet eine Einladungs-E-Mail an die Adresse des Gasts.

:::note
Wenn eine E-Mail-Adresse zu einem bestehenden OpenCloud-Benutzer gehört, schlägt OpenCloud diesen Benutzer anstelle eines Gasts vor.
:::

### Gastberechtigungen festlegen

Die Gastberechtigungen bestimmen, welche Aktionen der Gast mit den freigegebenen Inhalten ausführen kann.

| Berechtigung                        | Beschreibung                                                                                                                                 |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kann anzeigen**                   | Der Gast kann die freigegebenen Inhalte anzeigen und herunterladen.                                                                          |
| **Kann anzeigen (sichere Ansicht)** | Der Gast kann Dokumente, Bilder und PDF-Dateien nur im Browser anzeigen. Downloads sind nicht möglich und Wasserzeichen werden eingeblendet. |
| **Kann hochladen**                  | Der Gast kann die freigegebenen Inhalte anzeigen und herunterladen sowie neue Dateien hochladen.                                             |
| **Kann bearbeiten**                 | Der Gast kann Inhalte anzeigen, herunterladen, hochladen, bearbeiten, hinzufügen und löschen.                                                |

Die verfügbaren Berechtigungen hängen von der Art der freigegebenen Ressource ab. „Kann hochladen“ ist beispielsweise nur für Ordner verfügbar.

Öffnen Sie die Berechtigungsauswahl unterhalb des E-Mail-Adressfelds, bevor Sie auf „Teilen“ klicken, um eine Berechtigung auszuwählen.

<img src={require("./img/guest-access/guest-permissions.png").default} alt="Berechtigungen für einen externen Gast auswählen" width="900"/>

:::tip
Gewähren Sie nur die Berechtigungen, die für die Zusammenarbeit erforderlich sind. Verwenden Sie „Kann anzeigen“, wenn der Gast keine Änderungen vornehmen muss, und „Kann anzeigen (sichere Ansicht)“, wenn der Gast die Inhalte nicht herunterladen darf.
:::

### Bestehenden Gastzugang verwalten

Sie können den Gastzugang jederzeit überprüfen und ändern.

- Wählen Sie die freigegebene Datei oder den freigegebenen Ordner aus.
- Öffnen Sie in der rechten Seitenleiste den Bereich „Teilen“.
- Suchen Sie im Bereich „Freigegeben mit“ nach dem Gast.
- Um die Berechtigung zu ändern, verwenden Sie die Berechtigungsauswahl unterhalb der E-Mail-Adresse des Gasts.
- Öffnen Sie das Aktionsmenü (**⋮**) neben dem Gast, um weitere Optionen anzuzeigen:
  - **Zugriffsdetails** – Zeigt Details zum Zugriff des Gasts an.
  - **Ablaufdatum festlegen** – Legt ein Datum fest, nach dem der Gastzugang automatisch endet.
  - **Freigabe entfernen** – Entzieht dem Gast den Zugriff.

<img src={require("./img/guest-access/manage-guest.png").default} alt="Gastzugang und Berechtigungen verwalten" width="900"/>

#### Gastzugang entfernen

- Wählen Sie die freigegebene Datei oder den freigegebenen Ordner aus.
- Öffnen Sie in der rechten Seitenleiste den Bereich „Teilen“.
- Öffnen Sie das Aktionsmenü (**⋮**) neben dem Gast.
- Wählen Sie „Freigabe entfernen“ aus.

<img src={require("./img/guest-access/remove-guest.png").default} alt="Externen Gast von einer freigegebenen Ressource entfernen" width="900"/>

Nachdem Sie die Freigabe entfernt haben, kann der Gast nicht mehr auf die Inhalte zugreifen. Dies gilt auch dann, wenn er noch über den Einladungslink oder eine aktive Gastsitzung verfügt.

:::important
Durch das Entfernen des Zugriffs werden keine Kopien von Dateien gelöscht, die der Gast bereits heruntergeladen hat.
:::

### Empfehlungen

- Überprüfen Sie die E-Mail-Adresse des Gasts, bevor Sie die Einladung senden.
- Wählen Sie die niedrigste Berechtigungsstufe aus, die für die Zusammenarbeit ausreicht.
- Legen Sie ein Ablaufdatum für den Gastzugang fest.
- Überprüfen Sie Ihre Gastfreigaben regelmäßig.
- Entfernen Sie den Gastzugang, wenn die Zusammenarbeit beendet ist.

### Fehlerbehebung für die teilende Person

#### Die Option „Gast“ wird nicht angezeigt

- Vergewissern Sie sich, dass Sie die vollständige E-Mail-Adresse eingegeben haben.
- Prüfen Sie, ob Sie die ausgewählte Datei oder den ausgewählten Ordner freigeben dürfen.
- Fragen Sie Ihren Administrator, ob der Gastzugang aktiviert ist.

#### Der Gast hat keine E-Mail erhalten

- Überprüfen Sie die Schreibweise der E-Mail-Adresse.
- Bitten Sie den Gast, seinen Spamordner zu überprüfen.
- Entfernen Sie die Gastfreigabe und laden Sie den Gast erneut ein.
- Wenn das Problem weiterhin besteht, wenden Sie sich an Ihren Administrator.

## Für den eingeladenen Gast

Der eingeladene Gast öffnet die freigegebenen Inhalte über seine persönliche Einladungs-E-Mail. Ein reguläres OpenCloud-Konto ist nicht erforderlich.

### Gasteinladung öffnen

Dieser Abschnitt beschreibt die Schritte für den eingeladenen Gast.

- Öffnen Sie die von OpenCloud gesendete Einladungs-E-Mail.
- Klicken Sie auf den Link in der E-Mail.
- Der Link öffnet OpenCloud in Ihrem Webbrowser.
- OpenCloud überprüft die Einladung automatisch. Sie müssen sich nicht anmelden.
- Die freigegebene Datei oder der freigegebene Ordner wird angezeigt.

<img src={require("./img/guest-access/invitation-email.png").default} alt="Gasteinladung per E-Mail mit einem persönlichen Zugangslink" width="1000"/>

:::important
Der Einladungslink ist persönlich. Leiten Sie ihn nicht an andere Personen weiter.
:::

#### Einladungslink und Gastsitzung

- **Einladungslink:** Öffnen Sie den Link in der Einladungs-E-Mail innerhalb von **30 Minuten**.
- **Gastsitzung:** Nachdem Sie den Link geöffnet haben, können Sie in diesem Browser für einen begrenzten Zeitraum auf die freigegebenen Inhalte zugreifen, standardmäßig **24 Stunden**. Während dieser Zeit können Sie denselben Link erneut verwenden, um zu den Inhalten zurückzukehren.
- **Neuer Link:** Wenn Sie den Link nach Ablauf der 30 Minuten, in einem anderen Browser oder nach Ablauf Ihrer Sitzung öffnen, erhalten Sie automatisch eine E-Mail mit einem neuen Link.

Die Gültigkeitsdauer des Einladungslinks ist fest vorgegeben. Administratoren können die Dauer der Gastsitzung konfigurieren.

Wenn Sie einen bereits verwendeten Einladungslink im selben Browser öffnen und Ihre Gastsitzung noch gültig ist, können Sie Ihre Arbeit fortsetzen.

### Auf freigegebene Inhalte zugreifen

Als Gast arbeiten Sie in der OpenCloud-Weboberfläche. Sie können nur auf die Datei oder den Ordner zugreifen, die bzw. der für Sie freigegeben wurde.

Abhängig von den erteilten Berechtigungen können Sie:

- freigegebene Dateien öffnen und anzeigen,
- freigegebene Ordner durchsuchen,
- Dateien herunterladen,
- Dateien hochladen sowie
- Inhalte bearbeiten, hinzufügen und löschen.

<img src={require("./img/guest-access/guest-access.png").default} alt="Gast greift auf eine freigegebene Ressource zu" width="1000"/>

:::note
Der Gastzugang ist nur im Webbrowser verfügbar. Gäste können weder den OpenCloud Desktop Client noch die mobilen Apps verwenden.
:::

### Gastzugang erneuern

Gastsitzungen laufen nach einem begrenzten Zeitraum ab, standardmäßig nach 24 Stunden. Eine abgelaufene Sitzung hebt die zugrunde liegende Freigabe nicht auf. Solange die Freigabe noch besteht und nicht abgelaufen ist, können Sie Ihren Zugriff über eine neue E-Mail erneuern.

#### Vor Ablauf der Sitzung mit einer PIN erneuern

Etwa 15 Minuten vor Ablauf der Sitzung zeigt OpenCloud eine Warnung an.

<img src={require("./img/guest-access/guest-session-renewal.png").default} alt="Warnung vor dem bevorstehenden Ablauf der Gastsitzung mit der Option, eine PIN anzufordern" width="1000"/>

1. Wählen Sie vor Ablauf der Sitzung „PIN anfordern“ aus.
2. Öffnen Sie die neueste E-Mail von OpenCloud.
3. Kehren Sie zum Browser zurück und wählen Sie „PIN eingeben“ aus.
4. Geben Sie die PIN aus der E-Mail ein und wählen Sie „Weiter“ aus.

<img src={require("./img/guest-access/guest-pin-verification.png").default} alt="Dialog zur Eingabe der PIN für die Verlängerung der Gastsitzung" width="1000"/>

Nach der Überprüfung wird die Gastsitzung erneuert, ohne dass Sie die freigegebenen Inhalte verlassen müssen.

Die PIN-Option ist nur verfügbar, solange OpenCloud in dem Browser, über den die Erneuerung angefordert wurde, eine bestehende Gastsitzung für diese Freigabe überprüfen kann. Die PIN ist an diesen Browser gebunden. Wenn Sie den Browser wechseln, verwenden Sie stattdessen den Einladungslink aus der E-Mail.

#### Nach Ablauf der Sitzung erneuern

Wenn OpenCloud erkennt, dass die Gastsitzung nicht mehr gültig ist, wird automatisch die Seite zur Erneuerung geöffnet.

<img src={require("./img/guest-access/guest-session-expired.png").default} alt="OpenCloud erneuert eine abgelaufene Gastsitzung" width="1000"/>

1. Warten Sie, während OpenCloud „Ihr Zugriff wird erneuert …“ anzeigt.
2. Wenn „Prüfen Sie Ihren Posteingang“ angezeigt wird, öffnen Sie die neueste E-Mail von OpenCloud.
3. Öffnen Sie den Einladungslink aus der E-Mail, um fortzufahren. Wenn der neueste Link abgelaufen ist oder bereits verwendet wurde, sendet OpenCloud einen neuen Link.
4. Nach der Überprüfung öffnet OpenCloud die freigegebenen Inhalte erneut.

Wenn die Freigabe entfernt wurde oder abgelaufen ist, kann der Gastzugang nicht erneuert werden. Bitten Sie die Person, die Sie eingeladen hat, die Inhalte erneut für Sie freizugeben.

### Fehlerbehebung für den eingeladenen Gast

#### Der Einladungslink funktioniert nicht

- Stellen Sie sicher, dass der vollständige Link aus der E-Mail geöffnet wurde.
- Der Link wurde möglicherweise bereits verwendet oder ist abgelaufen. Bitten Sie die Person, die die Inhalte freigegeben hat, Sie erneut einzuladen.

#### Sie können eine Datei nicht bearbeiten

- Bitten Sie die Person, die die Inhalte freigegeben hat, zu prüfen, ob Sie über die Berechtigung „Kann bearbeiten“ verfügen.
- Prüfen Sie, ob der Dateityp in OpenCloud bearbeitet werden kann.

## Gastzugang im Vergleich zu anderen Freigabemöglichkeiten

Gastzugang, öffentliche Links und reguläre OpenCloud-Konten sind unterschiedliche Zugriffsmethoden. Eine kurze Gegenüberstellung finden Sie unter [Freigabemethoden](./index.md).
