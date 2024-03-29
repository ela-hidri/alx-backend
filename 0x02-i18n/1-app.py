#!/usr/bin/env python3
"""
init flesk app
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


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


@app.route("/")
def index():
    """
    return page with Hello world
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
