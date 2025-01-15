from io import BytesIO
from reportlab.pdfgen import canvas

class PDFGenerator:
  def __init__(self):
    self.buffer = BytesIO()

  def generate(self, title: str, content: str, author: str) -> BytesIO:
    pdf = canvas.Canvas(self.buffer)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 100, title)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 760, content)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 500, author)

    pdf.save()
    self.buffer.seek(0)

    return self.buffer