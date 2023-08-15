import flask
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ToDo.html')

if  __name__ == '__main__':
    app.run(debug=True)