import tkinter as tk

def get_class():  #no need to pass arguments to functions in both cases
    print (var.get())

def get_entry(): 
    print (ent.get())


root = tk.Tk()

var = tk.StringVar()

ent = tk.Entry(root,textvariable = var)
btn1 = tk.Button(root, text="Variable Class", command=get_class)
btn2 = tk.Button(root, text="Get Method", command=get_entry)

ent.pack()
btn1.pack()
btn2.pack()

root.mainloop()
