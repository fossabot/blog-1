from blog import db
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    name = db.Column(db.String)
    mail = db.Column(db.String)
    content = db.Column(db.Text)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
