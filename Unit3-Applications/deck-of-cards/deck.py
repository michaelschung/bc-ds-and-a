from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['C', 'D', 'H', 'S']:
            for val in range(1, 14):
                self.cards.append(Card(val, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for card in self.cards:
            print(card)

    def draw_card(self):
        return self.cards.pop()

    def peek_top_card(self):
        return self.cards[0]

    def peek_n_cards(self, n):
        return self.cards[:n]
