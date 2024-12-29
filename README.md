**MEMORY MATCH GAME** 
----------------------
**FILES USED**

1.  Python files:
   memory\_game.py -- driver file to play game 
   game\_base.py -- file to create the game board
   card.py -- Game play class to create the card behaviour, manage flipping  
              of cards and status of the current game
   playing\_cards.py -- file for creating and managing the card deck to play with
   leaderboard.py -- file to manage the leaderboard with names of the top 8 scorers

3.  Gif files:  
    'quitbutton.gif'  
    'quitmsg.gif'  
    'winner.gif'  
    'card\_warning.gif'   
    'card\_back.gif'   
    '2\_of\_clubs.gif'  
    '2\_of\_diamonds.gif'  
    '3\_of\_hearts.gif'  
    'ace\_of\_diamonds.gif'  
    'jack\_of\_spades.gif'  
    'king\_of\_diamonds.gif'  
    'queen\_of\_hearts.gif'  
             
4.  Txt Files:  
    'images.txt'  
    'leaderboard\_list.txt'

**DESIGN** 

1\. When the main driver file (memory\_game.py) is called it goes to the game\_outline() function in game\_base.py file. 
    This function creates the play area, status bar, leaderboard area and the quit functionality of the game.

2\. Then the text area is displayed for the user to enter their name. The game ends if they click on cancel.

3\. If the user enters a name then the game continues and the leaderboard is updated with the top 8 scores.  
  
4\. User is then prompted to choose the number of cards they want to play the game with:  
    --> If 8, 10 or 12 is chosen then the game continues with that   
        number of deck  
    --> If anything outside of the range of 8 to 12 is entered, the   
        user is prompted to enter a number again.  
    --> If input is 9 or 11 then the game reduces the value by 1   
       auto-selects that number. (example: if input = 9 then selected  
       deck will be 8 \[9-1 = 8\])

5\. The default deck in this game is based on the file names in images.txt file but another deck can be loaded by adding 
    another file name with different images in the function playing\_deck() in playing\_cards.py file \[line 51\].

6\. Each card is an object of the class Cards. This class also manages displaying the card image, positioning it and 
    flipping and hiding the card.

7\. The class Flip manages the logic of the game. If two cards are clicked they are added to a list and the images are 
    compared.

8\. The class Flip also counts the number of matches and guesses the user has made which is used as scores for the 
    leaderboard if the game is played successfully. 

**AUTHOR**

BHOOMIKA GUPTA
