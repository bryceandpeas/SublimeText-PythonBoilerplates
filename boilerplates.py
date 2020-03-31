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