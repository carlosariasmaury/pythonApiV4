from .db import db

class OrdenMedica():
    identifier  = db.StringField(required=True, unique=True)
    status  = db.StringField(required=True)
    category  = db.StringField(required=True)
    orderDetail  = db.ListField(db.StringField(), required=True)

