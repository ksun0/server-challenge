# Server chlalenge :rocket:

## Installation
1. Setup virtual environment and install dependencies from `requirements.txt`
2. Setup db:
  * `flask db init`
  * `flask db migrate -m "users, rankings table"`
  * `flask db upgrade`
3. Run app.py
4. Go to base route to create jennifer user and her rankings
5. Run in shell:
  * `flask shell`
  * `from app import db, User, Ranking`
  * `jennifer = User.query.get(1)`
  * `jennifer.set_password('password')`
6. GET clubs will read in from json file, POST will update the json file
7. GET, POST rankings will read in jennifer's rankings from database

## Notes
1. Implemented users
2. TODO: request errors, assign different club lists to different users, we make jennifer global since only one user
3. password set in shell for now (since no login forms)
4. html/js views (have done a lot in the past with Django)
5. Hosting (I'm experienced with DigitalOcean droplets, AWS, and Heroku)
