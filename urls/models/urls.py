from ..database.db import db

class Url(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    app_url = db.Column(db.String(50))

