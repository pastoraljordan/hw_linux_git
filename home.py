from flask import Flask, flash, redirect, render_template, request, session, abort
myapp_obj = Flask(__name__)

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myapp_obj.route("/")
def home():
    html_string =  f"""<html>
    <head>
    </head>
    <body>
    <h1>Welcome {name}!</h1>
    <a href="www.google.com"> not google </a>
    <ul>"""
    for city in city_names:
        html_string += f'<li>{city}</li>'
    html_string += '</ul></body></html>'
    return html_string
