#!/usr/bin/env python3
"""
init flesk app
"""
from flask import Flask
from flask import render_template, g
from flask_babel import Babel
from flask import request

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


def get_user():
    """
    returns a user dictionary or None
    """
    if app.request.get("login_as"):
        return users[int(app.request.get("login_as"))]
    return None

@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user()

@app.route("/")
def index():
    """
    return page with Hello world
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
