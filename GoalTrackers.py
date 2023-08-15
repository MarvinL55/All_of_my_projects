from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_Key'  # Replace with your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goals.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('goals', lazy=True))

    def __init__(self, title, description, deadline, user_id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.user_id = user_id


@app.route('/GoalTracker', methods=['GET', 'POST'])
def goal_tracker():
    user_id = 1  # Replace with the desired user ID

    if request.method == 'POST':
        # Handle the goal submission
        title = request.form['title']
        description = request.form['description']
        deadline = request.form['deadline']

        new_goal = Goal(title=title, description=description, deadline=deadline, user_id=user_id)
        db.session.add(new_goal)
        db.session.commit()

    user = User.query.get(user_id)
    goals = user.goals

    return render_template('GoalTracker.html', goals=goals)


@app.route("/")
def home():
    return render_template("GoalTracker.html")


if __name__ == '__main__':
    app.run(debug=True, port=500)
