import pyglet


def center_image(image):
    """
    Sets an images anchor point to its center
    :param image: Image to set anchor point for
    """
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Load up all the images that will be displayed for the game, and center their anchor points
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image('player.png')
center_image(player_image)

bullet_image = pyglet.resource.image('bullet.png')
center_image(bullet_image)

asteroid_image = pyglet.resource.image('asteroid.png')
center_image(asteroid_image)