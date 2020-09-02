from flask import flask

app = Flask(__init__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, Earth!</h1>"

if __name__ == '__main__':
    app.run(debug=True)