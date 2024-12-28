import turtle as t
import game_base
import playing_cards
from card import Flip
import leaderboard

def game():
    '''
    game() --
        Driver function where the memory game is setup 
    '''
    #create screen
    screen = t.Screen()
    screen.setup(width=.60, height=0.90, startx=None, starty=None)
    screen.title("CS 5001 Memory Game")

    # creating game outline 
    game_base.game_outline()

    # input player name
    user_name = screen.textinput("Player Name", " Enter your name:")

    # if user clicks on cancel when prompted to enter name
    if not user_name:  
        print("No name entered. Exiting game")
        screen.bye()
        return

    # display the leaderboard of top 8 players
    leaders = leaderboard.read_leaderboard()
    leaderboard.display_leaders(screen, leaders)

    # display and update the status of the current
    managing_game = Flip(screen)
    managing_game.update_status()

    # display the card deck on screen
    playing_cards.display_cards(managing_game)

    t.done()

    # add the player and guesses to leaderboard after the game ends
    if managing_game.game_completed:
        leaderboard.update_leaderboard(user_name, managing_game.guesses)

def main():
    game()
if __name__ == "__main__":
    main()


