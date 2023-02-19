import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11) ] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

beef = Card('3','5')
print(beef[1])
print(len(beef))
deck = Deck()
print(deck[0])
c = choice(deck)
print(c)
