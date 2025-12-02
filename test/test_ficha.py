import unittest
from unittest.mock import MagicMock
from app.services.ficha_service import FichaService
from app.models import Alumno, Facultad

class TestFichaService(unittest.TestCase):
    def setUp(self):
        mock_repo = MagicMock()
        alumno = Alumno()
        alumno.nro_legajo = 123
        alumno.apellido = "Pérez"
        alumno.nombre = "Juan"
        alumno.nrodocumento = "12345678"
        mock_repo.obtener_por_id.return_value = alumno
        self.service = FichaService(mock_repo)

    def test_obtener_ficha_json(self):
        ficha = self.service.obtener_ficha(1)
        self.assertEqual(ficha["nombre"], "Juan")
        self.assertEqual(ficha["nro_legajo"], 123)
        self.assertEqual(ficha["nrodocumento"], "12345678")

    def test_generar_pdf(self):
        pdf_bytes = self.service.generar_pdf(1)
        self.assertTrue(len(pdf_bytes) > 0)

if __name__ == "__main__":
    unittest.main()