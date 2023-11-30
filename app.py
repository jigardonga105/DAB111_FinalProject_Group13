from flask import Flask, render_template
from pathlib import Path
import sqlite3

base_path = Path.cwd()
db_name = "MCU.db"
file_path = base_path / db_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    movies = cursor.execute("SELECT * FROM movies").fetchall()


    columns_info = cursor.execute("PRAGMA table_info(movies)").fetchall()
    columns = [column[1] for column in columns_info]
    conn.close()

    return render_template("data.html", movies = movies, columns = columns)

if __name__=="__main__":
    app.run(debug=True)