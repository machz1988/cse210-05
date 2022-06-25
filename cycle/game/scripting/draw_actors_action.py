from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle import Cycle
import constants
import pyray

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def reset(self, cast, script):
        self.execute(cast, script)
        pyray.wait_time(5000)
    #     script.add_action("input", ControlCycle1Action(keyboard_service))
    # script.add_action("input", ControlCycle2Action(keyboard_service))
        #control1 = script
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        cast.remove_actor("cycle1", cycle1)
        cast.remove_actor("cycle2", cycle2)
        message = cast.get_first_actor("messages")
        cast.remove_actor("messages", message)
        
        # create positions
        position1 = Point(int(constants.MAX_X/5), int(constants.MAX_Y/2))
        position2 = Point(int(constants.MAX_X*4/5), int(constants.MAX_Y/2))
        colorcycle1 = constants.RED
        colorcycle2 = constants.GREEN
        cast.add_actor("cycle1", Cycle(position1, colorcycle1))
        cast.add_actor("cycle2", Cycle(position2, colorcycle2))
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")

        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        
        segments1 = cycle1.get_segments()
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
        #set a timer

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        segments1 = cycle1.get_segments()
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()