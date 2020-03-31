import os

import sublime
import sublime_plugin

root = os.path.dirname(os.path.abspath(__file__)) + '/boilerplates/'

class flask_minimal(sublime_plugin.TextCommand):
	#Generate Code for a minimal Flask application
	boilerplate_id = 'flask_minimal'
	flask_directory = 'flask/'

	def fetch(self, boilerplate_id, flask_directory):
		code = open(root + flask_directory + boilerplate_id + '.py').read()
		return code

	def run(self, edit):
		code = self.fetch('flask_minimal', 'flask/')
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, code)
			else:
				self.view.insert(edit, region.begin(), code)

class flask_render_template(sublime_plugin.TextCommand):
	#Generate Code for a Flask application that uses render_template()
	boilerplate_id = 'flask_render_template'
	flask_directory = 'flask/'

	def fetch(self, boilerplate_id, flask_directory):
		code = open(root + flask_directory + boilerplate_id + '.py').read()
		return code

	def run(self, edit):
		code = self.fetch('flask_render_template', 'flask/')
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, code)
			else:
				self.view.insert(edit, region.begin(), code)