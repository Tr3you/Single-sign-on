from flask import request, make_response, redirect, render_template, session, flash, Flask
from app.models.forms import LoginForm, RegisterForm
from app.models.user import User
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'qoNhFeWiVWO4u602pAIb'

@app.route('/')
def index():
    response = make_response(redirect('/apps'))
    return response

@app.route('/apps')
def hello():
    return render_template('apps.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if (request.method == 'GET'):
        context = {'login_form' : login_form}
        return render_template('login.html', **context)

    elif (request.method == 'POST'):
        email = login_form.email.data
        password = login_form.password.data
        context = {
            'correo' : email,
            'password' : password,
            'login_form' : login_form
        }
        flash('Login exitoso!')
        return render_template ('login.html', **context)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if(request.method == 'GET'):
        context = {'register_form' : register_form}
        return render_template('register.html', **context)
    elif(request.method=='POST'):
        email = register_form.email.data
        password = register_form.password.data
        name = register_form.name.data
        last_name = register_form.last_name.data
        is_siggned_in = 0
        user = User(email, password, name, last_name, is_siggned_in)
        r, message = user.create_user()

        if(r == 0):
            flash('El usuario a sido creado exitosamente')
        else:
            flash('ERROR: {}'.format(message))
    return render_template('register.html', register_form = register_form)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


