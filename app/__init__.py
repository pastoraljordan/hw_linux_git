from flask import Flask, flash, redirect, render_template, request, session, abort

myapp_obj = Flask(__name__)
myapp_obj.secret_key = 'cmpe131'
from app import routes
