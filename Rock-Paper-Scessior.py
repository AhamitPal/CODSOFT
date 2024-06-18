import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    play_again_button.pack()

def play_again():
    result_label.config(text="")
    play_again_button.pack_forget()


root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")


tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16)).pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", font=("Arial", 14),bg='Orange', command=lambda: determine_winner("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", font=("Arial", 14),bg='orange', command=lambda: determine_winner("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", font=("Arial", 14),bg='orange', command=lambda: determine_winner("Scissors")).grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

play_again_button = tk.Button(root, text="Play Again", font=("Arial", 14),bg='Lightblue', command=play_again)


root.mainloop()
