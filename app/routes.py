from app import app, db
from flask import render_template, flash, redirect
from app.forms import GameAddForm, GameDataForm
from app.models import Game


@app.route('/')
@app.route('/index')
def index():
    games = Game.query.all()

    return render_template('index.html', games=games)


@app.route('/create', methods=['GET', 'POST'])
def create_game():
    form = GameAddForm()
    if form.validate_on_submit():
        flash(f'creating Game {form.game.data}')
        game = Game(name=form.game.data, url=form.url.data)
        db.session.add(game)
        db.session.commit()
        return redirect('/index')

    return render_template('game.html', title='create game', form=form)


@app.route('/update', methods=['GET', 'POST'])
def update_game():
    form = GameDataForm()
    if form.validate_on_submit():
        game = Game.query.filter_by(name=form.game.data).one_or_none()
        if game is None:
            flash(f"failed to update game, game {form.game.data} does not exist")
            return redirect('/index')
        flash(f'updating Game {form.game.data}')
        game.highscore = form.highscore.data
        game.highscore_aciver = form.highscore_achiver.data
        db.session.add(game)
        db.session.commit()
        return redirect('/index')

    return render_template('game.html', title='update game', form=form)
