# TCP-Portscanner

Ein in Python entwickeltes Projekt zur Untersuchung offener TCP-Ports und erreichbaren Netzwerkdiensten.

## Funktionen

- Scannen von TCP-Ports
- Erkennen offener Ports
- Zuordnung zu gängigen Netzwerkdiensten
- Parallele Scans mit mehreren Threads
- Einstellbare Portbereiche und Timeouts
- Bedienung über die Kommandozeile (CLI)

## Verwendung

Einen einfachen Scan starten:

```bash
python3 main.py 127.0.0.1
```

Einen bestimmten Portbereich scannen:

```bash
python3 main.py 127.0.0.1 -s 1 -e 1024
```

Die Anzahl der verwendeten Threads festlegen:

```bash
python3 main.py 127.0.0.1 -t 100
```

## Technologien

- Python
- TCP/IP
- Netzwerkkommunikation

## Lernziele

Im Fokus des Projekts stehen folgende Themenbereiche:

- Netzwerksicherheit
- Analyse von Netzwerken und Netzwerkdiensten
- Programmierung mit Python
- Kommunikation über TCP/IP
- Grundlagen der IT-Sicherheit
