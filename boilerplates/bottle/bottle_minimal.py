from bottle import Bottle, run

app = Bottle()

@app.route('/')
def index():
	return "Hello, World!"

run(app)