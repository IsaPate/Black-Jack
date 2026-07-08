from game_files.deck import *
from game_files.player import *

class Game :
    def __init__(self):
       self.players : list[Player] = []
       self.winners : list[Player] = []
    
    def loadPlayers (self) :
        try:
            numberOfPlayers = int(input("Type the number of players"))
        except (ValueError, TypeError) as e:
            raise e
        
        for i in range( numberOfPlayers ):
            created = self._createPlayer()
            self.players.append(created)

    def _createPlayer (self) -> Player :
        name = input("Type your name.")
        return Player(name)

    def begin(self) -> list[Player] :
        while True :

            self.loadPlayers()
            dealer = Dealer("Mr Kostas")

            print(f"Game begin with {len(self.players)} Players and 1 Dealer.")
            shuffled = dealer.shuffle()
            self.fillPlayerCardDeck(dealer , None , 2  , shuffled)

            for pl in self.players :
                self.fillPlayerCardDeck(dealer , pl , 2 , shuffled)

            print("=============================================")
            print(len(shuffled))
            dealer.showCards()
            print("Dealer opens random 1 card")
            
            dealer.openCard(dealer.getsCards())

            dealer.showCards()
            print(f"Opened card { [ card for card in dealer.getsCards() if card.open == True]}")

            print("=============================================")
            
            playerCount = self._playerCountRoutine(dealer , shuffled)

            if len(playerCount) == 0 : 
                self.winners.append(dealer.name)
                return self.winners
            dealerCounter = self._dealerCountRoutine(dealer , shuffled)
            
            print(f"Dealer counter {dealerCounter}")
            if dealerCounter >= 21 :
                if len(playerCount) == 1 :
                    print(f"winner is {playerCount[0][0]}. Counter = {playerCount[0][1]}")
                    self.winners.append(playerCount[0][0])
                else :
                    print(f"Winner are {len(playerCount)}.")
                    for pl in playerCount :
                        print(f"{pl[0]} -> counter = {pl[1]}")  
                        self.winners.append(pl[0])     
                return self.winners
            else :
                if len(playerCount) == 1 :
                    playerCounter = playerCount[0][1]
                    if dealerCounter > playerCounter :
                        print(f"Dealer won : {dealer.name}")                
                        self.winners.append(dealer.name)
                    else : 
                        print(f"Player won : {playerCount[0][0]}")
                        self.winners.append(playerCount[0][0])
                else :
                    for pl in playerCount :
                        if pl[1] < dealerCounter :
                         self.winners.append(dealer.name)
                        else :
                         self.winners.append(pl[0])
            return self.winners
    def fillPlayerCardDeck (self , dealer : Dealer  , player : Player , numOfCards , shuffled : list[Card]) :
        mapObject = dealer if player == None else player
        removed = dealer.share(numOfCards , shuffled)
        mapObject.setCards(removed)
        print(f"{mapObject.name} cards")
        mapObject.showCards()
    
    def addPlayers ( self , player : Player) -> None:
        self.players.append(player)
    
    def _playerCountRoutine (self, dealer : Dealer  , shuffled : list[Card]) -> list[tuple]:
        countForEveryPlayer : list[tuple]= []

        for index , player in enumerate(self.players):
            print(f"previous counter {player.countValues(player.getsCards())}")
            lostPlayer = None
            stop = False
            print(f" Player No {index} , named {player.name}, ready to draw cards.")
            while stop == False :
                remov = dealer.share(1 , shuffled)
                print(f"{player.name} gets {remov}.")
                player.setCards(remov)

                counter = player.countValues(player.getsCards())
                
                print(f"{counter} < 21")
                print("=============================================")
                if counter > 17 and counter <= 20 : 
                    stop = True

                if counter >= 21 : 
                    lostPlayer = player
                    stop = True

                
            if lostPlayer != None :
                continue
            playerTuple = (player.name , counter)
            countForEveryPlayer.append(playerTuple)
        return countForEveryPlayer
    def _dealerCountRoutine (self , dealer:Dealer , shuffled : list[Card]):
         dealerCounter = dealer.countValues(dealer.getsCards())
         while dealerCounter <= 17 :
            remov = dealer.share(1 , shuffled)
            dealer.setCards(remov)
            dealerCounter = dealer.countValues(dealer.getsCards())
            if dealerCounter == 21 or (dealerCounter > 17 and dealerCounter <= 20) :
                break
         return dealerCounter
