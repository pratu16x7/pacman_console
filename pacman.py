import curses
from objects.character import Pacman, Ghost
from objects.game_box import GameBox
from objects.color import Color

color = Color(curses)


class PacmanGame:
    def __init__(self):
        self.init_curses_and_screen()
        self.init_map()
        self.init_characters()
        self.start()

        self.score = 0


    def init_curses_and_screen(self):
        self.screen_obj = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        self.screen_obj.border(0)


    def init_map(self):
        self.game_box = GameBox(self.screen_obj, {
            'wall': color.blue_fill,
            'door': color.blue,
            'space': color.black,
            'food': color.yellow
        })


    def init_characters(self):
        self.pacman = Pacman(
            self.game_box,
            [18, 29],
            color.yellow
        )

        self.ghosts = {
            'Blinky': Ghost(
                self.game_box,
                [12, 25],
                color.red
            ),

            'Pinky': Ghost(
                self.game_box,
                [12, 29],
                color.pink
            ),

            'Inky': Ghost(
                self.game_box,
                [12, 33],
                color.cyan
            ),

            'Clyde': Ghost(
                self.game_box,
                [11, 29],
                color.orange
            )
        }


    def start(self):
        key = curses.KEY_RIGHT
        while True:
            next_key = self.game_box.map_box.getch()
            key = key if next_key == -1 else next_key

            if key == curses.KEY_UP:
                self.pacman.move('UP')

            if key == curses.KEY_DOWN:
                self.pacman.move('DOWN')

            if key == curses.KEY_LEFT:
                self.pacman.move('LEFT')

            if key == curses.KEY_RIGHT:
                self.pacman.move('RIGHT')

            self.ghosts['Blinky'].move_in_random_direction()
            self.ghosts['Pinky'].move_in_random_direction()
            self.ghosts['Inky'].move_in_random_direction()
            self.ghosts['Clyde'].move_in_random_direction()


PacmanGame()
