import tkinter
import tkinter.ttk


root = tkinter.Tk()
root.geometry("300x300")

def raise_frame(self):
    tkinter.Frame.tkraise(self)

### MENU BAR ###
menu_bar = tkinter.Menu(root)

### File Menu ###
file_menu = tkinter.Menu(menu_bar)
file_menu.add_command(label="Open")
file_menu.add_command(label="Quit")
menu_bar.add_cascade(label="File", menu=file_menu)

### USERS MENU ###
users_menu = tkinter.Menu(menu_bar)
users_menu.add_command(label="New User")
users_menu.add_command(label="Edit User")
users_menu.add_command(label="Delete User")
menu_bar.add_cascade(label="Users", menu=users_menu)

#####
root.config(menu=menu_bar)
#####


f1 = tkinter.Frame(root)
f2 = tkinter.Frame(root)
f3 = tkinter.Frame(root)
f4 = tkinter.Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

b1 = tkinter.Button(f1, text="Frame 2", command=lambda:raise_frame(f2)).pack()
label_1 = tkinter.Label(f1, text="Frame 1").pack()

b2 = tkinter.Button(f2, text="Frame 3", command=lambda:raise_frame(f3)).pack()
label_2 = tkinter.Label(f2, text="Frame 2").pack()


raise_frame(f1)
root.mainloop()
