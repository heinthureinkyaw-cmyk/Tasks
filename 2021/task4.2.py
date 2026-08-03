from flask import *
from sqlite3 import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/round_1_scores")
def round_1():
    db = connect("Task4.db")
    c = db.cursor()
    c.execute('''SELECT competitor.name, scores.score
                FROM competitor, scores
                WHERE scores.round = 1
                AND competitor.id = scores.id
                ORDER BY scores.score DESC''')
    results = c.fetchall()
    db.close()


    return render_template("round.html", competitors = results)

@app.route("/round_2_scores")
def round_2():
    db = connect("Task4.db")
    c = db.cursor()
    c.execute('''SELECT competitor.name, scores.score
                FROM competitor, scores
                WHERE scores.round = 2
                AND competitor.id = scores.id
                ORDER BY scores.score DESC''')
    results = c.fetchall()
    db.close()


    return render_template("round.html", competitors = results)
@app.route("/round_3_scores")
def round_3():
    db = connect("Task4.db")
    c = db.cursor()
    c.execute('''SELECT competitor.name, scores.score
                FROM competitor, scores
                WHERE scores.round = 3
                AND competitor.id = scores.id
                ORDER BY scores.score DESC''')
    results = c.fetchall()
    db.close()


    return render_template("round.html", competitors = results)
@app.route("/mean_scores")
def mean():
    return render_template("index.html")

@app.route("/qualified_players")
def qualifiers():
    return render_template("index.html")

app.run(port = 5000)

