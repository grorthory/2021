from sim_helpers import *
def setup():
    size(600, 600)
    global enemies, player
    enemies = []
    player = {'x': pmouseX,
              'y': pmouseY,
              'size': 30
              }
    for i in range(4):
        addEnemy()
def draw():
    background(255)
    player['x'] = pmouseX
    player['y'] = pmouseY
    circle(player['x'], player['y'], 20)
    for i in range(len(enemies)):
        enemy = enemies[i]
        position(enemy, drawEnemy)
        enemy['x'] += cos(enemy['heading']) * enemy['speed']
        enemy['y'] += sin(enemy['heading']) * enemy['speed']
        avoid_walls(enemy, 40, 0.5)
        seek(enemy, player, 1000, 0.4)
        for other_enemy in enemies:
            distance = seek(enemy, other_enemy, 10, .5)
            if distance < 10 and other_enemy != enemy:s
                enemies.remove(enemy)
                enemies.remove(other_enemy)
                addEnemy()
                addEnemy()
def drawEnemy(enemy):
    triangle(10, 0, -enemy['size'], 10, -enemy['size'], -10)

def addEnemy():
    enemy = {'x': random(600),
                 'y': random(600),
                 'size': 40,
                 'heading': random(2*PI),
                 'speed': 5,
                 }
    enemies.append(enemy)
