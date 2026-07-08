from game_files.game import Game
                
def main():
    game = Game()         
    return game.begin()
    

if ( __name__ == "__main__"):
    winners = main()
    for winnerTuple in winners :
        print(f"Winner : {winnerTuple[0]} with count {winnerTuple[1]}")