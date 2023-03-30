class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_info(self):
        print(f"{self.value} of {self.suit}")

    def main():
        card_1 = Card("Hearts", "A") 
        card_2 = Card("Hearts", "2") 
        print(card_1 > card_2)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)
    def print_deck(self):
        for card in self.cards:
            card.print_info()
    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)
    def dell(self):     
      # return self.cards[-1]
        return self.cards.pop()



deck = Deck()
deck.print_deck()
print("-------------")
deck.shuffle()
deck.print_deck()
print("-----------")
card_1 = deck.dell()
card_1.print_info()
#firt_card = Card("Hearts", "A")
#firt_card.print_info()



