from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todo_list = []


@app.route('/')
def index():
    return render_template('ToDoList.html', todo_list=todo_list)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    # get new todo item from the form data
    title = request.form['title']
    # add the new todo item to the list
    todo_list.append(title)
    # redirect back to the todo_list
    return redirect(url_for('index'))

@app.route('/remove_todo', methods=['POST'])
def remove_todo():
    # get the title of the item to remove from the form list data
    title = request.form['title']
    # remove the  item from the todo_list
    todo_list.remove(title)
    # redirect back to the index page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=500)
