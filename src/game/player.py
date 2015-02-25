import math
import pyglet
from pyglet.window import key
import physicalobject
import resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_flame, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.thrust = 300.0
        self.rotate_speed = 200.0

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            # Draw the engine flame behind the ship when the player moves forward
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            # Hide the engine flame once the player stops moving teh ship
            self.engine_sprite.visible = False

