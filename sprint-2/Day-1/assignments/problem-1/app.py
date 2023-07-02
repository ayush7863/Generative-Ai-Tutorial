from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome_message():
    return "Welcome !"

@app.route('/greet/<name>')
def greet_message(name):
    return f"Hello {name}!"

@app.route('/farewell/<name>')
def goodbye_message(name):
    return f"Goodbye {name}!"


if __name__ == '__main__':
    app.run(port=8080)
