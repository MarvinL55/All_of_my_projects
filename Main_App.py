from flask import Flask
from Web_Apps import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

app.route("/")
def home():
    return "This is the home"


if __name__ == '__main__':
    app.run(debug=True)