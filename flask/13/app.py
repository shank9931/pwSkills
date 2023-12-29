from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client event')
def client_msg(msg):
    emit('server response', {'data': msg['data']}, broadcast=True)

@socketio.on('connect event')
def connected_msg(msg):
    emit('server response', {'data': msg['data']})

if __name__ == '__main__':
    socketio.run(app)