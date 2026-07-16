import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host, port, timeout=1):
    """
    Scan a single TCP port.

    Returns:
        (port, True)  -> if open
        (port, False) -> if closed
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))
        return port, result == 0

    except Exception:
        return port, False

    finally:
        sock.close()


def scan_host(host, ports, max_threads=100):
    """
    Scan multiple ports on a host.

    Returns:
        List of open ports.
    """

    open_ports = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(scan_port, host, port)
            for port in ports
        ]

        for future in as_completed(futures):
            port, is_open = future.result()

            if is_open:
                open_ports.append(port)

    open_ports.sort()

    return open_ports
