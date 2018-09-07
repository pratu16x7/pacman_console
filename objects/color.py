class Color:
    def __init__(self, curses):
        self.curses = curses
        self.init_curses_color_pairs()
        self.define_colors()
        self.set_color_properties()

    def init_curses_color_pairs(self):
        self.curses.initscr()
        self.curses.start_color()
        self.curses.use_default_colors()
        for i in range(0, self.curses.COLORS):
            self.curses.init_pair(i + 1, i, -1)
        for i in range(0, self.curses.COLORS):
            self.curses.init_pair(i + 1 + 300, i, i)

    def define_colors(self):
        self.color_values = {
            'black': 233,
            'blue': 22,
            'blue_fill': 278,
            'yellow': 12,
            'red': 2,
            'pink': 14,
            'cyan': 15,
            'orange': 209
        }

    def set_color_properties(self):
        for key, value in self.color_values.items():
            setattr(self, key, self.curses.color_pair(value))
