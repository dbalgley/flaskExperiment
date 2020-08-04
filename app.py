from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    print("Ah heck")
    return "I can't believe you've done this."

@app.route("/home")
def hello():
    return "Get lost"