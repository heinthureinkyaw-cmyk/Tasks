from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/round_1_scores")
def round_1():
    return render_template("index.html")

@app.route("/round_2_scores")
def round_2():
    return render_template("index.html")

@app.route("/round_3_scores")
def round_3():
    return render_template("index.html")

@app.route("/mean_scores")
def mean():
    return render_template("index.html")

@app.route("/qualified_players")
def qualifiers():
    return render_template("index.html")

app.run(port = 5000)

