import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_file
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = False

# Ensure responses aren't cached
# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_FILE_DIR"] = mkdtemp()
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///analytics.db")

#TO SEND FILE --> return send_file("filename")


@app.route("/")
def index():
    """Show main page"""
    return render_template("root_page.html", name="//")

@app.route("/toolkit")
def toolkit():
    """Show how to help page (toolkit)"""
    return render_template("toolkit.html", name="//")

@app.route("/toolkit/start_now/before_you_go")
def toolkit_start_now():
    """Show start now page (toolkit)"""
    return render_template("start_now.html", name="//")

@app.route("/toolkit/start_now/i_want_to_help")
def toolkit_help():
    """Show 'I want to help' submission page (toolkit)"""
    return render_template("help_submit.html", name="//")

@app.route("/toolkit/start_now/log_your_visit")
def toolkit_log():
    """Show 'log your visit' submission page (toolkit)"""
    return render_template("log_your_visit.html", name="//")

@app.route("/toolkit/start_now/on_the_street")
def toolkit_on():
    """Show 'on the street' page (toolkit)"""
    return render_template("on_the_street.html", name="//")

@app.route("/toolkit/start_now/after_your_visit")
def toolkit_after():
    """Show 'after your visit' page (toolkit)"""
    return render_template("after_your_visit.html", name="//")

@app.route("/toolkit/what_to_bring")
def toolkit_what_to_bring():
    """Show what to bring page (toolkit)"""
    return render_template("what_to_bring.html", name="//")

@app.route("/toolkit/how-to_videos")
def toolkit_how_to_videos():
    """Show what 'how-to videos' page (toolkit)"""
    return render_template("how-to_video.html", name="//")

@app.route("/community")
def community():
    """Show community page"""
    return render_template("community.html", name="//")


@app.route("/external_link")
def external_link():
    """Show external link page"""
    return render_template("t_external.html")

#SYS
@app.route('/favico.ico')
def favico():
    return send_file('./images/favico.ico', as_attachment=True)

#Filetransfer
@app.route("/files/<path>")
def file_transfer(path):
    """Find document in filesystem"""

    return send_file("./files/{}".format(path))

#Filetransfer
@app.route("/m_style.css")
def css_main_transfer():
    """Return main CSS"""

    return send_file("./files/m_style.css")

#ERROR
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return "404"

for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
