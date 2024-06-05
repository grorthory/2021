size(720, 600)
background(255)
#noStroke()
#x = 20
#for i in range(10):
#    fill(i*x, i*x, 10)
#    circle(i*40, i*40, 100)
noStroke()
for i in range(30):
    fill(random(0, 255), random(0, 255), random(0, 255), 50)
    beginShape()
    curveVertex(0, i*20)
    curveVertex(0, i*20)
    curveVertex(random(0, 720), random(0, 600))
    curveVertex(720, i*20)
    curveVertex(0, i*20)
    curveVertex(0, i*20)
    endShape()
        
