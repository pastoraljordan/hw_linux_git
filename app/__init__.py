from flask import Flask, flash, redirect, render_template, request, session, abort

myobj = Flask(__name__)
myobj.secret_key = 'cmpe131'
from app import routes
