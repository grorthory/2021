def setup():
    size(400, 400)
    noStroke()
    global x, y, d, heading, x_flip, y_flip
    x=200
    y=200
    d=50
    x_flip = 1
    y_flip = 1
    heading = random(2 * PI)
    fill(random(255), random(255), random(255))

def draw():
    global x, y, d, heading, x_flip, y_flip
    if (x + d/2 or x - d/2) >= 400 or (x + d/2 or x - d/2) <= d:
        x_flip = -x_flip
        fill(random(255), random(255), random(255))
    if (y + d/2 or y - d/2) >= 400 or (y + d/2 or y - d/2) <= d:
       y_flip = -y_flip
       fill(random(255), random(255), random(255))
    circle(x, y, d)
    x+=cos(heading)*x_flip
    y+=sin(heading)*y_flip
