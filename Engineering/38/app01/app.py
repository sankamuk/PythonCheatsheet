from flask import Flask  # Import

app = Flask(__name__)  # Use constructor to create Flask application


@app.route("/")  # Decorator to convert to a Flask View
def index_f():  # Plain old python function returning result from View
    return "Hello World!"
