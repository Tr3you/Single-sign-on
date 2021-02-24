from flask import request, make_response, redirect, render_template, session, flash, Flask, url_for, session
from models.forms import LoginForm, RegisterForm
from models.user import User
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'qoNhFeWiVWO4u602pAIb'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('apps.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if (request.method == 'GET'):
        try:
            session_state = session['user_session_state']
            if(session_state == 0):
                return make_response(redirect('/'))
            else:
                context = {'login_form': login_form}
                return render_template('login.html', **context)
        except:
            context = {'login_form': login_form}
            return render_template('login.html', **context)

    elif (request.method == 'POST'):
        email = login_form.email.data
        password = login_form.password.data
        r = User.get_user(User, email, password)
        if(r[0] == 0):
            response = make_response(
                redirect(url_for('single_sign_on', url_app='/index')))
            session.clear()
            session['user_session_email'] = email
            session['user_session_state'] = 0
            return response
        else:
            flash(
                "Login failed: las credenciales que ingreso son inconrrectas o no existen")
            context = {'login_form': login_form}
            return render_template('login.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if(request.method == 'GET'):
        context = {'register_form': register_form}
        return render_template('register.html', **context)
    elif(request.method == 'POST'):
        email = register_form.email.data
        password = register_form.password.data
        name = register_form.name.data
        last_name = register_form.last_name.data
        is_siggned_in = 0
        user = User(email, password, name, last_name, is_siggned_in)
        r = user.create_user()
        if(r[0] == 0):
            flash('El usuario a sido creado exitosamente')
            return make_response(redirect(url_for('index')))
        else:
            flash('ERROR: {}'.format(r[1]))
    return render_template('register.html', register_form=register_form)


@app.route('/convertidor', methods=['GET', 'POST'])
def convertidor():
    try:
        session_state = session['user_session_state']
        if(session_state == 0):
            return render_template('convertidor.html')
        else:
            return make_response(redirect(url_for('single_sign_on', url_app='/convertidor')))
    except:
        return make_response(redirect(url_for('single_sign_on', url_app='/convertidor')))


@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    try:
        session_state = session['user_session_state']
        if(session_state == 0):
            return render_template('calculadora.html')
        else:
            return make_response(redirect(url_for('single_sign_on', url_app='/calculadora')))
    except:
        return make_response(redirect(url_for('single_sign_on', url_app='/calculadora')))


@app.route('/singleSignOn/<url_app>', methods=['GET', 'POST'])
def single_sign_on(url_app):
    try:
        session_state = session['user_session_state']
    except:
        session_state = 1

    if(session_state == 0):
        if(url_app == 'index'):
            return make_response(redirect('/'))
        else:
            return make_response(redirect(url_app))
    else:
        return make_response(redirect('/login'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return make_response(redirect('/'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.before_request
def session_management():
    session.permanent = True
