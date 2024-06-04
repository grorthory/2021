size(1024, 768)

source_1 = loadImage("clouds.png")

for y in range(768):
    for x in range(1024):
    
        pixel_1 = source_1.get(x, y)
        r_1 = red(pixel_1)
        g_1 = green(pixel_1)
        b_1 = blue(pixel_1)
        if r_1>110:
            stroke(255-r_1, 255-g_1, 255-b_1)
        point(x, y)
