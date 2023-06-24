from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry('900x750')
root.title("News App")

heading = Label(text="Welcome to Appu News",font="serif 20 bold",padx=30 ,pady=14)
heading.pack();


mainFrame = Frame(root,bg='green',borderwidth=3)
mainFrame.pack(anchor='w',fill='both')


image_labels = []
photo_images = []  # Add a list to store the PhotoImage objects
text_labels = []
frames = []
for i in range(1, 5):
    frame = Frame(mainFrame,bg="green",borderwidth=4,)
    frame.pack(side=TOP,anchor='nw',pady=3,);
    frames.append(frame)
    
    image_load = Image.open(f"{i}.png")
    newsize = (200, 150)
    resized_image = image_load.resize(newsize)
    photo_image = ImageTk.PhotoImage(resized_image)
    photo_images.append(photo_image)  # Store the PhotoImage objects
    image_label = Label(frame, image=photo_image)
    image_label.pack(pady=10,side=LEFT)
    image_labels.append(image_label)  # Add the label to the list
   
    
    
    
    with open(f"{i}.txt") as file:
        file_content = file.read();
        text_label = Label(frame,text=file_content,wraplength=1200);
        text_label.pack(side=RIGHT,padx=10)
        text_labels.append(text_label)
        



root.mainloop();
