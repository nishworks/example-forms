from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms import validators
from wtforms.validators import Optional, InputRequired, DataRequired

class InputForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    states = SelectField("US States", validate_choice=False)
    territory = SelectField("Is Territory?", choices=["Unknown", "Yes", "No"], default="Unknown", validators=[InputRequired()])
    submit = SubmitField("Add State", validators=[Optional()])
