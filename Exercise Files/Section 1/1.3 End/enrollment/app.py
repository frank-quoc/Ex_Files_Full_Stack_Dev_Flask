from flask import flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)