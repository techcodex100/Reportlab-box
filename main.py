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
TABLE_WIDTH = 170 * mm   # common fixed width for all tables

def make_proposal(path="generated_proposal.pdf"):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
    )

    styles = getSampleStyleSheet()
    s_title = ParagraphStyle("Title", parent=styles["Heading1"], alignment=TA_CENTER, fontSize=18, spaceAfter=8)
    s_h1 = ParagraphStyle("H1", parent=styles["Heading2"], alignment=TA_LEFT, fontSize=12, spaceAfter=6, leading=14)
    s_normal = ParagraphStyle("Normal", parent=styles["Normal"], fontSize=10, leading=13)
    s_bold = ParagraphStyle("Bold", parent=styles["Normal"], fontSize=10, leading=13, fontName="Helvetica-Bold")

    elements = []

    # Header / Title
    elements.append(Paragraph("SALES CONTRACT PROPOSAL", s_title))
    elements.append(Spacer(1, 6))

    # --- Top Info Section ---
    top_data = [
        [Paragraph("<b>Website</b>", s_bold), "www.vidhi.com",
         Paragraph("<b>Company</b>", s_bold), "SHRADDHA IMPEX"],
        [Paragraph("<b>Email</b>", s_bold), "vidhi@gmail.com",
         Paragraph("<b>Organization</b>", s_bold), "Government organization"],
        [Paragraph("<b>Address</b>", s_bold), "dfghjkohgfdsdfrtyu",
         Paragraph("<b>GST</b>", s_bold), "567"],
        [Paragraph("<b>Contract No.</b>", s_bold), "34",
         Paragraph("<b>Date</b>", s_bold), "20-11-2021"],
    ]
    info_table = Table(top_data,
                       colWidths=[TABLE_WIDTH/4]*4,
                       hAlign="CENTER")
    info_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.lightgrey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),
        ("BACKGROUND", (2,0), (2,-1), colors.whitesmoke),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 12))

    # --- Parties Section ---
    elements.append(Paragraph("<b>Parties</b>", s_h1))
    parties_data = [
        [Paragraph("<b>Seller</b>", s_bold), "Shraddha Impex, Indore"],
        [Paragraph("<b>Consignee</b>", s_bold), "third floor it park indore"],
        [Paragraph("<b>Notify Party 1</b>", s_bold), "smart company bhawar kuaa"],
        [Paragraph("<b>Notify Party 2</b>", s_bold), "it paark indore nanga nagar"],
    ]
    parties_table = Table(parties_data,
                          colWidths=[TABLE_WIDTH/3, (TABLE_WIDTH*2)/3],
                          hAlign="CENTER")
    parties_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.lightgrey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(parties_table)
    elements.append(Spacer(1, 12))

    # --- Products Section ---
    elements.append(Paragraph("<b>Products</b>", s_h1))
    product_table_data = [
        [Paragraph("<b>Product</b>", s_bold),
         Paragraph("<b>Quantity</b>", s_bold),
         Paragraph("<b>Price (CIF, Colombo)</b>", s_bold),
         Paragraph("<b>Amount (CIF)</b>", s_bold)],
        ["Raw Sugar", "567", "89", "2345"],
    ]
    products_table = Table(product_table_data,
                           colWidths=[TABLE_WIDTH*0.35,
                                      TABLE_WIDTH*0.15,
                                      TABLE_WIDTH*0.25,
                                      TABLE_WIDTH*0.25],
                           hAlign="CENTER")
    products_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f2f2f2")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(products_table)
    elements.append(Spacer(1, 12))

    # --- Shipment & Payment Section ---
    elements.append(Paragraph("<b>Shipment & Payment Details</b>", s_h1))
    shipment_rows = [
        [Paragraph("<b>Packing</b>", s_bold), "4"],
        [Paragraph("<b>Loading Port</b>", s_bold), "India"],
        [Paragraph("<b>Destination Port</b>", s_bold), "Singapore"],
        [Paragraph("<b>Shipment</b>", s_bold), "45678"],
        [Paragraph("<b>Seller’s Bank</b>", s_bold), "fghjkl"],
        [Paragraph("<b>Account No.</b>", s_bold), "45678"],
        [Paragraph("<b>Documents</b>", s_bold), "4567890plknbvcvbhjkl;"],
        [Paragraph("<b>Payment Terms</b>", s_bold), "cvbhjklokjhgfdfrtyuik"],
    ]
    ship_table = Table(shipment_rows,
                       colWidths=[TABLE_WIDTH/3, (TABLE_WIDTH*2)/3],
                       hAlign="CENTER")
    ship_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.lightgrey),
        ("BACKGROUND", (0,0), (0,-1), colors.whitesmoke),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(ship_table)
    elements.append(Spacer(1, 12))

    # --- Arbitration Section ---
    elements.append(Paragraph("<b>Arbitration</b>", s_h1))
    arbitration_text = (
        "In the event of any dispute between the parties arising out of this contract, all disputes shall be "
        "settled by the way of arbitration through a sole arbitration to be appointed by M/S Shraddha Impex. "
        "The place of arbitration shall be in Indore, M.P. and the laws of India with regards to arbitration shall "
        "be applicable."
    )
    elements.append(Paragraph(arbitration_text, s_normal))
    elements.append(Spacer(1, 12))

    # --- Terms & Conditions Section ---
    elements.append(Paragraph("<b>Terms & Conditions</b>", s_h1))
    t1 = "1) In case of port congestion/skippance of vessel or any other port related disturbances, supplier or exporter will not be liable for any claim."
    t2 = "2) Quality approved at load port by independent surveyors is final, and to be acceptable by both the parties and the seller will not be liable for any claim at destination port."
    elements.append(Paragraph(t1, s_normal))
    elements.append(Paragraph(t2, s_normal))
    elements.append(Spacer(1, 24))

    # --- Signatures Section ---
    sign_data = [
        [Paragraph("<b>Accepted</b>", s_bold), "", ""],
        [Paragraph("<b>For, Seller</b>", s_normal),
         Paragraph("<b>For, Consignee</b>", s_normal),
         Paragraph("<b>For, Notify Party</b>", s_normal)],
        ["\n\n\n____________________",
         "\n\n\n____________________",
         "\n\n\n____________________"],
    ]
    sign_table = Table(sign_data,
                       colWidths=[TABLE_WIDTH/3]*3,
                       hAlign="CENTER")
    sign_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(sign_table)

    # Build document
    doc.build(elements)
    print(f"Saved PDF to: {path}")

if __name__ == "__main__":
    make_proposal()
