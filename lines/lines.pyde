size(500, 400)
noFill()
stroke(255)

previous_x1 = 250
previous_y1 = 200
previous_x2 = random(400)
previous_y2 = random(500)

for i in range(20):
    stroke(255-10*i, 0, 0+10*i)
    line(previous_x1, previous_y1, previous_x2, previous_y2)
    previous_x1 = previous_x2
    previous_y1 = previous_y2
    previous_x2 = random(400)
    previous_y2 = random(500)
