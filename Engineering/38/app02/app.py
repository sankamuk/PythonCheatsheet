from flask import Flask  # Import

app = Flask(__name__)
page_view = 0  # Page view tracker


@app.route("/")
def index_f():
    global page_view
    page_view += 1
    return "Total views is {}".format(page_view)

