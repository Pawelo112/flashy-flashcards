from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas - Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0)
flash_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 260, image=flash_card_image)
# Flash Card text
canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, compound='center', bd=0)
correct_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, compound='center', bd=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
