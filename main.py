from utils import print_banner, info, success
from scanner import scan_host
from services import get_service_name, grab_banner
from report import generate_html_report,generate_pdf_report

COMMON_PORTS = [
    20, 21, 22, 23, 25,
    53, 67, 68, 69,
    80, 110, 111, 123,
    135, 137, 138, 139,
    143, 161, 389, 443,
    445, 587, 993, 995,
    1433, 1521, 1723,
    2049, 3306, 3389,
    5432, 5900, 6379,
    8080, 8443
]


def main():
    print_banner()

    target = input("Enter target IP or hostname: ").strip()

    info(f"Scanning {target}...")
    info(f"Scanning {len(COMMON_PORTS)} common ports...\n")

    open_ports = scan_host(target, COMMON_PORTS)

    if not open_ports:
        print("\nNo open ports found.")
        return

    success("Open Ports Found:\n")

    results = []

    for port in open_ports:
        service = get_service_name(port)
        banner = grab_banner(target, port)

        results.append({
            "port": port,
            "service": service,
            "banner": banner
        })

        print(f"\nPort    : {port}")
        print(f"Service : {service}")

        if banner:
            print(f"Banner  : {banner}")

    html_report = generate_html_report(target, results)
    pdf_report = generate_pdf_report(target, results)

    success(f"\nHTML report saved to: {html_report}")
    success(f"PDF report saved to: {pdf_report}")


if __name__ == "__main__":
    main()
