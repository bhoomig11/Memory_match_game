import turtle as t
import time

def get_card_number():
    '''
    get_card_number() --
        takes in input of the number of cards user wishes to
        play with
    Return --
        card_num chosen by the user (int)
    '''
    screen = t.Screen()
    num = "Number of cards to play:(8, 10 or 12)"
    card = screen.numinput('Card Number', num, minval=8, maxval=12)

    DEFAULT_NUM = 8
    
    if card == None:  
        card = DEFAULT_NUM
        return card
    else:
        return card

def play_box():
    '''
    play_box() --
        draws a rectangle on turtle screen where cards
        will be displayed
    '''
    play_area = t.Turtle()
    play_area.speed('fast')

    play_area.penup()
    play_area.setpos(-365,-210)
    play_area.pendown()

    play_area.pensize(5)
    play_area.forward(487)
    play_area.left(90)
    play_area.forward(515)
    play_area.left(90)
    play_area.forward(487)
    play_area.left(90)
    play_area.forward(515)
    play_area.left(90)
    play_area.hideturtle()

def status_box():
    '''
    status_box() --
        draws a rectangle on turtle screen where status
        of the current game will be displayed
    '''
    status_box = t.Turtle()
    status_box.speed('fast')

    status_box.penup()
    status_box.setpos(-365,-290)
    status_box.pendown()

    status_box.pensize(5)
    status_box.forward(487)
    status_box.left(90)
    status_box.forward(50)
    status_box.left(90)
    status_box.forward(487)
    status_box.left(90)
    status_box.forward(50)
    status_box.left(90)
    status_box.hideturtle()
    
def leader_box():
    '''
    status_box() --
        draws a box on turtle screen where the top 8 players
        will be displayed
    '''
    leader_box = t.Turtle()
    leader_box.speed('fast')

    leader_box.penup()
    leader_box.setpos(150,-210)
    leader_box.pendown()

    leader_box.pensize(5)
    leader_box.color("blue")

    leader_box.forward(200)
    leader_box.left(90)
    leader_box.forward(515)
    leader_box.left(90)
    leader_box.forward(200)
    leader_box.left(90)
    leader_box.forward(515)
    leader_box.left(90)
    leader_box.hideturtle()

    #title of leaderboard
    leader_txt = t.Turtle()
    leader_txt.penup()
    leader_txt.setpos(280,280)
    leader_txt.pendown()
    leader_txt.color("blue")
    title = "Leaders: "
    leader_txt.write(title, move=True, align='right', font=('Arial', 16, 'normal'))
    leader_txt.hideturtle()

def close_screen():
    '''
    close_screen() --
        Displays an image that the game has ended before
        closing the screen
    '''
    print("Quit button clicked. Game ended")
    QUIT_MESSAGE = 'quitmsg.gif'
        
    quit_turtle = t.Turtle()
    quit_turtle.penup()
    quit_turtle.hideturtle()
    quit_turtle.setpos(0, 0)  
    screen = t.Screen()
    screen.register_shape(QUIT_MESSAGE)
    quit_turtle.shape(QUIT_MESSAGE)
    quit_turtle.showturtle()

    screen.ontimer(t.bye, 3000)

def quit_button(image):
    '''
    quit_button() --
        displays a quit button at the bottom right of the
        turtle screen
    '''
    img = t.Turtle()
    screen = t.Screen()
    
    img.penup()
    screen.register_shape(image)
    img.shape(image)
    img.setpos(268,-270)
        
    img.onclick(lambda x, y: close_screen())

def game_outline():
    '''
    game_outline() --
        calls the above functions to display the game
        on turtle screen
    '''
    screen = t.Screen()
    play_box()
    status_box()
    leader_box()
    quit_button("quitbutton.gif")

def user_number():
    '''
    user_number() --
        changes the card number to an even number if
        input is an odd number
    '''
    card_num = get_card_number()
    if card_num == 9 or card_num == 11:
        error = t.Turtle()
        screen = t.Screen()
        screen.register_shape('card_warning.gif')
        error.shape('card_warning.gif')
        time.sleep(5)
        error.shape('blank')
        card_num = card_num - 1

    return card_num
