import random 

class playing_card:
    def __init__(self, rank="queen", suit="hearts"):
        self._rank = rank 
        self._suit = suit
    def set_rank(self, rank): 
        self._rank = rank
    def set_suit(self, suit):
        self._suit = suit
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def select_at_random(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', "10", "jack", "queen", "king", "ace"]
        self._rank = random.choice(ranks)
        self.suit = random.choice(["spades", "hearts", "clubs", "diamonds"])
    def __str__(self):
        return(self._rank + " of " + self._suit)

