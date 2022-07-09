from flask import Flask

app = Flask(__name__)

@app.route('/')
def subscribe():
    return "Leave a like and a subscribe"
