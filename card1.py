class Card:
    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    def print_info(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in range(suits):
            for value in values:
                self.cards.append(Card(suit, value))

deck = Deck()
for card in deck.cards:
    print(card.print_info())
firt_card = Card("Hearts", "A")
firt_card.print_info()