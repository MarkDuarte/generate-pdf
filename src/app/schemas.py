from marshmallow import Schema, fields, ValidationError

class PdfSchema(Schema):
  title = fields.String(required=True, error_messages={"required": "O titulo é obrigatório."})
  content = fields.String(required=True, error_messages={"required": "O conteúdo é obrigatório"})
  author = fields.String(required=True, error_messages={"required": "O author é obrigatório"})

  def validate_pdf_data(data):
    schema = PdfSchema()
    try:
      schema.load()
    except ValidationError as err:
      return err.messages