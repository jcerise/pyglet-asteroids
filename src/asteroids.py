import pyglet
from game import resources, load

# Set the main game window
game_window = pyglet.window.Window(800, 600)

# Set the main labels that will display at the top of the screen
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(text="Pyglet Asteroids", x=400, y=575, anchor_x='center')

# Set up the player
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

# Set up the asteroids
asteroids = load.asteroids(3, player_ship.position)

@game_window.event
def on_draw():
    # Draw
    game_window.clear()
    level_label.draw()
    score_label.draw()
    player_ship.draw()

    for asteroid in asteroids:
        asteroid.draw()

if __name__ == '__main__':
    pyglet.app.run()
