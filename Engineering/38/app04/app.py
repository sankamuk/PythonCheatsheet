from flask import Flask, render_template

app = Flask(__name__)
user_dict = {
    "users": [
        {
            "name": "san",
            "age": 12,
            "city": "kolkata"
        },
{
            "name": "ali",
            "age": 11,
            "city": "belmundi"
        },
        {
            "name": "dab",
            "age": 13,
            "city": "belghoria"
        }
    ]
}


@app.route("/")
def index_f():
    return render_template("index.html", user=user_dict["users"][0])
