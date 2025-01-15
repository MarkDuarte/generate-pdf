from flask import send_file
from core.pdf_genarator import PDFGenerator

class PDFService:
  def create_pdf(self, data: dict):
    title = data.get('title', 'Titulo padrão')
    content = data.get('content', 'Conteúdo padrão')
    author = data.get('author', 'Autor do PDF')

    pdf_generator = PDFGenerator()
    pdf_file = pdf_generator.generate(title, content, author)

    return send_file(
      pdf_file,
      mimetype='application/pdf',
      as_attachment=True,
      download_name='document.pdf'
    )