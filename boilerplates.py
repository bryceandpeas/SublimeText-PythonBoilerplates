import sublime
import sublime_plugin

class flask_minimal(sublime_plugin.TextCommand):
	#Generate Code for a minimal Flask application

	def run(self, edit):
		text  = """
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'
"""
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, text)
			else:
				self.view.insert(edit, region.begin(), text)

class flask_render_template(sublime_plugin.TextCommand):
	#Generate Code for a Flask application that uses render_template()

	def run(self, edit):
		text  = """
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
"""
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, text)
			else:
				self.view.insert(edit, region.begin(), text)