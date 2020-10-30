from flask import Response, request
from database.models import OrdenMedica
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class OrdenesMedicasApi(Resource):
    def get(self):
        OrdenesMedicas = OrdenMedica.objects().to_json()
        return Response(OrdenesMedicas, mimetype="application/json", status=200)

    #@jwt_required
    def post(self):
        body = request.get_json()
        OrdenMedica = OrdenMedica(**body).save()
        id = OrdenMedica.id
        return {'id': str(id)}, 200


class OrdenMedicaApi(Resource):
    #@jwt_required
    def put(self, id):
        body = request.get_json()
        OrdenMedica.objects.get(id=id).update(**body)
        return '', 200

    #@jwt_required
    def delete(self, id):
        """Deletes Orden Medica"""
        OrdenMedica = OrdenMedica.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        try:
            OrdenMedica = OrdenMedica.objects.get(id=id).to_json()
            return Response(OrdenMedica, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
