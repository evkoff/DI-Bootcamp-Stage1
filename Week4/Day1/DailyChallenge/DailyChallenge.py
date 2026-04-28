# # OOP Quizz

# What You will learn :
# OOP
# Instructions
# Part 1 : Quizz :
# Answer the following questions
# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?

# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
class Deck:
    def __init__(self):
        self.cards = []
        
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
deck = Deck()
deck.shuffle()

card = deck.deal()
if card is not None:
    print(card.value, card.suit)

print(len(deck.cards))  # должно быть 51