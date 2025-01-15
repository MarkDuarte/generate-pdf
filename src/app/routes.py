from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from services.pdf_service import PDFService
from app.schemas import PdfSchema

routes = Blueprint('routes', __name__)

@routes.route('/generate-pdf', methods=['POST'])
def generate_pdf():
  try:
    data = request.get_json()

    if not data:
      return jsonify({"error": "Nenhum dado enviado"}), 400
    
    schema = PdfSchema()
    validated_data = schema.load(data)
    
    pdf_service = PDFService()
    pdf_file = pdf_service.create_pdf(validated_data)

    return pdf_file
  
  except ValidationError as e:
    return jsonify({"error": e.messages}), 500
  
  except Exception as e:
    return jsonify({"error": f"Error ao gerar PDF: {str(e)}"}), 500
  
def register_routes(app):
  app.register_blueprint(routes)