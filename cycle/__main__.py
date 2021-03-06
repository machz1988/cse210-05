import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_cycle1_action import ControlCycle1Action
from game.scripting.control_cycle2_action import ControlCycle2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.trail_growth_action import TrailGrowthAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():

    # create positions
    position1 = Point(int(constants.MAX_X/5), int(constants.MAX_Y/2))
    position2 = Point(int(constants.MAX_X*4/5), int(constants.MAX_Y/2))
    colorcycle1 = constants.RED
    colorcycle2 = constants.GREEN

    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle(position1, colorcycle1))
    cast.add_actor("cycle2", Cycle(position2, colorcycle2))
    cast.add_actor("score1", Score("Player 1"))
    aux_position = Point(constants.MAX_X-7*constants.CELL_SIZE,0)
    score2 = Score("Player 2")
    score2.set_position(aux_position)
    cast.add_actor("score2", score2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCycle1Action(keyboard_service))
    script.add_action("input", ControlCycle2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(video_service))
    script.add_action("update", TrailGrowthAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()