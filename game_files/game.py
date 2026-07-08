from game_files.deck import *
from game_files.player import *

class Game :
    def __init__(self):
       self.MAX_VALUE_THRESHOLD = 21
       self.SMART_VALUE_THRESHOLD = 17
       self.players : list[Player] = []
       self.winners : list[tuple] = []
    
    def loadPlayers (self) :      
        numberOfPlayers = self._getNumOfPlayers()
        
        for i in range( numberOfPlayers ):
            created = self._createPlayer()
            self.players.append(created)

    def _getNumOfPlayers (self) -> int :
        inp = input("Type the number of players")
        try:
            numberOfPlayers = int(inp)
        except ValueError as e : 
            raise e
        while numberOfPlayers<=0 : 
            print("give a valid number of players.")
            numberOfPlayers = int(input("Type the number of players"))
        return numberOfPlayers

    def _createPlayer (self) -> Player :
        name = input("Type your name.")
        return Player(name)

    def begin(self) -> list[tuple] :

            # players init 
            self.loadPlayers()
            dealer = Dealer("Mr Kostas")

            print(f"Game begin with {len(self.players)} Players and 1 Dealer.")

            # shuffled deck and fill player cards
            shuffled = dealer.shuffle()
            self.fillPlayerCardDeck(dealer , None , 2  , shuffled)
            for pl in self.players :
                self.fillPlayerCardDeck(dealer , pl , 2 , shuffled)

            # show cards
            print("=============================================")
            dealer.showCards()
            print("Dealer opens random 1 card")
            dealer.openCard(dealer.getsCards())

            dealer.showCards()
            print(f"Opened card { [ card for card in dealer.getsCards() if card.open == True]}")
            print("=============================================")

            # card count for every player
            playerCount = self._playerCountRoutine(dealer , shuffled)

            # if players have count >=21 then dealer is the winner
            if len(playerCount) == 0 : 
                self.winners.append(dealer.name)
                return self.winners
            
            # card count for dealer 
            dealerCounter = self._dealerCountRoutine(dealer , shuffled)
            print(f"Dealer counter {dealerCounter}")

            return self._getWinnersTuple(dealer , dealerCounter , playerCount)

            
    def _getWinnersTuple ( self , dealer :Dealer , dealerCounter : int , playerCount: list[tuple]) -> list[tuple] :
        
            # if dealer counter is over 21 then check the players
            if dealerCounter >= 21 :
                print("Dealer lost.")
                for playerTuple in playerCount :
                    self.winners.append(playerTuple)
                   
            # if not check players with dealer and add the winner - or winners
            else :
                for playerTuple in playerCount :
                    print(playerTuple)
                    playerCounter = playerTuple[1]
                    if dealerCounter > playerCounter : 
                        dealerTuple = (dealer , dealerCounter)
                        self.winners.append(dealerTuple)
                    else : 
                        self.winners.append(playerTuple)
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
                if counter > self.SMART_VALUE_THRESHOLD and counter <= self.MAX_VALUE_THRESHOLD - 1 : 
                    stop = True

                if counter >=  self.MAX_VALUE_THRESHOLD : 
                    lostPlayer = player
                    stop = True

                
            if lostPlayer != None :
                continue
            playerTuple = (player.name , counter)
            countForEveryPlayer.append(playerTuple)
        return countForEveryPlayer
    
    def _dealerCountRoutine (self , dealer:Dealer , shuffled : list[Card]):
         dealerCounter = dealer.countValues(dealer.getsCards())
         while dealerCounter <= self.SMART_VALUE_THRESHOLD :
            remov = dealer.share(1 , shuffled)
            dealer.setCards(remov)
            dealerCounter = dealer.countValues(dealer.getsCards())
            if dealerCounter == self.MAX_VALUE_THRESHOLD or (dealerCounter > self.SMART_VALUE_THRESHOLD and dealerCounter <= self.MAX_VALUE_THRESHOLD-1) :
                break
         return dealerCounter
