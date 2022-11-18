import os

from cs50 import SQL
from flask import Flask, render_template, redirect, request

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cards.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Create a route for index
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("/game")

    else:
        return render_template("/index.html")

# Create a route for game
@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":

        ids = {}
        # Get a random id from the table
        id = db.execute("SELECT id FROM card ORDER BY RANDOM() LIMIT 1")[
            0]['id']

        if id in ids:
            return redirect("/game")

        else:
            ids[id] = 1

        # Get the title frm the table
        title = db.execute("SELECT title FROM card WHERE id = ?", id)[
            0]['title']

        # Get the item from the table
        item = db.execute("SELECT item FROM card WHERE id = ?", id)[0]['item']

        # Make the title and item uniform
        title = title.upper()
        item = item.capitalize()

        return render_template("game.html", title=title, item=item)

    else:
        # Redirect again to the game
        return redirect("/game")


@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        # Access from the data given
        title = request.form.get("title")
        item = request.form.get("item")

        # Insert data into database
        db.execute("INSERT INTO card (id, title, item) VALUES(NULL, ?, ?)", title, item)

        return redirect("/insert")

    else:
        return render_template("/insert.html")


@app.route("/about")
def about():
    return render_template("/about.html")
