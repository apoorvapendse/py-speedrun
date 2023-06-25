from tkinter import *
import tkinter.messagebox as tsmg
root = Tk()
root.geometry("800x700")
root.title("slider")

def withdraw():
    money = slider.get()
    tsmg.showinfo("Success!",f"{money} dollars have been credited")
    with open("money.txt","a") as file:
        file.write(f"{money}\n");
        

Label(root,text="select the amount").pack()
slider = Scale(root,from_=0 , to=100,orient='vertical',tickinterval=20)
slider.pack()
Button(root,text="Withdraw Amount",command=withdraw).pack(pady=20)

root.mainloop()
