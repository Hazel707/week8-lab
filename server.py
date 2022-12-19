from flask import Flask, render_template,request,redirect
from collections import namedtuple
#flask --app server.py --debug run

app=Flask(__name__)
#app=Flask(__name__,static_folder='../static')
#<link rel="stylesheet" href="/static/style.css">
Post=namedtuple('Post',['title'])
users_to_posts={
    'alice':[
        Post('greetings'),
    ],
    'bob': [
        Post('hello world'),
        Post('farewell'),
    ],
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play',methods=['GET','POST'])
def play():
    return render_template('play.html')

@app.route('/stats',methods=['GET','POST'])
def stats():
    return render_template('stats.html')

@app.route('/goodbye')
def goodbye():
    return 'cya'

@app.route('/user/<name>')
def profile(name):
    posts=users_to_posts[name]
    return render_template('profile.html', name=name)

@app.route('/game/<game_id>')
def show_game(game_id):
    return 'facts about game '+game_id

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return redirect('/users/'+ request.form['username'])
    else:
        return render_template('login.html',blah=request.method)

@app.route('/debug',methods=['GET','POST'])
def debug():
    return render_template('debug.html',request=request)

