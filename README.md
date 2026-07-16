Network Scanner and Service Analyzer

«A lightweight Python-based network reconnaissance tool for TCP port scanning, service detection, banner grabbing, and HTML report generation.»

"Python" (https://img.shields.io/badge/Python-3.8%2B-blue)
"License" (https://img.shields.io/badge/License-MIT-green)
"Platform" (https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)

---

Overview

Network Scanner and Service Analyzer is a command-line application that helps identify open TCP ports, detect common network services, retrieve service banners when available, and generate structured HTML reports.

The project is designed with a modular architecture, making it easy to understand, extend, and maintain. It serves as a practical learning project for networking and cybersecurity fundamentals while remaining useful for basic network enumeration tasks.

---

Features

- TCP port scanning
- Common service identification
- Banner grabbing
- HTML report generation
- Modular project structure
- Simple command-line interface
- Easily configurable list of target ports

---

Project Structure

Network-scanner-and-service-analyzer/
├── main.py
├── scanner.py
├── services.py
├── report.py
├── utils.py
├── requirements.txt
├── reports/
└── README.md

---

Installation

Clone the repository:

git clone git@github.com:Jerin7575/Network-scanner-and-service-analyzer.git

Move into the project directory:

cd Network-scanner-and-service-analyzer

Install the required dependencies:

pip install -r requirements.txt

---

Usage

Run the application:

python main.py

Enter the target IP address or hostname when prompted.

---

Example Output

Target: 192.168.1.10

PORT     STATE    SERVICE
22       Open     SSH
80       Open     HTTP
443      Open     HTTPS

Generating HTML report...
Report saved successfully.

---

Generated Report

Each scan generates an HTML report containing:

- Target information
- Scan timestamp
- Open ports
- Detected services
- Service banners (when available)
- Scan summary

---

Roadmap

- Host discovery (Ping Sweep)
- Multi-threaded scanning
- UDP port scanning
- Custom port range support
- Command-line arguments
- Export results to JSON and CSV
- OS fingerprinting
- Version detection
- Progress indicator
- Scan history

---

Disclaimer

This project is intended for educational purposes and authorized security testing only. Always obtain permission before scanning systems or networks you do not own. The author assumes no responsibility for misuse of this software.

---

License

This project is licensed under the MIT License.
