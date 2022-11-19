import json
from datetime import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


PLACE_PRICE = 3


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        if request.form['email'] == '':
            flash("Veuillez saisir votre email.")
        else:
            flash("Email non reconnu.")
        return render_template('index.html'), 403


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            competition_datetime = datetime.strptime(foundCompetition['date'], "%Y-%m-%d %H:%M:%S")
            if competition_datetime < datetime.now():
                flash("Cette compétition est terminée, veuillez en choisir une autre")
                return render_template('welcome.html', club=foundClub, competitions=competitions), 403
            else:
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
    except IndexError:
        return render_template('index.html'), 403


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    total_cost = placesRequired * PLACE_PRICE
    if placesRequired > int(competition['numberOfPlaces']):
        flash(f"Pas assez de places disponibles pour la compétition {competition['name']}.")
        flash(f"Demandées: {placesRequired}. Disponibles: {competition['numberOfPlaces']}.")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    if placesRequired > 12:
        flash("Vous ne pouvez pas réserver plus de 12 places sur une compétition")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    if total_cost > int(club['points']):
        flash("Votre nombre de points est insuffisant")
        return render_template('welcome.html', club=club, competitions=competitions), 400
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    club['points'] = int(club['points']) - total_cost
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))