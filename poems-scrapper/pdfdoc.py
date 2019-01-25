from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

def create_pdf(title, content):
    page_size = (210 * mm, 297 * mm)
    doc = SimpleDocTemplate(
        'poem.pdf',
        pagesize = page_size,
        topMargin = 50 * mm,
        leftMargin = 50 * mm
    )
    styles = getSampleStyleSheet()
    #styles.list() # List available styles
    data = []

    header = Paragraph(title, styles['Heading1'])
    data.append(header)

    for p in content:
        data.append(Paragraph(p.text.replace('\n','<br />\n').replace(u'\xa0', ''), styles['BodyText']))

    # Write the PDF
    doc.build(data)
