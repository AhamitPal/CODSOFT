import tkinter as tk

def update_expression(value):
    current_text=expression.get()
    expression.set(current_text+str(value))

def evaluate_expression():
    try:
      current_text=expression.get()
      result=eval(current_text)
      expression.set(result)
    except Exception as e:
       expression.set("Error")

def clear_expression():
    expression.set("")

root=tk.Tk()
root.title("Calculator")
expression=tk.StringVar()

expression_entry=tk.Entry(root,textvariable=expression ,font=('Times New Roman',24), bg='lightgrey',insertwidth=2, width=14, borderwidth=4)
expression_entry.grid(row=0,column=0,columnspan=4)

buttons=[
   '7','8','9','/',
   '4','5','6','*',
   '1','2','3','-',
   '0','.','=','+'



]

row_value= 1
col_value=0

for button in buttons:
   if button=='=':
      button_object=tk.Button(root,text=button,command=evaluate_expression, font=('Times New',18),padx=20,pady=20,bg='lightgrey')
   else:
      button_object=tk.Button(root,text=button,command=lambda b= button: update_expression(b), font=('Times New Roman',18),padx=20,pady=20, bg='lightgrey')
   button_object.grid(row=row_value,column=col_value,sticky="nsew")
   col_value+=1
   if col_value>3:
      col_value=0
      row_value+=1

clear_button=tk.Button(root,text="Clear",command=clear_expression, font=('Times New',18),padx=20,pady=20,bg='Lightgrey')
clear_button.grid(row=row_value, column=0, columnspan=4, sticky="nsew")


for i in range(5):
   root.grid_rowconfigure(i,weight=1)
for i in range(4):
   root.grid_columnconfigure(i,weight=1)

root.mainloop()
   
      
