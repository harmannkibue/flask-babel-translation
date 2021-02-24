from flask import Flask, render_template, request, flash
import sqlite3
from flask_babel import Babel, gettext
import os

app = Flask(__name__)
babel = Babel(app)
app.config["SECRET_KEY"] = "HARMONIZEharmonize"
app.config["FLASK_ENV"] = "development"
app.config["DEBUG"] = "True"
app.config["LANGUAGES"] = {
    'de': 'Deutsch',
    'en': 'English'
}

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["BABEL_TRANSLATION_DIRECTORIES"] = os.path.join(base_dir, "translation")

print("The path to the translations is", app.config["BABEL_TRANSLATION_DIRECTORIES"])


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# add to you main app code
@babel.localeselector
def get_locale():
    return 'de'
    # return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    message = gettext("This is very awesome")
    flash(message)
    return render_template('index.html', posts=posts)


@app.route('/hello')
def greeting():
    print(get_locale())
    return gettext("This is very awesome")
