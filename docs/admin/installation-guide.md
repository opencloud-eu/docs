---
sidebar_position: 3
id: installation-guide
title: Installation on Ubuntu Server
---

Die Anleitung beschreibt die Installation von ownCloud Infinite Scale (oCIS) auf einem Ubuntu LTS-Server unter Verwendung von Docker Compose für den produktiven Einsatz. Ziel ist es, oCIS zusammen mit Web-Office-Anwendungen für die Dokumentenzusammenarbeit bereitzustellen, was sich besonders für den Heimgebrauch oder kleine Unternehmen eignet. Es werden gültige Zertifikate von Let's Encrypt verwendet.

Voraussetzungen:

    Hardware: Die Anleitung ist für verschiedene Hardwaretypen geeignet, darunter Raspberry Pi (ab Version 4), physische Server oder virtuelle Maschinen. Es werden mindestens 4-6 GB RAM empfohlen. Für die Standarddienste werden etwa 2,4 GB Speicherplatz benötigt.

    Kenntnisse: Administratoren sollten in der Lage sein, externe Domains zu konfigurieren, Router, Firewalls und Netzwerke einzurichten sowie grundlegende Befehle in der Kommandozeile auszuführen und Server zu warten.

    Software: Die Anleitung basiert auf Ubuntu LTS 24.04, ist jedoch auch mit Ubuntu LTS 22.04 kompatibel. Es wird vorausgesetzt, dass Docker und Docker Compose installiert und vorkonfiguriert sind.

Schritte zur Installation:

    Server vorbereiten: Installieren Sie die erforderlichen Softwarepakete und stellen Sie sicher, dass der Server auf dem neuesten Stand ist.

    Beispiel herunterladen und übertragen: Laden Sie die bereitgestellten Beispielkonfigurationen herunter und übertragen Sie sie auf Ihren Server.

    Konfigurationsdatei bearbeiten: Passen Sie die Konfigurationsdatei entsprechend Ihrer Umgebung an, insbesondere hinsichtlich der Domain-Namen und Zertifikatseinstellungen.

    Zertifikate generieren: Führen Sie den Prozess zur Generierung von Let's Encrypt-Zertifikaten durch, um sichere HTTPS-Verbindungen zu ermöglichen.

    Deployment starten: Starten Sie die Bereitstellung mit Docker Compose und überprüfen Sie, ob alle Dienste ordnungsgemäß laufen.

    Erster Login: Melden Sie sich zum ersten Mal an und ändern Sie das Standard-Admin-Passwort.

    Überwachung und Wartung: Überwachen Sie die laufenden Container und Logs, führen Sie regelmäßige Backups durch und aktualisieren Sie die Installation bei Bedarf.

Die Anleitung betont die Bedeutung eines gründlichen Verständnisses der einzelnen Schritte und empfiehlt, die gesamte Dokumentation sorgfältig zu lesen, anstatt nur Befehle zu kopieren und einzufügen. Es wird darauf hingewiesen, dass jede Bereitstellung nur eine Instanz von oCIS enthält.