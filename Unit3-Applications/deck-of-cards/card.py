class Card:
    def __init__(self, val, suit):
        self.suit = suit
        self.val = val

    def __str__(self):
        return '{} of {}'.format(self.val, self.suit)
