from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('mouse')
def mouse(message):
    print(message)

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)