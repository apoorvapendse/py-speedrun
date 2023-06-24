from tkinter import *
root = Tk()
root.geometry("800x700")
root.title("Form")

def getData():
    print(name.get(),country.get(),gender.get(),age.get(),isStudent.get())
    with open("data.txt",'a') as file:
        file.write(f"{name.get()} {country.get()} {gender.get()} {str(age.get())} {str(isStudent.get())}\n");



heading = Label(text="Welcome to XYZ Form",font="Roboto 15 bold").grid(column=2);
nameLabel = Label(text="Name",).grid(row=1,column=1);
countryLabel = Label(text="Country",).grid(row=2,column=1);
genderLabel = Label(text="Gender",).grid(row=3,column=1);
ageLabel = Label(text="Age",).grid(row=4,column=1);

name = StringVar()
country = StringVar()
gender = StringVar()
age = IntVar()
isStudent = BooleanVar()

nameEntry = Entry(root,textvariable=name).grid(row=1,column=2)
countryEntry = Entry(root,textvariable=country).grid(row=2,column=2)
genderEntry = Entry(root,textvariable=gender).grid(row=3,column=2)
ageEntry = Entry(root,textvariable=age).grid(row=4,column=2)



StudentCheck = Checkbutton(text="Are you a student?",variable=isStudent).grid(row=5,column=2)

submitBtn = Button(text='submit form' ,command=getData).grid(row=6,column=2)



root.mainloop()