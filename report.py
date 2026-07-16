from datetime import datetime
import os
from jinja2 import Environment, FileSystemLoader
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_html_report(target, results):
    """
    Generate an HTML scan report.

    Args:
        target (str): Target IP or hostname
        results (list): List of dictionaries
            [
                {
                    "port": 22,
                    "service": "SSH",
                    "banner": "OpenSSH_9.6"
                }
            ]
    """

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    html = template.render(
        target=target,
        scan_date=datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        total_ports=len(results),
        results=results
    )

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    return filename
def generate_pdf_report(target, results):
    """
    Generate a PDF scan report.
    """

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>Network Scanner Report</b>", styles["Title"]))
    elements.append(Paragraph(f"Target: {target}", styles["Normal"]))
    elements.append(
        Paragraph(
            f"Scan Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    data = [["Port", "Service", "Banner"]]

    for item in results:
        data.append([
            str(item["port"]),
            item["service"],
            item["banner"] or "-"
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ]))

    elements.append(table)

    doc.build(elements)

    return filename
