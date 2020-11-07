from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# ...

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cory'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautfull day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember+me{}'.format(form, username, data, form.remember_me,data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)