background(0, 100, 100)
size(600, 600)
noStroke()
for i in range(20):
    fill(255, 255, 0, 100-i*10)
    ellipse(300, 300, 10*i*i, 50*i)
    
save("circles.png")
