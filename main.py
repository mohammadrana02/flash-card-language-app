from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    french_words_df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    french_words_df = pd.read_csv("data/french_words.csv")
    new_data_file = open("words_to_learn.csv", "a")
    new_data_file.write("French,English")
    new_data_file.close()
finally:
    french_dict = french_words_df.to_dict(orient="records")

current_card = {}


def right_button_click():
    new_card()
    remove_card()


def wrong_button_click():
    new_card()
    words_to_learn()


def remove_card():
    global current_card
    french_dict.remove(current_card)


def words_to_learn():
    data_file = open("words_to_learn.csv", "a")
    data_file.write(f"{current_card['French']},{current_card['English']}\n")
    data_file.close()


def new_card():
    # print(len(french_dict))
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(canvas_background, image=card_front_image)
    canvas.itemconfig(card_title, fill="black", text="French")
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=card_back_image)
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
    canvas.itemconfig(card_title, fill="white", text="English")


window = Tk()
window.config(padx=50, pady=50, bg="#B1DDC6")
window.title("Flash Card Game")

flip_timer = window.after(3000, func=flip_card)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_button_click)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_button_click)
wrong_button.grid(column=0, row=1)

new_card()

window.mainloop()
