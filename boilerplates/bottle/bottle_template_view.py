from bottle import Bottle, template, run

app = Bottle()

@app.route('/')
@app.view('index')
def index():
	return dict()

run(app)