from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

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


@app.route("/")
def home_f():
    return render_template("users.html", users=user_dict["users"])


@app.route("/user/<int:idx>")
def index_f(idx):
    try:
        return render_template("user.html",
                               user=user_dict["users"][idx],
                               current_index=idx,
                               max_index=(len(user_dict["users"]) - 1))
    except IndexError as e:
        abort(404)


@app.route("/api/user/<int:idx>")
def rest_user(idx):
    if 0 <= idx < len(user_dict["users"]):
        return jsonify(user_dict["users"][idx])
    else:
        return jsonify(dict())


@app.route("/api/users")
def rest_users():
    return jsonify(user_dict)


@app.route("/select", methods=["GET", "POST"])
def select_user():
    if request.method == "POST":
        return redirect(url_for("index_f", idx=request.form["index"]))
    else:
        return render_template("select_user.html")


@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user_dict["users"].append({
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "city": request.form["city"]
        })
        return redirect(url_for("index_f", idx=len(user_dict["users"]) - 1))
    else:
        return render_template("new_user.html")


@app.route("/delete/<int:index>", methods=["GET", "POST"])
def drop_user(index):
    if request.method == "POST":
        user_dict["users"].pop(index)
        return redirect(url_for("home_f"))
    else:
        return render_template("drop_user.html",
                               user=user_dict["users"][index]
                               )
