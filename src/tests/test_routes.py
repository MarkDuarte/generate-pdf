import unittest
from main import create_app

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes"""
        cls.app = create_app()
        cls.app.testing = True
        cls.client = cls.app.test_client()

    def test_generate_pdf_success(self):
        """Teste para gerar PDF com dados válidos"""
        response = self.client.post('/generate-pdf', json={
            "title": "Teste PDF",
            "content": "Este é o conteúdo do PDF gerado no teste.",
            "author": "Marcos Duarte"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/pdf')

    def test_generate_pdf_missing_data(self):
        """Teste para requisição sem dados"""
        response = self.client.post('/generate-pdf', json={})

        self.assertEqual(response.status_code, 400)
        self.assertIn('Nenhum dado enviado', response.get_json().get('error', ''))

    def test_generate_pdf_invalid_method(self):
        """Teste para método inválido (GET em vez de POST)"""
        response = self.client.get('/generate-pdf')

        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()
