size(640, 480)
strokeWeight(5)

def input(x_start, y_start, x_anchor1, y_anchor1, x_anchor2, y_anchor2, x_stop, y_stop):
    line(x_start, y_start, x_stop, y_stop)
    point(x_anchor1, y_anchor1)
    point(x_anchor2, y_anchor2)
    bezier(x_start, y_start, x_anchor1, y_anchor1, x_anchor2, y_anchor2, x_stop, y_stop)

input(100, 100, 200, 300, 400, 150, 400, 400)
