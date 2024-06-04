size(500, 400)
#background(148, 21, 20, 100)
noStroke()

for j in range(50):
    fill(random(154, 157), random(17, 157), random(17, 148))
    initial_vertex = random(-50, 550), random(-50, 450)
    beginShape()
    curveVertex(*initial_vertex)
    curveVertex(*initial_vertex)
    for i in range(int(random(3, 10))):
        curveVertex(random(-50, 550), random(-50, 450))
    curveVertex(*initial_vertex)
    curveVertex(*initial_vertex)
    endShape()
