'''
- Criar a rota de Login e o formulário, pré-definindo uma senha e login, assim, redirecionando pra página do dashboard.
- Na página de Dashboard, conter uma lista com cada produto, marcando como vermelho aqueles que não possuem um lucro grande e verde para os que possuirem um lucro maior.
'''

from flask import render_template, redirect, request, flash, Flask, make_response, url_for
from form.forms import Login
from another_routes.table import table_route
from another_routes.form_products import form_register
from another_routes.navbar import nav_route

from database.users import db, Users

db.connect()
db.create_tables([Users])
app = Flask(__name__)

app.config['SECRET_KEY'] = '9efaec900d476ff1f3a2384a4b66d1ae'
app.register_blueprint(form_register)
app.register_blueprint(nav_route)
app.register_blueprint(table_route)

MASTER_PASSWORD = 'masterloginpassword'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    cookie_name = request.cookies.get('name')
    cookie_password = request.cookies.get('password')
    
    if not cookie_name and not cookie_password:    
        if request.method == 'POST':
                if form.validate_on_submit() and form.password.data == MASTER_PASSWORD:
                    cookie = make_response(redirect(url_for('register')))
                    cookie.set_cookie('name', form.name.data)
                    cookie.set_cookie('password', form.password.data)
                    return cookie      
                else:
                    try:
                        user = Users.get(Users.name == form.name.data)         
                        cookie = make_response(redirect(url_for('home')))
                        cookie.set_cookie('name', form.name.data)
                        cookie.set_cookie('password', form.password.data)
                        return cookie     
                    except:
                        flash('Esse usuário não existe.', 'danger')
    else:
        return redirect(url_for('home'))
    
    return render_template('login.html', form=form)


@app.route('/home', methods=['GET', 'POST'])
def home():
    cookie = request.cookies.get('name')
    cookie_password = request.cookies.get('password')
    
    if not cookie and not cookie_password:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/cadaster', methods=['GET', 'POST'])
def register():
    cookie = request.cookies.get('name')
    cookie_password = request.cookies.get('password')
    
    if not cookie and not cookie_password:
        return redirect(url_for('login'))
    
    if cookie_password != MASTER_PASSWORD:
        return redirect(url_for('home'))

    return render_template('cadastrar.html')

app.run(debug=True)