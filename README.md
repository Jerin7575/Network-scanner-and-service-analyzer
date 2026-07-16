Network Scanner & Service Analyzer

A Python-based network scanning tool that scans TCP ports, identifies common network services, performs basic banner grabbing, and generates HTML and PDF reports.

«Disclaimer: This project is intended for educational purposes and for scanning systems that you own or have explicit permission to test.»

---

Features

- Scan common TCP ports on a target host
- Multithreaded scanning for improved performance
- Identify common network services
- Perform basic banner grabbing for service detection
- Generate HTML reports
- Generate PDF reports
- Modular and easy-to-understand project structure
- Command-line interface with formatted output

---

Project Structure

network_scanner/
│
├── main.py
├── scanner.py
├── services.py
├── report.py
├── utils.py
├── requirements.txt
│
├── reports/
│
└── templates/
    └── report.html

---

Requirements

- Python 3.10 or later
- rich
- jinja2
- reportlab

Install the required packages:

pip install -r requirements.txt

---

Usage

Run the application:

python main.py

When prompted, enter the target IP address or hostname:

Enter target IP or hostname:
scanme.nmap.org

Example output:

Port    : 22
Service : SSH
Banner  : SSH-2.0-OpenSSH_9.6

Port    : 80
Service : HTTP
Banner  : HTTP/1.1 200 OK

---

Generated Reports

After each scan, the application generates:

- HTML report
- PDF report

The reports are saved in the "reports/" directory.

---

Technologies Used

- Python
- socket
- concurrent.futures
- Rich
- Jinja2
- ReportLab

---

Learning Objectives

This project demonstrates:

- Socket programming
- TCP networking
- Port scanning
- Service identification
- Banner grabbing
- Multithreading
- HTML report generation
- PDF report generation
- Modular Python application design

---

Limitations

- Scans TCP ports only.
- Uses a predefined list of common ports.
- Banner grabbing depends on the target service responding with version information.
- HTTPS services are identified by port but encrypted banners are not inspected.

---

Future Improvements

- Custom port range scanning
- Full subnet scanning
- Reverse DNS lookup
- MAC address detection for local networks
- Basic operating system fingerprinting
- CSV and JSON report export
- Command-line arguments using "argparse"
- Progress indicator during scans

---

Disclaimer

This software is provided for educational purposes only.

Only scan systems, networks, or devices that you own or have explicit authorization to test. Unauthorized scanning may violate applicable laws, organizational policies, or terms of service.

The authors and contributors assume no responsibility for any misuse of this software.
