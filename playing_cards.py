import turtle as t
import random
from game_base import user_number
from card import Cards
from card import Flip

def get_cards(cfg_file):
    '''
        get_cards() --
            create a list of the images name in a
            file
        Parameters --
            cfg_file - .txt file
        Return --
            list of strings
        '''
    img_lst = []
    with open(cfg_file, 'r', encoding = 'utf=8') as images:
        for line in images:
            img_lst.append(line)

    for i in range(len(img_lst)):
        img_lst[i] = img_lst[i].replace('\n', '')

    return img_lst

def double_elements(lst):
    '''
        double_elements() --
            doubles the elements of a list
        Parameters --
            lst - list
        Return --
            list of strings
    '''    
    doubled_lst = []
    for item in lst:
        doubled_lst.extend([item, item])
        
    return doubled_lst

def playing_deck():
    '''
        playing_deck() --
            creates a shuffled deck based on user input
            for number of cards to play with
        Return --
            list of strings
    '''  
    # number of cards to play with
    DEFAULT_SET = 'images.txt'
    card_lst = get_cards(DEFAULT_SET)
    num_img = int(user_number()) / 2
    selected_img = random.sample(card_lst, int(num_img))

    # creating duplicate image to form a pair
    selected_img = double_elements(selected_img)

    #shuffling selected images
    random.shuffle(selected_img)

    return selected_img

def display_cards(handler):
    '''
        display_cards() --
            displays the card objects at specific location
            on the game board based on the card number input 
        Parameter --
            handler - manages the game logic for
                      fro class Cards
        Return -- None
    '''
    image_lst = playing_deck()

    line1 = image_lst[0:4]
    line2 = image_lst[4:8]
    line3 = image_lst[8:]

    rows = [line1, line2, line3]
    
    COVER = "card_back.gif"
    cards_lst = []
    x = - 300
    y = 210
    
    for line in rows:
        x = -295
        for img in range(len(line)):
            image = Cards(x, y, line[img], COVER, manage = handler)
            cards_lst.append(image)
            handler.cards.append(image)
            x = x + 110
        y = y - 160

















