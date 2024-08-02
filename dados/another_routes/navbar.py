from flask import Blueprint, render_template

nav_route = Blueprint('nav', __name__)

@nav_route.route('/nav')
def nav():
    return render_template('navbar.html')