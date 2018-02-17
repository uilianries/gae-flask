from main import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    url = db.Column(db.String)
    comments = db.Column(db.String)

    def __init__(self, name, email, url="", comments=""):
        self.name = name
        self.email = email
        self.url = url
        self.comments = comments

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
