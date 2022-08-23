from ..database.db import db


class Url(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    shortened_url = db.Column(db.String(50))
    # title = db.Column(db.String(80))
    # body = db.Column(db.String(500))
    # email = db.Column(db.String(500))

