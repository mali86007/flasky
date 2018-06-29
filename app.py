from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)
"""
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent
"""
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
"""
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(400)
    return '<h1>Hello, %s</h1>' % user.name
"""
if __name__ == '__main__':
    app.run(debug=True)