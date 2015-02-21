import pyglet
import random
import math
import resources


def distance(point_1=(0, 0), point_2=(0, 0)):
    """
    Returns the distance between two points
    :return: The distance between the two supplied points
    """
    #TODO: Is this the best way to do this?
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2
    )


def asteroids(num_asteroids, player_position):
    """
    Creates num_asteroids asteroid sprites at random positions and rotations, checking to ensure they are far enough
    away from the players location.
    :param num_asteroids: The number of asteroids to draw to the screen
    :param player_position: The players current position
    :return: A list of asteroids sprites
    """
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        # Try and place a new asteroid. If it is too close to the player, start again
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image, x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids