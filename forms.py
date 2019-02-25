from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired()])
    last_name= StringField('last name', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired()])
    cellphone= StringField('cell phone', validators=[DataRequired()])
    submit = SubmitField('Sign In')