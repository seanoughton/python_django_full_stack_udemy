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
        self.cards = []
        for suit in SUITE:
            for rank in RANKS:
                if rank == "A":
                    rank = "14"
                if rank == "K":
                    rank = "13"
                if rank == "Q":
                    rank = "12"
                if rank == "J":
                    rank = "11"

                self.cards.append(suit+rank)

    def split(self):
        self.shuffle()
        return [ self.cards[0:26],self.cards[26:] ]

    def shuffle(self):
        shuffle(self.cards)
        return self.cards

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def add_card(self,card):
        self.cards.append(card)

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



######################
#### GAME PLAY #######
######################

deck = Deck()
hands = deck.split()
hand_one = Hand(hands[0])
hand_two = Hand(hands[1])
player = Player("Sean",hand_one)
computer = Player("Computer",hand_two)
print("Welcome to War, let's begin...")

def test_cards(computer_card,player_card):
    if (computer_card[1:] < player_card[1:]):
        return "computer"
    else:
        return "player"

def add_cards(person,cards):
    if person == "computer":
        for card in cards:
            computer.hand.add_card(card)
    else:
        for card in cards:
            player.hand.add_card(card)



while len(player.hand.cards) > 0 and len(computer.hand.cards) > 0:
    computer_card = computer.hand.remove_card()
    player_card = player.hand.remove_card()
    cards = [computer_card,player_card]
    print("Your Card is {x}".format(x=player_card))
    print("Computer's Card is {x}".format(x=computer_card))


    if (computer_card[1:] == player_card[1:]):
        if(len(player.hand.cards)<3  or len(computer.hand.cards)<3):
            break
        print("WAR!!!")
        cards = []
        for i in range(4):
            cards.append(computer.hand.remove_card())
            cards.append(player.hand.remove_card())

        computer_up = cards[0]
        player_up = cards[1]

        if (test_cards(computer_up,player_up) == "player"):
            add_cards("player",cards)
        else:
            add_cards("computer",cards)

    else:
        if (test_cards(computer_card,player_card) == "computer"):
             #print("Computer Won")
             add_cards("computer",cards)
        else:
            #print("Player Won")
            add_cards("player",cards)

if len(player.hand.cards) > len(computer.hand.cards):
    print ("You Won")
else:
    print ("The Computer Won")


# Use the 3 classes along with some logic to play a game of war!
