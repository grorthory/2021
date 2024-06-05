size(500, 400)
background(93, 10, 129)
stroke(255, 255, 0)
strokeWeight(10)

point_list = []

for i in range(50):
    point_list.append((int(random(0, 500)), int(random(0, 400))))
    
for i in range(50):
    point(point_list[i][0], point_list[i][1])

strokeWeight(2)
for i in range(50):
    for j in range(50):
        if abs(point_list[i][0] - point_list[j][0]) < 50 and abs(point_list[i][1] - point_list[j][1]) < 50 and random(1) > .5:
            line(point_list[i][0], point_list[i][1], point_list[j][0], point_list[j][1])
            
save("stars3.png")    
    
