from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "Key"

users = {
    'Marvin': {
        'username': 'Marvin',
        'password': 'passwords'
    }
}

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            flash("Login successful", "success")
            return redirect(url_for("dashboard"))
        else:
            # Invalid credentials
            flash("Invalid username or password", "error")

    return render_template("login.html")

@app.route('/register', methods=["GET", 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']

        if username in users:
            # TODO: Implement email confirmation and password reset logic
            flash("Password reset email sent", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid username", 'error')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard'

if __name__ == '__main__':
    app.run(debug=True)
