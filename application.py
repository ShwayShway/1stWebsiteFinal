from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("x") or not request.form.get("o") or not request.form.get("p") or not request.form.get("q"):
        return render_template("failure.html")
    file = open("studentregistrants.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("x"), request.form.get("o"), request.form.get("p"), request.form.get("q")))
    file.close()
    return render_template("success.html")