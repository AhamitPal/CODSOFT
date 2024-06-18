import tkinter as tk
from tkinter import messagebox
import random

def winner(user_choice):
    options=["Rock","Paper","Scissor"]
    computer_choice=random.choice(options)
    result=""
    if user_choice==computer_choice:
        result="Tie"
    elif (user_choice=="Rock" and computer_choice=="Scissor") or (user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Scissor" and computer_choice=="Paper"):
        result="You Win!"
    else:
        result="You Lose!"

    messagebox.showinfo("Result",f"Your choice:{user_choice}\n Computer's choice:{computer_choice}\n\n {result}")

def on_button_click(choice):
    winner(choice)

root=tk.Tk()

root.title("Rock, Paper, Scissor Game")

rock_button=tk.Button(root,text="Rock",command=lambda:on_button_click("Rock"), width=60, height=2, bg='red')

paper_button=tk.Button(root,text="Paper",command=lambda:on_button_click("Paper"), width=60, height=2,bg='green')

scissor_button=tk.Button(root,text="Scissor",command=lambda:on_button_click("Scissor"), width=60, height=2,bg='blue')

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissor_button.pack(pady=10)

root.mainloop()


                        