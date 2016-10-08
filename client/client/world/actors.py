from .abc import ABCActor
from .constants import (
    CHARACTER_RADIUS, CHARACTER_SPEED, CHARACTER_ROTATION)
from engine.geometry import Circle, Vector


class ActorMovement(object):
    """ Simple helper to fully describe movement of a character
    """

    def __init__(self, forward=Vector.polar(0)):
        # One of:
        # * 0 - no movement
        # * 1 - movement forward
        # * -1 - movement backward
        self.movement = 0
        # One of:
        # * 0 - no rotation
        # * 1 - rotation right
        # * -1 - rotation left
        self.rotation = 0
        # One of:
        # * 0 - no strafe
        # * 1 - strafe right
        # * -1 - strafe left
        self.strafe = 0

        # Forward unit vector
        self.forward = forward

        # TODO: add `target`


class Actor(ABCActor):

    def __init__(self, world, position=Vector(0, 0)):
        self._world = world
        self._position = position

    @property
    def position(self):
        return self._position


class Character(Actor):

    shape = Circle(Vector(0, 0), CHARACTER_RADIUS)
    movement = ActorMovement()

    def tick(self, dt):
        movement = self.movement
        # Rotate forward vector
        if movement.rotation:
            speed = CHARACTER_ROTATION * movement.rotation
            ang = movement.forward.angle + dt * speed
            movement.forward = Vector.polar(ang)
        # Determime movement vector
        if movement.movement:
            move = movement.forward * movement.movement
            # Apply strafing to movement vector
            if movement.strafe:
                move = move.rotate_deg(
                    45 * movement.strafe * movement.movement)
        elif movement.strafe:
            move = movement.forward.rotate_deg(movement.strafe * 90)
        else:
            move = Vector(0, 0)
        # Move character position
        self._position += move * (dt * CHARACTER_SPEED)
