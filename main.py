from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- VARIABLES ------------------------------- #
# Checking if learning file exist
# if not - read from main file
try:
    words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pd.read_csv("data/french_words.csv")

# Transforming DataFrame to a list of dictionaries
words_to_learn = words_data.to_dict(orient='records')
word = {}
side = 'front'


# ---------------------------- FLASH CARDS MECHANISM ------------------------------- #
def generate_card():
    """Generates and displays new flash card."""
    global word, side

    word = random.choice(words_to_learn)

    # Card is always displayed front first
    canvas.itemconfig(displayed_word, text=word['French'], fill='black')
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(main_image, image=card_front_image)
    side = 'front'


def generate_card_and_update_words():
    """Generates and displays new flash card.
    Additionally, removes current word from learning list."""
    global word, side

    # Removing learned word from a list
    words_to_learn.remove(word)
    updated_words_data = pd.DataFrame(words_to_learn)
    updated_words_data.to_csv('data/words_to_learn.csv', index=False)

    # Generating new card with updated list of words
    generate_card()


def flip_card():
    """Flips the current flash card."""
    global side

    if side == 'front':
        canvas.itemconfig(main_image, image=card_back_image)
        canvas.itemconfig(title, text='English', fill='white')
        canvas.itemconfig(displayed_word, text=word['English'], fill='white')
        side = 'back'

    else:
        canvas.itemconfig(main_image, image=card_front_image)
        canvas.itemconfig(title, text='French', fill='black')
        canvas.itemconfig(displayed_word, text=word['French'], fill='black')
        side = 'front'


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas - Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file='images/card_back.png')
main_image = canvas.create_image(400, 263, image=card_front_image)
# Flash Card text
title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
displayed_word = canvas.create_text(400, 263, text='',
                                    font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=3)

# Buttons
correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, compound='center',
                        bd=0, command=generate_card_and_update_words)
correct_button.grid(row=1, column=2)

flip_image = PhotoImage(file='images/flip.png')
flip_button = Button(image=flip_image, background=BACKGROUND_COLOR, highlightthickness=0, compound='center',
                     bd=0,  command=flip_card)
flip_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, compound='center', bd=0, command=generate_card)
wrong_button.grid(row=1, column=0)

generate_card()
window.mainloop()
