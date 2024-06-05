from random import randint
def setup():
    size(304, 304)
    global source, timer, period, flip, thresholds, threshold_x, threshold_y, num_thresholds, colors
    #source = loadImage("skull.png")
    #source = loadImage("deer.png")
    source = loadImage("toad.png")
    source.loadPixels()
    timer = 0
    period = 30
    flip = 1
    num_thresholds = 6
    interval = 255/num_thresholds
    thresholds = []
    threshold_x = 255
    threshold_y = 212.5
    colors = [[245, 76, 0], [255, 150, 0], [244, 78, 163], [199, 26, 253], [73, 65, 248], [0, 154, 228]]
    for i in range(num_thresholds):
        thresholds.append([threshold_x-(i*interval), threshold_y - (i*interval)])
        #format: x, y, r, g, b
def draw():
    global timer, thresholds, flip, threshold_x, threshold_y, num_thresholds
    filler_number = randint(0, num_thresholds-1)
    filler_color = color(colors[filler_number][0], colors[filler_number][1], colors[filler_number][2])
    for y in range(source.height):
        for x in range(source.width):
            pixel_1 = source.pixels[x+y*source.width]
            r_1 = red(pixel_1)
            g_1 = green(pixel_1)
            b_1 = blue(pixel_1)
            for i in range(len(thresholds)):
                if thresholds[i][1]<b_1<thresholds[i][0]:
                    stroke(colors[i][0], colors[i][1], colors[i][2])
                    break
                else:
                    stroke(filler_color)
                    #stroke(255)
            point(x, y)
    if millis() - timer > 10:
        for threshold in thresholds:
            threshold[0] = threshold[0] - (4*flip)
            threshold[1] = threshold[1] - (4*flip)
            if threshold[0] < 0:
                threshold[0] = threshold_x
                threshold[1]= threshold_y
        #if thresholds[0][0] < 40 or thresholds[0][0] > 260:
        #    flip = -flip
        timer = millis()
    saveFrame()
