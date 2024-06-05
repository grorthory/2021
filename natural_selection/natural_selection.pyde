from sim_helpers import *

def setup():
    size(400, 400)
    noStroke()
    global cells, survivors, foods, timer
    survivors = []
    timer = 0
    cells = []
    for i in range(5):
        cell = {'x': random(400),
                'y': random(400),
                'size': 10.0,
                'speed': 1.5,
                'heading': random(2*PI),
                'color': color(0, 255, 0),
                'sight': random(40, 60),
                'food_count': 0
                }
        cells.append(cell)
    
    foods = []
    for i in range(30):
        food = {'x': random(400),
                'y': random(400)
                }
        foods.append(food)
    
def draw():
    global cells, foods, timer, survivors
    background(255)
    for cell in cells:
        fill(cell['color'])
        circle(cell['x'], cell['y'], cell['size'])
        #cell['speed'] = 10 / cell['size']
        cell['x'] += cos(cell['heading']) * cell['speed']
        cell['y'] += sin(cell['heading']) * cell['speed']
        avoid_walls(cell, 40, 0.5)
        for food in foods:
            seek(cell, food, cell['sight'], random(0.1, 5))
            if dist(cell['x'], cell['y'], food['x'], food['y']) < cell['size']*.5:
                foods.remove(food)
                cell['size'] = cell['size']+2.5
                cell['food_count'] += 1
                if cell['food_count'] == 2:
                    cells.remove(cell)
                    survivors.append(cell)
        
        for other_cell in cells:
            if other_cell['size'] < cell['size'] and other_cell != cell:
                seek(cell, other_cell, cell['sight'], 0.5)
                distance = seek(cell, other_cell, cell['sight'], .5)
                if distance < cell['size'] / 2:
                    cell['size'] = cell['size'] + other_cell['size']
                    cells.remove(other_cell)
                    cell['food_count'] += 1
                    if cell['food_count'] == 2:
                        cells.remove(cell)
                        survivors.append(cell)
            if other_cell['size'] >= cell['size'] and other_cell != cell:
                avoid(cell, other_cell, cell['sight'], 0.5)
    for survivor in survivors:
        fill(0, 255, 0, 50)
        circle(survivor['x'], survivor['y'], survivor['size'])
            
    for food in foods:
        fill(255, 0, 0)
        square(food['x'], food['y'], 5)
        
    if millis() - timer > 5000:
        cells = []
        for survivor in survivors:
         for i in range(2):
             cell = {'x': random(survivor['x']-survivor['size']*.5, survivor['x']+survivor['size']*.5),
                'y': random(survivor['y']-survivor['size']*.5, survivor['y']+survivor['size']*.5),
                'size': survivor['size']*.5,
                'speed': survivor['speed'],
                'heading': random(2*PI),
                'color': survivor['color'],
                'sight': survivor['sight'],
                'food_count': 0
                }
             if random(1) < .2:
                 cell['speed'] = survivor['speed'] + random(-1, 1)
                 cell['color'] = color(255, 255, 0)
             cells.append(cell)
        survivors = []
        if len(foods) < 30:
            for i in range(30-len(foods)):
                food = {'x': random(400),
                'y': random(400)
                }
                foods.append(food)
        timer = millis()
