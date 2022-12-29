# HigherOrLower

import random

# Card constants
SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King")

NCARDS = 8

# Pass in a deck and this functions returns a random card from the deck


def getCard(deckListIn):
    thisCard = deckListIn.pop()  # Pop one off the top of the deck and the card return \
    return thisCard

# Pass in a deck and this fucntions returns a shuffle copy of the deck


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Main Code
print("Welcome to Higher or Lower.")
print("You have to choose wether the next card to be shown would be higher or lower than the current card")
print("Getting it right adds 20 point; get it wrong and you lose 15 points ")
print("You have 50 points to start")
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue + 1
                    }
        startingDeckList.append(cardDict)

score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)

    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f"Starting card is: {currentCardRank} of {currentCardSuit}")
    print()

    for cardNumber in range(0, NCARDS):  # Play one game of this many cards
        answer = input(
            f"Will the next card be higher or lower than the {currentCardRank} of {currentCardSuit}? (enter h or l)")
        answer = answer.casefold()  # Force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print(f"Next card is: {nextCardRank} of {nextCardSuit}")

        if answer == "h":
            if nextCardValue > currentCardValue:
                print("You got it right, it was higher")
                score = score + 20
            else:
                print("Sorry, it was not higher")

        elif answer == "l":
            if nextCardValue < currentCardValue:
                score = score + 20
                print("you got it right, it was lower.")
            else:
                score = score - 15
                print("Sorry it was not lower")

        print(f"You score is {score}")
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # don't need current suit

    goAgain = input("To play again, press ENTER or 'q' to quit: ")
    if goAgain == "q":
        break

    print("Ok Bye")
