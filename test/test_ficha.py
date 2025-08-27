import unittest
from unittest.mock import MagicMock
from app.services.ficha_service import FichaService
from app.models import Alumno, Facultad

class TestFichaService(unittest.TestCase):
    def setUp(self):
        mock_repo = MagicMock()
        facultad = Facultad(nombre="Facultad de Ingeniería")
        alumno = Alumno(legajo="A123", apellido="Pérez", nombre="Juan", dni="12345678", facultad=facultad)
        mock_repo.obtener_por_id.return_value = alumno
        self.service = FichaService(mock_repo)

    def test_obtener_ficha_json(self):
        ficha = self.service.obtener_ficha(1)
        self.assertEqual(ficha["nombre"], "Juan")
        self.assertEqual(ficha["facultad"], "Facultad de Ingeniería")

    def test_generar_pdf(self):
        pdf_bytes = self.service.generar_pdf(1)
        self.assertTrue(len(pdf_bytes) > 0)

if __name__ == "__main__":
    unittest.main()