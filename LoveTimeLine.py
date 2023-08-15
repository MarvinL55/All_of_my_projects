from flask import Flask, render_template
import os

app = Flask(__name__)

def get_images_files(folder_path):
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_files.append(os.path.join(folder_path, filename))
    return image_files

timeline_events = [
    {"date": "March", "image_file": get_images_files("C:\\Users\\marvi\\PycharmProjects\\pythonProject1\\templates\\Photos-001 (6)")}
]

@app.route('/')
def time():
    return render_template('TimeLine.html', events=timeline_events)

if __name__ == '__main__':
    app.run(debug=True)
