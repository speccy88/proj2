var socket;

function setup() {
  createCanvas(1200, 600);
  background(51);

  socket = io("http://192.168.1.16:5000");
}

function draw() { 
  noStroke();
  background(51);
  fill(255);
  ellipse(mouseX,mouseY,5,5);
  var data = {
    x: map(mouseX, 0, width, 15, 0),
    y: map(mouseY, 0, height, 0, 1)
  }
  socket.emit('mouse', data);
}
