from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    """A general user capable of ranking clubs.

    :param str email: email address of user
    :param str password_hash: encrypted password for the user

    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rankings = db.relationship('Ranking', backref='author', lazy='dynamic')

    # helper method for printing
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking_jsonstr = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Ranking {}>'.format(self.ranking_jsonstr)

clubs = []
with open('club_list.json') as f:
    clubs = json.load(f)

@app.route('/')
def main():
    return "Welcome to PennClubReview!"

@app.route('/api')
def api():
    return "Welcome to the PennClubReview API!."

@app.route('/api/clubs', methods=['GET'])
def get_clubs():
    return str(clubs)

@app.route('/api/clubs', methods=['POST'])
def create_club():
    if request.json:
        club = {
            'name': request.json['name'],
            'size': request.json['size'],
        }
        clubs.append(club)
        json.dump(clubs, 'club_list.json')
        return str(clubs)

@app.route('/api/rankings', methods=['GET'])
def get_rankings():
    if len(User.query.all()) != 0:
        jennifer = User.query.get(1)

        if len(Ranking.query.all()) == 0:
            jennifer_ranking = Ranking(ranking_jsonstr=str(clubs), author=jennifer)
            db.session.add(jennifer_ranking)
            db.session.commit()

        print(str(jennifer.rankings.all()))
        return str(jennifer.rankings.all())
    # else:
    #     jennifer = User(username='jennifer')
    #     db.session.add(jennifer)
    #     db.session.commit()



@app.route('/api/rankings', methods=['POST'])
def change_rankings():
    if len(Ranking.query.all()) == 0:
        jennifer_ranking = Ranking(ranking_jsonstr=str(clubs), author=jennifer)
        db.session.add(jennifer_ranking)
        db.session.commit()
    if request.json:
        for c in clubs:
            d.update((n, request.json['size']) for n, s in d.items() if n == request.json['name'])

        return str(clubs)

@app.route('/user/<int:user_id>')
def user(user_id):
    # Do something with user_id
    pass

if __name__ == '__main__':
    app.run()
