from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- FLASH CARDS MECHANISM ------------------------------- #
words_data = pd.read_csv("data/french_words.csv")

# Transforming DataFrame to a list of dictionaries
words = words_data.to_dict(orient='records')


def generate_word():
    """Generates and displays random word on the flash card,
    after pushing the button."""
    word = random.choice(words)['French']
    canvas.itemconfig(displayed_word, text=word)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas - Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
# Flash Card text
title = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
displayed_word = canvas.create_text(400, 263, text=f'{random.choice(words)["French"]}', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, compound='center', bd=0, command=generate_word)
correct_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, compound='center', bd=0, command=generate_word)
wrong_button.grid(row=1, column=0)

window.mainloop()
