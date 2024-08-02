from flask import Blueprint, render_template, request, redirect, url_for
from form.forms import User_Register
from database.users import Users

form_register = Blueprint('register', __name__)

@form_register.route('/register', methods=['GET', 'POST'])
def register():
    form = User_Register()
    print(request.method)
    
    
    
    if request.method == 'POST':
        if form.validate_on_submit():
            print('yes')
            Users.create(name=form.name.data, password=form.password.data)  
            return redirect(url_for('register'))
            
    return render_template('add_clients.html', form=form)