import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

def get_answer(answer_number):
    string = ["you got chocolate", "you got pen", "you got eraser", "you got cycle", "you got ball", "you got book", "you got money", "you got game"]
    return string[answer_number]

def result():
    answer = get_answer(random.randint(0, 7))
    label.config(text=answer.capitalize())  # Display the result in the label

window = tk.Tk()
window.title("Random Gift Generator")
window.geometry("500x250+250+90")  # Set window size


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
