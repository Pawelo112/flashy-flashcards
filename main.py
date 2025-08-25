from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas - Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0)
flash_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flash_card_image)
canvas.grid(row=0, column=0, columnspan=1)

window.mainloop()
