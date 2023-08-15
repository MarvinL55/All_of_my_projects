from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("base.html", notes=notes)

@app.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note = {'title': title, 'content': content}
        notes.append(note)
        return redirect(url_for('home'))
    return render_template('create_note.html')

@app.route('/note/<int:note_id>')
def note_detail(note_id):
    note = notes[note_id]
    return render_template('note_details.html', note=note)

@app.route('/note/<int:note_id>/edit', methods=['GET', 'POST'])
def edit_note(note_id):
    note = notes[note_id]
    if request.method == 'POST':
        note['title'] = request.form['title']
        note['content'] = request.form['content']
        return redirect(url_for('note_detail', note_id=note_id))
    return render_template('edit_note.html', note=note)

@app.route('/note/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    notes.pop(note_id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
