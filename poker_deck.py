from itertools import count

from deck import Deck, card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

count = 0
flushes = 0
while flushes < 1000:
    deck = Deck()
    deck._shuffle()
    hand = PokerHand(deck)
    print(hand)
    if hand.is_flush:
        flushes += 1
    count += 1

    print(f"prob of a flush is a {1000*flushes/count}%")
