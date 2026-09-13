class Stone:
    def __init__(self, color):
        self.color = color
        self.liberties = set()

    def add_liberty(self, position):
        self.liberties.add(position)


    def remove_liberty(self, position):
        self.liberties.discard(position)


    def has_liberties(self):
        return len(self.liberties) > 0