import turtle 

class Cards():
    ''' Class Cards
        Attributes: x, y, image, cover, manage
        Methods: register_img(), set_position(), flip(),
                 on_click(), etc
    '''
    def __init__(self, x, y, image, cover = 'card_back.gif', manage = None):
        '''
        Constructor -- creates an new instance
                   of Cards
        Parameters -- self - the current object
                      x, y - coordinates
                      image - the front side of card
                      cover - the back side of the card
                      manage - used here to handle the game logic
        '''
        if not isinstance(image, str):
            raise ValueError
                        
        if not isinstance(cover, str):
            raise ValueError

        self.image = image
        self.cover = cover
        self.x = x
        self.y = y
        self.manage = manage
        
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        
        self.register_img()
        self.turtle.shape(cover)
        self.turtle.goto(x,y)

        self.is_flipped = False
        self.turtle.onclick(self.on_click)
        
    def register_img(self):
        '''
        register_img --
            Registers the front and back image of the card
        '''
        if self.cover not in turtle.getshapes():
            turtle.register_shape(self.cover)
            
        if self.image not in turtle.getshapes():
            turtle.register_shape(self.image)

    def set_position(self, x, y):
        '''
        set_position --
            Updates the position of the card
        '''
        self.x = x
        self.y = y
        self.turtle.goto(x, y)

    def flip(self):
        '''
        flip()--
            Flips the card to show the front or back image
        '''
        if self.is_flipped:
            # flip to back
            self.turtle.shape(self.cover)  
            self.is_flipped = False
        else:
            # flip to the image
            self.turtle.shape(self.image)  
            self.is_flipped = True

    def hide(self):
        '''
        hide() --
            Hides the card after the cards match
        '''
        self.turtle.hideturtle()

    # handle user click
    def on_click(self, x, y):
        '''
        on_click() --
            Handles the card click event
        '''
        if not self.is_flipped and self.manage:
            self.flip()
            self.manage.card_flipped(self)
        
class Flip():
    ''' Class Flip
        Attributes: screen
        Methods: card_flipped(), check_cards(), match(),
                 reset(), etc
    '''
    def __init__(self, screen):
        '''
        Constructor -- creates an new instance
                   of Flip
        Parameters -- self - the current object
                      screen
        '''
        # List to store currently flipped cards
        self.flipped_cards = [] 

        # List of all cards in the game
        self.cards = []
        self.screen = screen

        #initial matches and guesses are zero
        self.guesses = 0
        self.matches = 0

        self.game_completed = False
        self.screen.register_shape('winner.gif')

    def card_flipped(self, card):
        '''
        card_flipped() --
            Handles a card being flipped
        '''
        self.flipped_cards.append(card)
        if len(self.flipped_cards) == 2:
            self.check_cards()

    def check_cards(self):
        '''
        check_cards() --
            Checks if the two flipped cards match
        '''
        self.guesses += 1
        self.update_status()
        card1, card2 = self.flipped_cards
        if card1.image == card2.image:
            self.match()
        else:
            self.screen.ontimer(self.reset, 1000)

    def match(self):
        '''
        match() --
            Handles a matching pair of cards
        '''
        for card in self.flipped_cards:
            # Hide the matching cards
            card.hide() 

        self.matches += 1
        self.update_status()
            
        # Clear the flipped cards list
        self.flipped_cards = []

        # to check if the game is played sompletely
        if self.matches == len(self.cards) // 2:
            self.game_completed = True
            self.display_win_msg()

    def reset(self):
        '''
        reset() --
            Flips the cards back if they don't match
        '''
        for card in self.flipped_cards:
            card.flip()

        # Clear the flipped cards list
        self.flipped_cards = []

    def update_status(self):
        '''
        update_status --
            Update the status of the game
        '''
        turtle.clear()
        # Write the current number of guesses
        turtle.penup()
        turtle.goto(-355, -275)
        turtle.write(f'Status: Guesses: {self.guesses} Matches: {self.matches}',
                     font=('Arial', 12, 'normal'))
        turtle.hideturtle()
        
    def display_win_msg(self):
        '''
        display_win_msg --
            Displays a win message after all cards are matched
        '''
        win_turtle = turtle.Turtle()
        win_turtle.penup()
        win_turtle.hideturtle()
        win_turtle.setpos(0,0)
        win_turtle.shape('winner.gif')
        win_turtle.showturtle()

        self.screen.ontimer(lambda: win_turtle.hideturtle(), 5000)

        self.screen.ontimer(turtle.bye, 5000)
