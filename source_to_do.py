from tkinter import *
from tkinter import ttk as ttk
import tkinter as tk

# TODO: upload to github repo / store tasks in a database / improve ui, fix measurements / add a settings area 

# * here the window is defined standard boiler plate

root = tk.Tk()
root.title("To do...")
root.geometry("489x500")

# * here is the addition of the task in this function

arr = []

def comfirm():
    task = taskentry.get()
    taskentry.delete(0, 10000000)
  
    taskholder.insert(parent="", index="end", iid=len(arr), text="", values=(len(arr), task))

    arr.append(task)

# * gui / buttons / entry box / treeview

taskholder = ttk.Treeview(root)
taskholder["columns"] = ("ID", "Task")
taskholder.column("#0", width=0, minwidth=25)
taskholder.column("ID", anchor=W, width=30)
taskholder.column("Task", anchor=CENTER, width=150)
taskholder.heading("#0", text="", anchor=W)
taskholder.heading("ID", text="ID:", anchor=W)
taskholder.heading("Task", text="Task:", anchor=CENTER)

taskholder.place(x="0", y="0")

taskentry = tk.Entry(root, width="41")
taskentry.place(x="0", y="475")

taskcomfirm = tk.Button(root, command=comfirm, text="add task", width="15", height="1")
taskcomfirm.place(x="336", y="469")

# * toolbar creation

menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

# * menu commands

def save_text():
    None

def popup(e):
    rcmenu.tk_popup(e.x_root, e.y_root)

def settingswindow():
    settingsroot = tk.Tk()
    settingsroot.title("settings")
    settingsroot.geometry("500x500")

    colour_text = tk.Entry(settingsroot, width=20, borderwidth=5)
    colour_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    colour_text_label = tk.Label(settingsroot, text="choose your text colour:")
    colour_text_label.grid(row=0, column=0)







    settingsroot.mainloop 

# * files 

filemenu = tk.Menu(menubar)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="save as text file", command=save_text)

# * settings menu

settingsmenu = tk.Menu(menubar)
menubar.add_cascade(label="settings", menu=settingsmenu)
settingsmenu.add_command(label="settings", command=settingswindow)


# * right click menu

rcmenu = tk.Menu(root, tearoff=False)
rcmenu.add_command(label="save as text file", command=save_text)

root.bind("<Button-3>", popup)

# * boilerplate

root.mainloop()