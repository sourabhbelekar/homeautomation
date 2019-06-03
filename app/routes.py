from app import app

@app.route('/')
@app.route('/index')
def index():
	return "haha"


@app.route('/register', methods=['POST'])
def register():
	return "Success"
