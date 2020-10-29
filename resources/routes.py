from .client import ClientsApi, ClientApi
from .orden_medica import OrdenesMedicasApi, OrdenMedicaApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')
    api.add_resource(OrdenesMedicasApi, '/api/OrdenesMedicas')
    api.add_resource(OrdenMedicaApi, '/api/OrdenMedica/<id>')

