from game.scripting.action import Action
import random

class TrailGrowthAction(Action):

    def __init__(self):
        self._counter = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._counter += 1
        self._handle_trail_growth(cast)

    def _handle_trail_growth(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")

        rnumber = random.randint(101, 500)
        if self._counter > rnumber:
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)
            self._counter = 0