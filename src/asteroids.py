import pyglet
from game import resources, load, physicalobject, player

# Set the main game window
game_window = pyglet.window.Window(800, 600)

# Define the main graphics batch
main_batch = pyglet.graphics.Batch()

# Set the main labels that will display at the top of the screen
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Pyglet Asteroids", x=400, y=575, anchor_x='center', batch=main_batch)
player_lives = load.player_lives(3, main_batch)

# Set up the player
player_ship = player.Player(x=400, y=300, batch=main_batch)

# Let Pyglet know the player is an even handler
game_window.push_handlers(player_ship)

# Set up the asteroids
asteroids = load.asteroids(3, player_ship.position, main_batch)

# Create a list of all game objects
game_objects = [player_ship] + asteroids


def update(dt):
    for obj in game_objects:
        obj.update(dt)


@game_window.event
def on_draw():
    # Draw all of our batched sprites to the screen
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
