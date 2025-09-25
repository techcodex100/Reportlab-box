from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER


PAGE_WIDTH, PAGE_HEIGHT = A4
TABLE_WIDTH = 170 * mm


def make_agreement_proposal(path="agreement_proposal.pdf"):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
    )

    styles = getSampleStyleSheet()
    s_title = ParagraphStyle("Title", parent=styles["Heading1"], alignment=TA_CENTER, fontSize=16, spaceAfter=8)
    s_h1 = ParagraphStyle("H1", parent=styles["Heading2"], alignment=TA_LEFT, fontSize=12, spaceAfter=6, leading=14)
    s_normal = ParagraphStyle("Normal", parent=styles["Normal"], fontSize=10, leading=13)
    s_bold = ParagraphStyle("Bold", parent=styles["Normal"], fontSize=10, leading=13, fontName="Helvetica-Bold")
    
    # 🔹 New style for product table data (smaller font)
    s_product = ParagraphStyle("Product", parent=styles["Normal"], fontSize=9, leading=11)

    elements = []

    # 🔷 Header Row (Website | Company Name | Email)
    header_data = [
        [Paragraph("<b>Website:</b> www.shraddhaimpex.com", s_normal),
         Paragraph("<b>SHRADDHA IMPEX</b>", s_title),
         Paragraph("<b>Email:</b> info@shraddhaimpex.com", s_normal)]
    ]
    header_table = Table(header_data, colWidths=[TABLE_WIDTH/3]*3, hAlign="CENTER")
    header_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(header_table)

    # Organization line
    elements.append(Paragraph("Private Limited Company", s_normal))
    elements.append(Spacer(1, 10))

    # 🔷 Address + GST
    addr_data = [
        [Paragraph("<b>Address:</b> 308, Third Floor, Fortune Business Center, 165 R.N.T. Marg, Indore 452001, Madhya Pradesh, India", s_normal),
         Paragraph("<b>GST:</b> GSTIN1234567890", s_normal)]
    ]
    addr_table = Table(addr_data, colWidths=[TABLE_WIDTH*0.65, TABLE_WIDTH*0.35], hAlign="CENTER")
    elements.append(addr_table)
    elements.append(Spacer(1, 12))

    # 🔷 Title + Contract Info
    elements.append(Paragraph("<b>SALES CONTRACT</b>", s_title))
    contract_data = [
        [Paragraph("<b>Contract No:</b> AGR-2025-002", s_normal),
         Paragraph("<b>Date:</b> 26-09-2025", s_normal)]
    ]
    contract_table = Table(contract_data, colWidths=[TABLE_WIDTH/2, TABLE_WIDTH/2], hAlign="CENTER")
    elements.append(contract_table)
    elements.append(Spacer(1, 16))

    # 🔷 Parties (Seller | Consignee | Notify Party)
    parties_data = [
        [Paragraph("<b>SELLER</b><br/>Shraddha Impex<br/>308, Third Floor, Fortune Business Center<br/>165 R.N.T. Marg<br/>Indore - 452001, Madhya Pradesh, India<br/>Tel: (+91) 731 2515151<br/>Email: info@shraddhaimpex.com", s_normal),
         Paragraph("<b>CONSIGNEE</b><br/>Smart Company Pte Ltd<br/>25 International Business Park<br/>Singapore - 609916<br/>Tel: (+65) 6222 1234<br/>Email: contact@smartcompany.sg", s_normal),
         Paragraph("<b>NOTIFY PARTY</b><br/>Global Trade Associates<br/>7th Floor, Skyline Towers<br/>Colombo 03, Sri Lanka<br/>Tel: (+94) 11 2345678<br/>Email: notify@globaltrade.lk", s_normal)]
    ]
    parties_table = Table(parties_data, colWidths=[TABLE_WIDTH/3]*3, hAlign="CENTER")
    parties_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    elements.append(parties_table)
    elements.append(Spacer(1, 16))

    # 🔷 Product Table
    product_data = [
        [Paragraph("<b>Product</b>", s_bold),
         Paragraph("<b>Quantity</b>", s_bold),
         Paragraph("<b>Price (CIF)</b>", s_bold),
         Paragraph("<b>Amount (CIF)</b>", s_bold)],
        [Paragraph("Raw Cane Sugar - ICUMSA 45", s_product),
         Paragraph("5,000 MT", s_product),
         Paragraph("USD 460 per MT (CIF, Colombo)", s_product),
         Paragraph("USD 2,300,000", s_product)]
    ]
    prod_table = Table(product_data, colWidths=[TABLE_WIDTH*0.35, TABLE_WIDTH*0.15, TABLE_WIDTH*0.25, TABLE_WIDTH*0.25], hAlign="CENTER")
    prod_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(prod_table)
    elements.append(Spacer(1, 15))

    # 🔷 Shipment & Payment Details
    shipment_data = [
        ["Packing", "50 Kg PP Bags with Inner Liner"],
        ["Loading Port", "Mundra Port, Gujarat, India"],
        ["Destination Port", "Colombo Port, Sri Lanka"],
        ["Shipment", "October - November 2025"],
        ["Seller’s Bank", "State Bank of India, Indore Branch"],
        ["Account No.", "123456789012"],
        ["Documents", "Commercial Invoice, Packing List, Bill of Lading, Certificate of Origin"],
        ["Payment Terms", "100% LC at Sight"],
    ]
    shipment_table = Table(shipment_data, colWidths=[TABLE_WIDTH/3, (TABLE_WIDTH*2)/3], hAlign="CENTER")
    shipment_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.lightgrey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    elements.append(shipment_table)
    elements.append(Spacer(1, 16))

    # 🔷 Arbitration
    arbitration_text = (
        "In the event of any dispute between the parties arising out of this contract, "
        "all disputes shall be settled by arbitration through a sole arbitrator appointed by M/S Shraddha Impex. "
        "The place of arbitration shall be Indore, M.P., and the laws of India shall apply."
    )
    elements.append(Paragraph("<b>Arbitration</b>", s_h1))
    elements.append(Paragraph(arbitration_text, s_normal))
    elements.append(Spacer(1, 12))

    # 🔷 Terms & Conditions
    elements.append(Paragraph("<b>Terms & Conditions</b>", s_h1))
    elements.append(Paragraph("1) In case of port congestion/skippance of vessel or any other port disturbances, the supplier or exporter will not be liable for any claim.", s_normal))
    elements.append(Paragraph("2) Quality approved at load port by independent surveyors is final and shall be acceptable by both parties. The seller will not be liable for any claim at destination port.", s_normal))
    elements.append(Spacer(1, 24))

    # 🔷 Signatures
    sign_data = [
        [Paragraph("<b>Accepted</b>", s_bold), "", ""],
        [Paragraph("For, Seller", s_normal), Paragraph("For, Consignee", s_normal), Paragraph("For, Notify Party", s_normal)],
        ["\n\n\n____________________", "\n\n\n____________________", "\n\n\n____________________"],
    ]
    sign_table = Table(sign_data, colWidths=[TABLE_WIDTH/3]*3, hAlign="CENTER")
    elements.append(sign_table)

    doc.build(elements)
    print(f"Saved Agreement Proposal PDF: {path}")


if __name__ == "__main__":
    make_agreement_proposal()
