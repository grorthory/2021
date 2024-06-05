from sim_helpers import *

def setup():
    size(400, 400)
    global sun, planet, planets
    planets = []
    
    sun = {'x': 200,
           'y': 200,
           'size': 50
           }
    
    for i in range(4):
        planet = {'x': random(400),
              'y': random(400),
              'size': random(20.0, 40.0),
              'heading': random(2*PI),
              'speed': 1,
              'attraction': 1,
              'atmosphere': 1,
              'color': color(random(255), random(255), random(255))
              }
        planet['attraction'] = planet['size']/2000
        planet['atmosphere'] = planet['size']*5
        planets.append(planet)

def draw():
    global sun, planets
    for i in range(len(planets)):
        planet = planets[i]
        #circle(sun['x'], sun['y'], sun['size'])
        stroke(planet['color'])
        circle(planet['x'], planet['y'], planet['size'])
        planet['x'] += cos(planet['heading']) * planet['speed']
        planet['y'] += sin(planet['heading']) * planet['speed']
        avoid_walls(planet, 40, 0.5)
        for other_planet in planets:
            if other_planet != planet: 
                seek(planet, other_planet, other_planet['atmosphere'], planet['attraction'])
