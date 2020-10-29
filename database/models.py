from .db import db

class Client(db.Document):
    doc_id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    preexistence = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')
    
class OrdenMedica():
    identifier  = db.StringField(required=True, unique=True)
    status  = db.StringField(required=True)
    category  = db.StringField(required=True)
    orderDetail  = db.ListField(db.StringField(), required=True)

