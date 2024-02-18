from flask import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired 

class RegisterForm(FlaskForm):
    username=StringField(label='User Name:',validators=[Length(min=2,max=30),DataRequired()])
    email=StringField(label='Email Address:',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    submit=SubmitField(label='Create Account')