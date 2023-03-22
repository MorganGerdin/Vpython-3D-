from vpython import *
import random

def main():

    # set up the game environment
    scene = canvas(title="Asteroid Attack", width=800, height=600)
    scene.background = color.black
    scene.autoscale = False
    scene.range = 10

    # set up the player's spaceship
    ship = box(pos=vector(0, -9, 0), size=vector(1, 1, 1), color=color.white)

    # set up the asteroids
    num_asteroids = 10
    asteroids = []
    for i in range(num_asteroids):
        x = random.uniform(-10, 10)
        y = random.uniform(0, 10)
        z = random.uniform(-10, 10)
        asteroid = sphere(pos=vector(x, y, z), radius=1, color=color.red)
        asteroids.append(asteroid)

    # set up the game loop
    game_over = False
    while not game_over:
        rate(30)  # limit the frame rate

        # check for collisions between the ship and the asteroids
        for asteroid in asteroids:
            if mag(ship.pos - asteroid.pos) < 1.5:
                game_over = True

        # move the asteroids
        for asteroid in asteroids:
            asteroid.pos.y -= 0.1
            if asteroid.pos.y < -10:
                asteroid.pos.y = 10
                asteroid.pos.x = random.uniform(-10, 10)
                asteroid.pos.z = random.uniform(-10, 10)

        # move the ship
        keys = keysdown()
        if "left" in keys:
            ship.pos.x -= 0.1
        elif 'right' in keys:
            ship.pos.x += 0.1



    # game over screen
    text(pos=vector(-5, 0, 0), text="Game Over", color=color.white, height=2)
    button(bind=startOver, text='Play Again')


def startOver():
    text(pos=vector(0,-2,0), text='jk', color=color.white, height=2)
    

main()

