import turtle
import game_base 
from card import Flip

def write_leaderboard(leader_board, file_name="leaderboard_list.txt"):
    '''
    write_leaderboard() --
        Writes the updated leaderboard to a file
    Parameters --
        leader_board, file_name
    '''
    with open(file_name, "w") as file:
        for name, score in leader_board:
            file.write(f"{name},{score}\n")

def get_score(x):
    '''
    get_score() --
        Returns the item at index 1 of the parameter
    '''
    return x[1]

def read_leaderboard(file_name="leaderboard_list.txt"):
    '''
    read_leaderboard() --
        Reads the leaderboard from a file and returns it
        as a sorted list of tuples
    Parameter --
        file_name (.txt file)
    Return --
        list of tuples with players and their scores sorted
        based on lowest to highest scores
    '''
    leaderboard = []
    try:
        with open(file_name, "r") as file:
            for line in file.readlines():
                name, score = line.strip().split(",")
                # Convert score to an integer and add to list
                leaderboard.append((name, int(score)))
            
            # Sort by score
            sorted_leaderboard = sorted(leaderboard, key = get_score)                  
            return sorted_leaderboard  

    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return leaderboard  
            
def update_leaderboard(player_name, guesses, file_name="leaderboard_list.txt"):
    '''
    update_leaderboard() --
        Updates the leaderboard with the current user's score
    Parameter --
        player_name, guesses, file_name
    '''
    # player_name = game_base.user_name()
    leaderboard = read_leaderboard(file_name)
    leaderboard.append((player_name, guesses))

    sorted_leaderboard = sorted(leaderboard, key=get_score)
    
    # Keep only the top 8 scores
    top_leaders = []
    
    for i in range(min(len(sorted_leaderboard), 8)):
        top_leaders.append(sorted_leaderboard[i])

    write_leaderboard(top_leaders, file_name)
    
    return top_leaders

def display_leaders(screen, leaders):
    '''
    display_leaders() --
        Displays the top 8 scorers on the Turtle screen
    Parameters --
        screen (turtle screen), leaders (list)
    '''
    display_turtle = turtle.Turtle()
    display_turtle.penup()
    display_turtle.color("blue")
    display_turtle.hideturtle()
    x = 170
    y = 240

    #positioning players and scores on the leaderboard
    for each in leaders:
        y = y - 30
        player = each[0] + ": " + str(each[1])
        display_turtle.setpos(x,y)
        display_turtle.write(player, False, font=('Arial', 12, 'normal'))
