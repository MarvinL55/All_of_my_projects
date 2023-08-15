import flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
items = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("Wants.html", items=items)

@app.route('/add_wants', methods=['POST'])
def add_list():
    new_item = request.form['item']
    if new_item:
        items.append(new_item)
    return redirect(url_for('home'))

@app.route('/remove_wants', methods=['POST'])
def remove_wants():
    # get the title of the item to remove from the form list data
    new_item = request.form['item']
    # remove the  item from the todo_list
    items.remove(new_item)
    # redirect back to the index page
    return redirect(url_for('home'))

if __name__ == "__main__":
   app.run(debug=True)
