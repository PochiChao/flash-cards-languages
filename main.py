from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    french_words = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    french_words = pd.read_csv('./data/french_words.csv')
    french_words_dict = french_words.to_dict('records')
else:
    french_words_dict = french_words.to_dict('records')

card = {}


def next_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(french_words_dict)
    canvas.itemconfig(card_shown, image=card_front)
    canvas.itemconfig(card_language, text='French', fill='black')
    canvas.itemconfig(card_word, text=card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global card
    canvas.itemconfig(card_shown, image=card_back)
    canvas.itemconfig(card_language, text='English', fill='white')
    canvas.itemconfig(card_word, text=card['English'], fill='white')


def is_known():
    global card
    french_words_dict.remove(card)
    data = pd.DataFrame(french_words_dict)
    data.to_csv('./data/words_to_learn.csv', index=False)


window = Tk()
window.title('Language Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
card_shown = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_language = canvas.create_text(400, 150, font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, font=('Arial', 60, 'bold'))
flip_timer = window.after(3000, func=flip_card)

next_word()

card_back = PhotoImage(file='./images/card_back.png')

known = PhotoImage(file='./images/right.png')
known_button = Button(image=known, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

unknown = PhotoImage(file='./images/wrong.png')
unknown_button = Button(image=unknown, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

window.mainloop()
