size(600, 600)
background(255)
fill(225, 0)
def makeTriangle(x1, y1a, y1b, x2, y2, x3, y3):
    for i in range(10):
        y1a = y1a - 10*i
        triangle(x1, y1a, x2, y2, x3, y3)
        y1b = y1b + 10*i
        triangle(x1, y1b, x2, y2, x3, y3)
        #y1 = y1 - 10*i

#change k to change the horizontal distance between triangles
#cool settings: 75, 30, 5, 15, 112.5, 37.5
k = 37.5
for j in range(20):                
    makeTriangle(0+k*j, 350, 350, -75+k*j, 350, 75+k*j, 350)
    
save("triangles.png")
