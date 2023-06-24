from tkinter import *
root = Tk()

root.title("canvas")
canvasWidth = 800
canvasHeight = 500
root.geometry(f"{canvasWidth}x{canvasHeight}")

canvas_widget = Canvas(root,height=canvasHeight, width=canvasWidth, bg="green");
canvas_widget.pack()

# canvas_widget.create_line(0,0,800,300,fill="white")

canvas_widget.create_rectangle(400,200,500,300)
# rectangle takes coordinates of top left and bottom right

# canvas_widget.create_text(300,300,text="hello canvas text")

# oval is always present inside a rectangle and we supply the top left and bottom right coordinates of that rectangle
canvas_widget.create_oval(4,4,600,300,fill="white")


root.mainloop()
