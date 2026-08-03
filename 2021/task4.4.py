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
    db = connect("Task4.db")
    c = db.cursor()
    c.execute('''SELECT competitor.name, ROUND(AVG(scores.score), 2)
                FROM competitor, scores
                WHERE competitor.id = scores.id
                GROUP BY competitor.id
                ORDER BY competitor.name ASC''')
    results = c.fetchall()
    db.close()
    
    return render_template("mean.html", competitors = results)

@app.route("/qualified_players")
def qualifiers():
    db = connect("Task4.db")
    c = db.cursor()
    c.execute('''SELECT competitor.name, SUM(scores.score), SUM(scores.score) > 250
                FROM competitor, scores
                WHERE competitor.id = scores.id
                GROUP BY competitor.id
                ORDER BY SUM(scores.score) DESC ''')
    results = c.fetchall()
    db.close()
  
    return render_template("qualified.html", competitors = results)

app.run(port = 5000)

