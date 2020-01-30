from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class GameAddForm(FlaskForm):
    game = StringField('Game Name', validators=[DataRequired()])
    url = StringField('link')
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Create Game')


class GameDataForm(FlaskForm):
    game = StringField('Game Name', validators=[DataRequired()])
    highscore = StringField('new high score', validators=[DataRequired()])
    highscore_achiver = StringField('Who Achived the high score', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField("update High Score")
