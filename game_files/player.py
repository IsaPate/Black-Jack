from game_files.deck import * 

class Player : 
    
    def __init__(self , name : str):
        self.name = name 
        self.cards : list[Card] = []
    
    def getsCards (self) -> list[Card]: 
        return self.cards
    
    def setCards ( self , cards: list[Card]):
        for card in cards : 
            self.cards.append(card)

    
    def countValues (self , playerCards : list[Card]) -> int :
        sumOfCards = 0
        for card in playerCards : 
            if card.getValue() == "J" or card.getValue() == "K" or card.getValue() == "Q":
                sumOfCards += 10
            else :
                sumOfCards += int(card.getValue())
        return sumOfCards
    
    # make it one string
    def showCards (self) -> None : 
        for card in self.cards :
            print(card.__repr__())

class Dealer (Player):

    def __init__(self, name):
        super().__init__(name)
        self.deck = Deck()

    def shuffle (self) -> list[Card] : 
         initialized = self.deck.initializeDeck()
         return self.deck.shuffleDeck(initialized)

    def share (self , numOfCards : int , deck : list[Card]) -> list[Card] : 
       removedCards : list[Card] = []
       for i in range(numOfCards):
           removed = deck.pop(i)
           removedCards.append(removed)
       return removedCards
    
    def openCard (self, cards : list[Card]) -> list[Card]:
        rand = random.randint(0,1)
        card = cards[rand]
        card.setOpen( True)
        return cards
        