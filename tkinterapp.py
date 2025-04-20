import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

def get_answer(answer_number):
    if answer_number == 1:
        return "you got chocolate"
    elif answer_number == 2:
        return "you got pen"
    elif answer_number == 3:
        return "you got eraser"
    elif answer_number == 4:
        return "you got cycle"
    elif answer_number == 5:
        return "you got ball"
    elif answer_number == 6:
        return "you got book"
    elif answer_number == 7:
        return "you got money"
    elif answer_number == 8:
        return "you got game"
    else:
        return "Invalid number"  # Handle unexpected input

def result():
    answer = get_answer(random.randint(1, 8))
    label.config(text=answer.capitalize())  # Display the result in the label

window = tk.Tk()
window.title("Random Gift Generator")
window.geometry("500x200+170+90")  # Set window size


gift_icon = tk.PhotoImage(file=r"C:\Desktop\CODES\resources\gift_icon.png")

gift_icon = gift_icon.subsample(20,20)    #Ruduce image by half(adjust value as needed)

button = tk.Button(
    window,
    image=gift_icon,
    compound=tk.LEFT,
    text = "Get Gift",
    # text = "Click for Gift", 
    command = result,
    bg = "lightblue",
    fg = "green",
    font= ("Century",14,"bold"),
    padx=10,
    pady=6,
    activebackground= "lightgray",
    # activeforeground= "lightpink",
    cursor= "hand2"
)
button.pack(pady=20)


name = StringVar()
entry_box = Entry(
    window, 
    textvariable=name, 
    font=("Arial", 8, "bold"),
).place(x=10, y=100)

label = ttk.Label(
    window, 
    text="▶️",
    font = ("Arial",14, "bold"),
    foreground = "blue",
    padding = 10,
)
label.pack()
window.mainloop()
