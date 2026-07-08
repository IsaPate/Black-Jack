import random

class Deck :
    
    def __init__(self):
       self.cards : list[Card] = []

    def initializeDeck (self) -> list[Card]:
        categories = {
            1 : "♥", 
            2 : "♦", 
            3 : "♣", 
            4 : "♠"
        }
        characters = {
            1 : "J" , 
            2 : "K" , 
            3 : "Q"
        }
        for i in range(1,5):
            category = categories[i]
            for j in range(1 , 11 ):
                card = Card(category , str(j) , False)
                self.cards.append(card)
            for c in range(1,4):
                character = characters[c]
                card = Card(category , character , False)
                self.cards.append(card)
        return self.cards
    
    def printDeck (self) :
        for card in self.cards :
            print(card.printCard())

    def printDeckArray (self , array : list[Card] ):
        for item in array : 
                print(item.printCard())
        
    def shuffleDeck (self ,initialized : list[Card]) -> list[Card] :
        result : list[Card] = []
        last = -1 
        while len(result) < 52 : 
            index = random.randint(0,51)
            if index == last : continue
            card = initialized[index]
            result.append(card)
            last = index
        return result

class Card : 

    def __init__(self  , category : str , value : str , open : bool):
        self.category = category
        self.value = value
        self.open = open
    
    def getCategoryValue (self) :
        return self.category 
    
    def getValue (self) : 
         return self.value
    
    def printCard (self) : 
        return f"{self.category} - {self.value} - {self.open}"
    
    def __str__(self):
        return self.printCard()

    def __repr__(self):
      return self.printCard()
    
    def setOpen (self,  open : bool) : 
        self.open = open
    def getOpen(self):
        return self.open
   