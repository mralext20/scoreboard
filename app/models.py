from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True, unique=True)
    url = db.Column(db.String(), index=True)
    highscore = db.Column(db.String())
    highscore_aciver = db.Column(db.String())

    def __repr__(self):
        return '<Game {}>'.format(self.name)
