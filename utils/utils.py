import os


class Helpers:
    def clearScreen():
        os.system("cls" if os.name == "nt" else "clear")
        Helpers.printer("Jungle Hero \n", False, "red")

    def printer(message: str, underline: bool = False, color: str = "white"):
        colors = {
            "red": "31",
            "green": "32",
            "yellow": "33",
            "blue": "34",
            "magenta": "35",
            "cyan": "36",
            "white": "37",
        }
        if underline:
            print(f"\033[{colors[color.lower()]};4m{message}\033[0m")
        else:
            print(f"\033[{colors[color.lower()]}m{message}\033[0m")
