import random
import copy

# types of hands
HAND_TYPES = {
    1: "High Card",
    2: "Pair",
    3: "Two Pair",
    4: "Three of a Kind",
    5: "Straight",
    6: "Flush",
    7: "Full House",
    8: "Four of a Kind",
    9: "Straight Flush",
    10: "Royal Flush"
}

# ranks
RANKS = list(range(2, 15))

# suits
SUITS = ["H", "S", "C", "D"]

# full unshuffled deck
DECK = [str(r)+s for s in SUITS for r in RANKS]     

# shuffle a deck
def shuffle(deck):
    random.shuffle(deck)

# draw card from a deck
def draw(deck):
    return deck.pop(0)

# driver to check hand score (ten possibilities, 1 = high card & 10 = royal flush)
def check_hand_score(hand):

    # initialize score
    score = 0

    #
    # compute key info about hand
    #

    # get list of ranks
    ranks = []
    # get list of suits
    suits = []
    # get highest card
    h_card = hand[0]
    # iterate cards
    for card in hand:
        ranks.append(card[:-1])
        suits.append(card[-1])
        if card[:-1] > h_card[:-1]:
            h_card = card
    # find repetitions (of ranks and suits)
    rranks = [ranks.count(i) for i in ranks]
    rsuits = [suits.count(i) for i in suits]
    # get longest sequence
    ranks.sort()
    l_seq = [].append(ranks[0])
    for i in range(1, len(ranks)):
        if ranks[i] == ranks[i-1]+1:
            l_seq.append(ranks[i])
        else:
            l_seq = [].append(ranks[i])
    # indicator of possible straight
    p_straight = len(l_seq) >= 5
    # indicator of possible flush
    p_flush = max(rsuits) >= 5

    #
    # determine hand scoring
    #

    # royal flush
    if p_straight and p_flush:
        # check royal flush
        pass

    # straight flush
    if p_straight and p_flush:
        # check straight flush
        pass

    # four of a kind
    if max(rranks) >= 4:
        # check four of a kind
        pass
    
    # full house
    if max(rranks) >= 3:
        # check full house
        pass
    
    # flush
    if p_flush:
        # check flush
        pass

    # straight
    if p_straight:
        # check straight
        pass

    # three of a kind
    if max(rranks) >= 3:
        # check three of a kind
        pass

    # two pair
    if max(rranks) >=2:
        # check two pair
        pass

    # high card
    if score == 0:
        score = 1
        return score, h_card

    #return ranks, suits, rranks, rsuits


deck1 = DECK.copy()

print("deck1: ")
print(deck1)
print("")

print("shuffled: ")
shuffle(deck1)
print(deck1)
print(len(deck1))

print("draw a stack of seven cards:")
cards = []
for _ in range(7):
    cards.append(draw(deck1))
print("cards: ")
print(cards)
print("deck after draw: ")
print(deck1)
print(len(deck1))

r, s, rranks, rsuits = check_hand_score(cards)
print(r)
print(s)
print(rranks)
print(rsuits)


def check_royal_flush(info):
    pass

def check_straight_flush(cards):
    pass

def check_four_of_a_kind(cards):
    pass

def check_full_house(cards):
    pass

def check_flush(cards):
    pass

def check_straight(cards):
    pass

def check_three_of_a_kind(cards):
    pass

def check_two_pair(cards):
    pass

def check_pair(cards):
    pass

def check_high_card(cards):
    pass