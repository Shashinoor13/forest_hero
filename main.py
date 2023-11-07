from utils.utils import Helpers
from functions.game_generate import GameGenerate

try:
    game_state = GameGenerate()
    while not game_state.is_complete:
        game_state
except KeyboardInterrupt:
    print("Oh! you pressed CTRL + C.")
    print("Game Exited.")

except Exception as e:
    print("Error occurred : ", e)

except BaseException as e:
    print("Error occurred : ", e)

finally:
    Helpers.printer("\n Thanks for playing", True, "green")
