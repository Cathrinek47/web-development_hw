from flask import Flask
app = Flask(__name__)


@app.route('/')    # связывает функцию home() с корневым URL
def home():
    return 'Hello, Flask!'


@app.route('/user/<name>')
def show_user_profile(name):
    return f'Hello, {name}!'



if __name__ == '__main__':
    app.run(debug=True)
