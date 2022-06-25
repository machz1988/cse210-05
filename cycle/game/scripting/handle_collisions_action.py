from itertools import cycle
from re import T
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
#from game.services.video_service import VideoService
from threading import Timer

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collides
    with the each other, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, video_service):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._cycle1_wins = False
        self._cycle2_wins = False
        self._video_service = video_service
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        
        # if self._video_service.is_window_open():
        #     self._handle_cycle_collision(cast)
        #     self._handle_segment_collision(cast)
        #     self._handle_game_over(cast, script)
        if not self._is_game_over:
            self._handle_cycle_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)
       

    def _handle_cycle_collision(self, cast):
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        for segment1 in segments1:
            if head2.get_position().equals(segment1.get_position()):
                self._cycle1_wins = True
                self._is_game_over = True
                score1.add_points(1)

        for segment2 in segments2:
            if head1.get_position().equals(segment2.get_position()):
                self._cycle2_wins = True
                self._is_game_over = True
                score2.add_points(1)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        cycle2 = cast.get_first_actor("cycle2")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        
        for segment1 in segments1:
            if head1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._cycle2_wins = True
                score2.add_points(1)
        for segment2 in segments2:
            if head2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._cycle1_wins = True
                score1.add_points(1)

    # def _reset(self, cast, script):
    #     self._is_game_over = False
    #     daas = script.get_actions("output")
    #     for daa in daas:
    #         daa.execute(cast, script)

    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycle1")
            segments1 = cycle1.get_segments()
            cycle2 = cast.get_first_actor("cycle2")
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            if self._cycle1_wins:
                message.set_text(f"{score1.get_player()} wins this round!")
                self._cycle1_wins = False
            else:
                message.set_text(f"{score2.get_player()} wins this round!")
                self._cycle2_wins = False
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)
            
            my_script = script.get_actions("output")[0]
            control1 = script.get_actions("input")[0]
            control2 = script.get_actions("input")[1]
            control1.set_direction(Point(0, -constants.CELL_SIZE))
            control2.set_direction(Point(0, -constants.CELL_SIZE))
            self._is_game_over = False
            
            #my_script.execute(cast, script)
            my_script.reset(cast, script)

        #     daas = script.get_actions("output")
        # for daa in daas:
        #     daa.execute(cast, script)
            #t = Timer(5, self._reset(cast, script))
            #t.start()