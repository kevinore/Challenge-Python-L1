from app import db


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String(80))
    minimum  = db.Column(db.String(80))
    max = db.Column(db.String(80))
    average = db.Column(db.String(80))

    def __repr__(self):
        return '<Total {}>'.format(self.total)