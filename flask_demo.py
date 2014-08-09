from flask import Flask, render_template
app = Flask(__name__)
app = Blueprint(app)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
