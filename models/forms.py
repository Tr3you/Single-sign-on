from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    correo_electronico = StringField('Correo electronico', validators = [DataRequired()])
    password = PasswordField('Contraseña',  validators = [DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Correo electronico', validators = [DataRequired()])
    password = PasswordField('Contraseña',  validators = [DataRequired()])
    name = StringField('Nombre', validators = [DataRequired()])
    last_name = StringField('Apellido', validators = [DataRequired()])
    submit = SubmitField('Sign up')