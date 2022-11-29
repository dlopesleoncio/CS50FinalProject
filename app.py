from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL

db = SQL("sqlite:///series.db")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    Nserie = db.execute("SELECT * FROM series")
    return render_template("index.html",serie=Nserie)
    
@app.route("/addserie", methods=["GET", "POST"])
def adds():
    serie =  request.form.get("series")
    db.execute("INSERT INTO series (name) VALUES(?)", serie)
    return redirect("/")

@app.route("/del", methods=["GET", "POST"])
def delete():
    serie =  request.form.get("nseries")
    query = "DELETE FROM series WHERE id = '?'".replace('?',serie)
    db.execute(query)
    return redirect("/")

@app.route("/addlink", methods=["GET", "POST"])
def alink():
    lserie =  request.form.get("serieslink")
    id =  request.form.get("idseries")
    db.execute("UPDATE series SET link = ? WHERE id = ?", lserie,id)
    #Nserie = db.execute("SELECT * FROM series")
    return redirect("/")

@app.route("/addepisode", methods=["GET", "POST"])
def addepisode():
    episode = request.form.get("episode")
    id = request.form.get("idseries")
    db.execute("UPDATE series SET ep = ? WHERE id = ?",episode,id)
    #Nserie = db.execute("SELECT * FROM series")
    return redirect("/")
