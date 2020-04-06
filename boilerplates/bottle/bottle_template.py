import os

from bottle import Bottle, run, template, TEMPLATE_PATH

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))

app = Bottle()

@app.route('/')
def index():
	return template('index')

run(app)