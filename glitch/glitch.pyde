size(400, 400)
#strokeWeight(5)

source_1 = loadImage("deer.png")

for y in range(400):
    for x in range(400):
    
        pixel_1 = source_1.get(x, y)
        r_1 = red(pixel_1)
        g_1 = green(pixel_1)
        b_1 = blue(pixel_1)
        if r_1 > 150:
            stroke(255, random(125, 255), random(150, 255))
        elif r_1 > 100:
            stroke(255, random(61, 255), random(61, 255))
        else:
            stroke(255, random(200), random(200))
       #     stroke(r_1, g_1, b_1)

        point(x, y)
