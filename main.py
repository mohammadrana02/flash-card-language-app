from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

french_words_df = pd.read_csv("data/french_words.csv")
french_dict = french_words_df.to_dict(orient="records")


def new_card():
    random_card = random.choice(french_dict)
    french_word = random_card["French"]
    canvas.itemconfig(french_text, text=french_word)


#
def show_answer():
    canvas.itemconfig(front_of_card, image=back_of_card)


window = Tk()
window.config(padx=50, pady=50, bg="#B1DDC6")
window.title("Flash Card Game")

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
front_of_card = canvas.create_image(400, 263, image=card_front_image)
back_of_card = canvas.create_image(400, 263, image=card_back_image)
canvas.grid(column=0, row=0, columnspan=2)
english_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
