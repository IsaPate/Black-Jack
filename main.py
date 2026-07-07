from game_files.deck import Deck , Player , Dealer
from game_files.game import *
                
def main():
    game = Game()         
    return game.begin()
    

if ( __name__ == "__main__"):
    winners = main()
    for w in winners :
        print(w)