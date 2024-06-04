size(304, 304)

source_1 = loadImage("deer.png")

for y in range(304):
    for x in range(304):
    
        pixel_1 = source_1.get(x, y)
        r_1 = red(pixel_1)
        g_1 = green(pixel_1)
        b_1 = blue(pixel_1)
        stroke(r_1, g_1, b_1)
        if r_1<50:
            stroke(0)
        elif r_1<100:
            stroke(255)
        elif r_1 < 110:
            stroke(0)
        elif r_1 < 120:
            stroke(255)
        elif r_1 < 130:
            stroke(0)
        elif r_1 < 140:
            stroke(255)
        elif r_1 < 150:
            stroke(0)
        elif r_1 < 160:
            stroke(255)
        else:
            stroke(0)
        point(x, y)

save("deer.png")
