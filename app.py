from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import WordVectors
import NounOfTheDay
import NounList
import Guess
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'supersecretsessionkey'
db = SQLAlchemy(app)


# initialize scheduler
scheduler = BackgroundScheduler()

currentBestGuess = None
token_noun = None

class GuessList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Guess %r>' % self.id

class VectorsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    vector_val = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Vector %r>' % self.id
        

def job():
    token_noun = NounOfTheDay.noun
    print(token_noun)
    try:
        db.session.query(GuessList).delete()
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting db"

scheduler.add_job(func=job, trigger="cron", hour=0)
scheduler.start()

@app.route('/', methods=['POST', 'GET'])
def index():
    global token_noun
    global currentBestGuess

    if request.method == 'POST':
        guess_content = request.form['content']
        new_guess = GuessList(content=guess_content)
        guess = Guess.Guess(guess_content)
        if guess.isNoun:
            if guess.isInVector:
                if currentBestGuess == None:
                    currentBestGuess = guess
                if currentBestGuess.vectorIndex > guess.vectorIndex:
                    currentBestGuess = guess
                if currentBestGuess.vectorIndex == 0:
                    return redirect('/game_won')
                try:
                    db.session.add(new_guess)
                    db.session.commit()
                    return redirect('/')
                except:
                    return 'failed to commit'
            else:
                return "not in word list!"
        else:
            return "guess is not a noun!"
    else:
        guesses = GuessList.query.all()
        return render_template('index.html', guesses=guesses, currentBestGuess=currentBestGuess)

@app.route('/delete/')
def delete():
    try:
        db.session.query(GuessList).delete()
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting db"

@app.route('/game_won')
def game_won_landing():
    guesses = GuessList.query.all()
    return render_template('game_won.html', guesses=guesses, currentBestGuess=currentBestGuess)

if __name__ == "__main__":
    app.run(debug=True)