import os
from flask import Flask, request, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key101061',))
app.config.from_envvar('CHRISDAW_SETTINGS', silent=True)

colors = {
        "dark blue": "#1D3557",
        "blue": "#457B9D",
        "light blue": "#A8DADC",
        "white": "#F1FAEE",
        "red": "#E63946",
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cs')
def cs():
    return render_template('cs.html')

@app.route('/theatre')
def theatre():
    return render_template('theatre.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
