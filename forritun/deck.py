import random


class Card:
    __INT_RANK_DICT = {1: "A", 11: "J", 12: "Q", 13: "K"}
    __STR_RANK_DICT = {"A": 1, "J": 11, "Q": 12, "K": 13}
    __SUIT_SET = {"H", "S", "D", "C"}

    def __init__(self, rank=0, suit=''):
        if type(rank) == str:
            rank = str(rank).upper()
            self.__rank = self.__STR_RANK_DICT.get(rank, 0)
        else:
            if type(rank) == int and 0 <= rank <= 13:
                self.__rank = rank
            else:
                self.__rank = 0
        suit = str(suit).upper()
        if suit in self.__SUIT_SET:
            self.__suit = suit
        else:
            self.__suit = ''

    def __str__(self):
        if self.is_blank():
            return "blk"
        rank_str = self.__INT_RANK_DICT.get(self.__rank, self.__rank)
        card_string = "{}{}".format(rank_str, self.__suit)
        return "{:>3}".format(card_string)

    def is_blank(self):
        return self.__rank == 0 or self.__suit == ''


class Deck:
    def __init__(self):
        self.__deck = list()
        suits = ["S", "H", "D", "C"]
        for i in range(1, 14):  # assemble deck
            for j in range(4):
                suit = suits[j]
                card = Card(i, suit)
                self.__deck.append(card)

    def __str__(self):
        deck_string = ""
        line_length = 13
        for i in range(4):
            index = i * line_length
            last_index = index + line_length
            line = self.__deck[index:last_index]
            for card in line:
                deck_string += str(card) + " "
            if len(self.__deck) > last_index:
                deck_string += "\n"
        return deck_string

    def shuffle(self):
        random.shuffle(self.__deck)

    def deal(self):
        return self.__deck.pop(0)


class PlayingHand:
    NUMBER_CARDS = 13

    def __init__(self):
        self.cards = list()
        for _ in range(self.NUMBER_CARDS):
            self.cards.append(Card())

    def add_card(self, card):
        for i, stored_card in enumerate(self.cards):
            if stored_card.is_blank():
                self.cards[i] = card
                break

    def __str__(self):
        hand_string = ""
        for card in self.cards:
            hand_string += str(card) + " "
        return hand_string


def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5, 's')
    print(card2)
    card3 = Card('Q', 'D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)


def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)


def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for _ in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())


def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)

    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)


# The main program starts here
random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)
