"""
This is from the RealPython Tutorial Discover Flask
"""

# import Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

# create application object
app = Flask(__name__)

app.secret_key = "my precious" #should be random key

#login requiered decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
           return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to route/link the function to a url
@app.route('/')
@login_required
def home():
    #return "hello, world!"  # return a string
    return render_template("index.html") # render template

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")  # render template


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'pass':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))


# start the server with the 'run()'method
if __name__ == '__main__':
    app.run(debug=True)
