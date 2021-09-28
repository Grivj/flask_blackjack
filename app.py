from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('path')
def func_name(foo):
    return render_template('expression')

if __name__ == '__main__':
    app.run(debug=True)
