# Network Scanner and Service Analyzer

A lightweight Python-based network reconnaissance tool for TCP port scanning, service detection, banner grabbing, and HTML report generation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)

---

## Overview

Network Scanner and Service Analyzer is a command-line application that identifies open TCP ports, detects common network services, attempts banner grabbing where supported, and generates HTML reports summarizing the results.

## Features

- TCP port scanning
- Common service detection
- Banner grabbing
- HTML report generation
- Modular codebase
- Configurable target ports
- Command-line interface

## Project Structure

```text
Network-scanner-and-service-analyzer/
├── main.py
├── scanner.py
├── services.py
├── report.py
├── utils.py
├── requirements.txt
├── reports/
│   └── *.html
└── README.md
```

## Installation

Clone the repository:

```bash
git clone git@github.com:Jerin7575/Network-scanner-and-service-analyzer.git
cd Network-scanner-and-service-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Enter the target IP address or hostname when prompted.

## Generated Report

Each scan produces an HTML report containing:

- Target information
- Scan timestamp
- Open ports
- Detected services
- Service banners (when available)
- Scan summary

## Roadmap

- Host discovery
- Multi-threaded scanning
- UDP scanning
- Custom port ranges
- Command-line arguments
- JSON/CSV export
- OS fingerprinting
- Service version detection

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Always obtain permission before scanning systems or networks you do not own.

## License

Released under the MIT License.
