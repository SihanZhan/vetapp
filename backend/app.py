from flask import Flask 

app = Flask(__name__)


@app.route('/')
def home():
    return "Here is the Home Page"

@app.route('/about')
def about():
    return "This is the About Page"


@app.route('/Pizza')
def pizza():
    return "This is the Pizza Page"

@app.route('/user/<username>')
def user_profile(username):
    return f'User {username}'

if __name__ == "__main__":
    app.run(debug=True)