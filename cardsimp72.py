#In this project, I used Object Orienented Design to
#make a program that shuffles a deck of cards
import random
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

class Deck():
    import random

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self, cards):
        return self.random.shuffle(cards)

    def draw(self, number):
        return self.cards[number]


def main():
    stack = []
    stack = createCards(stack)
    deck1 = Deck(stack)
    deck1.shuffle(stack)
    for i in range(52):
        x = deck1.draw(i)
        y = x.getRank()
        if y == 11:
            y = 'jack'
        if y == 12:
            y = 'queen'
        if y == 13:
            y = 'king'
        if y == 1:
            y = 'ace'
        z = x.getSuit()
        print(y, 'of', z)

def createCards(stack):
    stack = [0] * 52
    po = 0
    lo = 1
    for i in range(13):
        tcard = Card('spade', lo)
        stack[po] = tcard
        po = po + 1
        lo = lo + 1
    lo = 1
    for i in range(13):
        tcard = Card('heart', lo)
        stack[po] = tcard
        po = po + 1
        lo = lo + 1
    lo = 1
    for i in range(13):
        tcard = Card('club', lo)
        stack[po] = tcard
        po = po + 1
        lo = lo + 1
    lo = 1
    for i in range(13):
        tcard = Card('diamond', lo)
        stack[po] = tcard
        po = po + 1
        lo = lo + 1
    return stack
main()
