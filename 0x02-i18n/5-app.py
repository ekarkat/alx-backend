#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    user_id = request.args.get('login_as')
    return users.get(int(user_id))


@app.before_request
def before_request():
    """Bfore"""
    user = get_user()
    g.user = user


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
