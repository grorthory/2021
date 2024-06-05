from sim_helpers import *

def setup():
    size(400, 400)
    global cell
    global cells
    cells = []
    for i in range(20):
        cell = {'x': random(400),
                'y': random(400),
                'diameter': random(5, 50),
                'speed': 0,
                'heading': random(2*PI),
                'color': color(random(255), random(255), random(255))
                }
        cell['speed'] = 20 / cell['diameter']
        cells.append(cell)
def draw():
    global cells
    background(255)
    for cell in cells:
        fill(cell['color'])
        circle(cell['x'], cell['y'], cell['diameter'])
        cell['x'] += cos(cell['heading']) * cell['speed']
        cell['y'] += sin(cell['heading']) * cell['speed']
        
        avoid_walls(cell, 40, .5)
        
        for other_cell in cells:
            if other_cell['diameter'] > cell['diameter']:
                avoid(cell, other_cell, 40, .1)
            else:
                seek(cell, other_cell, 40, .1)
