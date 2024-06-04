size(720, 600)
background(255)
#noStroke()
#x = 20
#for i in range(10):
#    fill(i*x, i*x, 10)
#    circle(i*40, i*40, 100)
noFill()
for i in range(30):
    strokeWeight(i/3)
    beginShape()
    curveVertex(0, i*20)
    curveVertex(0, i*20)
    curveVertex(i*24, i*30)
    curveVertex(720, i*20)
    curveVertex(720, i*20)
    endShape()
    strokeWeight(i+5/3)
    point(i*24+15, i*30+15)
        
