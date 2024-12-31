import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    my_label.config(text=input.get())


def new_button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)

button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=new_button_clicked)

new_button.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
 
input.grid(column=3, row=2)

window.mainloop()
