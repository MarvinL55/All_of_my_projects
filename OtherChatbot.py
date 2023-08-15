import socketio
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['Key'] = 'secret!'
socketio = SocketIO(app)

user = {}

@app.route('/')
def index():
   return render_template('chatbot.html')

@socketio.on('connect')
def on_connect():
    print("User connected")

@socketio.on('disconnect')
def on_disconnect():
    print("user had been disconnected")

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']

    if username in user.values():
        emit('Username error', {'message': 'username is already taken'})
    else:
        user[request.sid] = username
        join_room(room)
        emit('join message', {'message': username + "has joined the room."}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['zoom']

    del user[request.sid]
    leave_room(room)
    emit('leave message', {'message': username + ' has left the room.'},room=room)

@socketio.on('send message')
def on_send_message(data):
    message = data['message']
    username = user[request.sid]
    room=data['room']
    emit('new message', {'username': username, 'message': message}, room=room)

def handle_message(message):
    print('received message ' + message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)