from flask import Flask, flash, redirect, render_template, request, session, abort
myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    html_string =  f"""<html>
    <head>
    </head>
    <body>
    <h1>Welcome {name}</h1>
    <a href="https://www.google.com"> not google </a>
    <ul>"""
    for city in city_names:
        html_string += f'<li>{city}</li>'
    html_string += '</body></html>'
    return html_string
