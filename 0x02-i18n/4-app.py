#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# def get_locale():
#     """get local"""
#     locale = request.args.get('locale')
#     if locale in app.config['LANGUAGES']:
#         return locale
#     return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_pyfile('babel.cfg')
# babel = Babel(app, locale_selector=get_locale)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get local"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """default route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
