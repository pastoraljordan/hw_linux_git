from app import myobj
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form["city"]
        flash(user)
        return redirect(url_for('home'))
    return render_template("home.html", name = name, city_names = city_names)
