import os

import sublime
import sublime_plugin

root = os.path.dirname(os.path.abspath(__file__)) + '/boilerplates/'

algorithm_directory = 'algorithms/'
arguments_directory = 'arguments/'
bottle_directory = 'bottle/'
django_directory = 'django/'
flask_directory = 'flask/'
full_stack_directory = 'full_stack/'
kivy_directory = 'kivy/'
general_directory = 'general/'
logging_directory = 'logging/'
pyqt5_directory = 'pyqt5/'
tests_directory = 'tests/'
tkinter_directory = 'tkinter/'
tornado_directory = 'tornado/'

class BaseFunction(sublime_plugin.TextCommand):

	def fetch(self, bp_id, directory, ext):
		return open(root + self.directory + self.bp_id + self.ext).read()

	def run(self, edit):
		code = BaseFunction.fetch(self, self.bp_id, self.directory, self.ext)
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit, region, code)
			else:
				self.view.insert(edit, region.begin(), code)

class Gitignore(BaseFunction):
	"""Generate a python focused .gitignore file"""

	bp_id = 'gitignore'
	directory = general_directory
	ext = ''

	def run(self, edit):
		BaseFunction.run(self, edit)

class BasicScript(BaseFunction):
	"""Generate code for a basic executable python script"""

	bp_id = 'basic_script'
	directory = general_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class HelloWorld(BaseFunction):
	"""Generate code to print 'Hello, World!' in python"""

	bp_id = 'hello_world'
	directory = general_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Argparse(BaseFunction):
	"""Generate code for a python script that uses the argparse library"""

	bp_id = 'argparse'
	directory = arguments_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class PyPi(BaseFunction):
	"""Generate code for a basic executable python script"""

	bp_id = 'basic_script'
	directory = general_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class BottleMinimal(BaseFunction):
	"""Generate code for a minimal Bottle application"""
	
	bp_id = 'bottle_minimal'
	directory = bottle_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class BottleTemplate(BaseFunction):
	"""Generate code for a Bottle application that uses template()"""
	
	bp_id = 'bottle_template'
	directory = bottle_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class BottleTemplateView(BaseFunction):
	"""Generate code for a Bottle application that uses @view with dict()"""
	
	bp_id = 'bottle_template_view'
	directory = bottle_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class FlaskMinimal(BaseFunction):
	"""Generate code for a minimal Flask application"""
	
	bp_id = 'flask_minimal'
	directory = flask_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class FlaskRenderTemplate(BaseFunction):
	"""Generate code for a Flask application that uses render_template()"""
	
	bp_id = 'flask_render_template'
	directory = flask_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Logging(BaseFunction):
	"""Generate code for logging with the python built-in"""
	
	bp_id = 'logging'
	directory = logging_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class LogToFile(BaseFunction):
	"""Generate code for logging to a file with the python built-in"""
	
	bp_id = 'log_to_file'
	directory = logging_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Logzero(BaseFunction):
	"""Generate code for logging with logzero"""
	
	bp_id = 'logzero'
	directory = logging_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Pytest(BaseFunction):
	"""Generate code for testing with pytest"""
	
	bp_id = 'pytest'
	directory = tests_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Tox(BaseFunction):
	"""Generate code for testing with tox"""
	
	bp_id = 'tox'
	directory = tests_directory
	ext = '.ini'

	def run(self, edit):
		BaseFunction.run(self, edit)

class Unittest(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'unittest'
	directory = tests_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterBasicWindow(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_basic_window'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterBasicButton(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_basic_button'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterBasicButtonClick(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_basic_button_click'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterBasicInput(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_basic_input'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterBasicLabel(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_basic_label'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterCheckbox(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_checkbox'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterCombobox(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_combobox'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterFileDialog(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_file_dialog'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterMessagebox(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_messagebox'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterMenubar(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_menubar'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterProgressbar(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_progressbar'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterRadioButtons(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_radio_buttons'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterRadioButtonsGet(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_radio_buttons_get'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterScrolledText(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_scrolledtext'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterSpinbox(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_spinbox'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterTabControl(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_tab_control'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TkinterWarningsErrors(BaseFunction):
	"""Generate code for testing with unittest"""
	
	bp_id = 'tkinter_warnings_errors'
	directory = tkinter_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)

class TornadoMinimal(BaseFunction):
	"""Generate code for a minimal Tornado application"""
	
	bp_id = 'tornado_minimal'
	directory = tornado_directory
	ext = '.py'

	def run(self, edit):
		BaseFunction.run(self, edit)
