from tkinter import * 
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("800x700")
root.title("radioBtn")

def order():
    orderedItem = item.get()
    tmsg.showinfo("Order Confirmed",f"We will deliver {orderedItem} to you soon!")

item = StringVar()
item.set("")



Label(root,text="what would you like to eat?",font="Roboto 15 bold",padx=12,pady=20).pack(anchor='w')
radio = Radiobutton(root,text="Dosa",variable=item,value="Dosa").pack(anchor='w')
radio = Radiobutton(root,text="Idli",variable=item,value="Idli").pack(anchor='w')
radio = Radiobutton(root,text="Pohe",variable=item,value="Pohe").pack(anchor='w')
radio = Radiobutton(root,text="Rice",variable=item,value="Rice").pack(anchor='w')

Button(text="Confirm Order", command=order).pack()

root.mainloop()
