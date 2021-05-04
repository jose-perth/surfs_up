from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/greet/')
def greet():
    return 'Top of the morning to you!'