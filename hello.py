from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'webapp deez nuts lmao gotem'
def test:
    return sup

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

#use $env:FLASK_APP="hello,py" and then flask run. This is in powershell NOT terminal.
