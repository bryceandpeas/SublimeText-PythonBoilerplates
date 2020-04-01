import os

import sublime
import sublime_plugin

root = os.path.dirname(os.path.abspath(__file__)) + '/boilerplates/'
general_directory = 'general/'

flask_directory = 'flask/'


class BaseFunction(sublime_plugin.TextCommand):
	boilerplate_id = ''
	directory = ''
	extension = ''

	@staticmethod
	def fetch(self, boilerplate_id, directory, extension):
		return open(root + self.directory + self.boilerplate_id + self.extension).read()

	@staticmethod
	def run(self, edit):
		code = BaseFunction.fetch(self, self.boilerplate_id, self.directory, self.extension)
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, code)
			else:
				self.view.insert(edit, region.begin(), code)

class BasicScript(BaseFunction):
	"""Generate code for a basic executable python script"""

	boilerplate_id = 'basic_script'
	directory = general_directory
	extension = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Gitignore(BaseFunction):
	"""Generate a python focused .gitignore file"""

	boilerplate_id = 'gitignore'
	directory = general_directory
	extension = ''

	def run(self, edit):
		BaseFunction.run(self, edit)

class HelloWorld(BaseFunction):
	"""Generate code to print 'Hello, World!' in python"""

	boilerplate_id = 'hello_world'
	directory = general_directory
	extension = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class FlaskMinimal(BaseFunction):
	"""Generate code for a minimal Flask application"""
	
	boilerplate_id = 'flask_minimal'
	directory = flask_directory
	extension = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class FlaskRenderTemplate(BaseFunction):
	"""Generate code for a Flask application that uses render_template()"""
	
	boilerplate_id = 'flask_render_template'
	directory = flask_directory
	extension = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)
