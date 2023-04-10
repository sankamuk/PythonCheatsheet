from flask import Flask, render_template

app = Flask(__name__)
page_view = 0


@app.route("/")
def index_f():
    global page_view
    page_view += 1
    return render_template("index.html", page_views=page_view)
