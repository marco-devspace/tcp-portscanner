# TCP Port Scanner

A personal cybersecurity project written in Python for analyzing open TCP ports and available network services.


## Features

- TCP port scanning
- Detection of open ports
- Identification of common services
- Multi-threaded scanning to improve performance
- Configurable port ranges and timeouts
- Command-line interface (CLI)

## Usage

Basic scan:
```bash
python3 main.py 127.0.0.1
```
Scan a custom port range:
```bash
python3 main.py 127.0.0.1 -s 1 -e 1024
```
Change the number of threads:
```bash
python3 main.py 127.0.0.1 -t 100
```

## Technologies

- Python
- TCP/IP
- Network communication


## Learning Goals

This project was created to strengthen practical knowledge in:

- Network Security
- Network Analysis
- Python Programming
- TCP/IP Communication
- Cybersecurity Fundamentals


## Disclaimer

This project is intended for educational purposes only.

Only scan systems and networks where you have explicit permission.
