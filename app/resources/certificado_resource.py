from flask import Blueprint
certificado_bp=Blueprint('certificado', __name__)
@certificado_bp.route('certificado/{id}/pdf')
def reporte_pdf():
    pass
