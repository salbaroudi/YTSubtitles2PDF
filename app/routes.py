from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sean'}
    movs = [
        {
            'movie': "Gattaca",
            'score': '8.5'
        },
        {
            'movie': "Royal Tannenbaums",
            'score': '6.1'
        },
        {
            'movie': "For a Few Dollars More",
            'score': '8.5'
        },
        {
            'movie': "Dumb and Dumber",
            'score': '7.9'
        },
        {
            'movie': "The Big Lebowski",
            'score': '8.9'
        },        
        ]
    return render_template('index.html', title='Home', user=user,movies=movs)
    
@app.route('/help')
def help():
	return "This is the help page"

@app.route('/testkey')
def testkey():
	return app.config['SECRET_KEY']

@app.route('/faq')
def faq():
	return "This is the FAQ Page."

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
