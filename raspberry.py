from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import board
import time
import neopixel
from random import randint
import colorsys

r = lambda : randint(0,255)
b = 1
NUM = 16
pixels = neopixel.NeoPixel(board.MOSI, NUM,brightness=b,auto_write=True)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('mouse')
def mouse(message):
    print(message)
    pixels.fill((0, 0, 0)) 
    c = [int(x * 255) for x in colorsys.hsv_to_rgb(message['y'], 1, 1)] 
    pixels[int(message['x'])] = c 

@app.route("/")
def hello_world():
    return "hello"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)