import socket

# Common port-to-service mapping
COMMON_SERVICES = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "SMB",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    1723: "PPTP",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}


def get_service_name(port):
    """
    Return the common service name for a port.
    """
    return COMMON_SERVICES.get(port, "Unknown")


def grab_banner(host, port, timeout=2):
    """
    Attempt to grab a service banner.
    Returns None if no banner is received.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))

        # Trigger a response for HTTP servers
        if port in (80, 8080, 8000):
            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

        elif port in (443, 8443):
            # HTTPS is encrypted; skip banner grabbing
            sock.close()
            return None

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner.replace("\r", " ").replace("\n", " ")

    except Exception:
        pass

    return None
