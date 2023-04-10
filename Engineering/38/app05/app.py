from flask import Flask, render_template, abort

app = Flask(__name__)
user_dict = {
    "users": [
        {
            "name": "san", "age": 12, "city": "kolkata"
        },
        {
            "name": "ali", "age": 11, "city": "belmundi"
        },
        {
            "name": "abb", "age": 15, "city": "raibareli"
        },
        {
            "name": "prem", "age": 10, "city": "benaras"
        },
        {
            "name": "dab", "age": 13, "city": "belghoria"
        }
    ]
}


@app.route("/user/<int:idx>")
def index_f(idx):
    try:
        return render_template("user.html",
                               user=user_dict["users"][idx],
                               current_index=idx)
    except IndexError as e:
        abort(404)


