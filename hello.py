from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Gil!'

#use $env:FLASK_APP="hello,py" and then flask run. This is in powershell NOT terminal.
