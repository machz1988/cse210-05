import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.

    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position, colorcycle):
        super().__init__()
        self._segments = []
        self._prepare_body(position, colorcycle)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self, position, colorcycle):
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            color=colorcycle

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            color = tail.get_color()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_text("#")
            segment.set_color(color)
            segment.set_velocity(velocity)
            segment.set_position(position)
            self._segments.append(segment)