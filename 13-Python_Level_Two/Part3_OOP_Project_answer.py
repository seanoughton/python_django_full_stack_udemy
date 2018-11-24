#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

#import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        #use a tuple for each card
        # self.cards = []
        # for r in RANKS:
        #     for s in SUITE:
        #         cards.append((s,r))
        # or use list comprehension , the above is equal to this
        self.cards = [(s,r) for s in SUITE for r in RANKS]


    def split_in_half(self):
        #returns a tuple of the split cards
        return (self.cards[0:26],self.cards[26:])

    def shuffle(self):
        shuffle(self.cards)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):#returns the number of cards in a players hand
        return "Contains {} cards".format(len(self.cards))

    def add(self,card):
        self.cards.extend(card)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Return true if player still has cards left
        """
        return len(self.hand.cards) != 0
######################
#### GAME PLAY #######
######################



print("Welcome to War, let's begin...")
d = Deck()
d.shuffle()
#below assigns each variable to one of the tuples that is returned
#tuple unpacking
half1,half2 = d.split_in_half()

comp = Player("computer",Hand(half1)) #creates a computer player with a Hand object created with the first half of the cards

name = input ("what is your name?")
user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and user.still_has_cards():
    total_rounds += 1
    print("time for a new round")
    print("here are the current standings")
    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(comp.name + "has the count: " + str(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print ("War!")
        #Below draws the four cards necessary for war and adds them to the table_cards list
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        #it takes the index value of RANKS, for instance RANKS.index(5) = 3, it is the index value fo the number 5 in the RANKS LIST
        #where is the index of each card in the RANKS list
        #RANKS is indexed so that the lowest card is 0 and the highest card is 12 (A)
        #RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    #if there is no war, just compare the cards
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

#end while Loop

print("game over, number of rounds: " + str(total_rounds))
print("a war happend " + str(war_count)+ " times")
# Use the 3 classes along with some logic to play a game of war!
