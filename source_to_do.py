from tkinter import *
from tkinter import ttk as ttk
import tkinter as tk

# TODO: upload to github repo / store tasks in a dat file / improve ui, fix measurements / need to add settings to mentubar 
# TODO: remove task feature

# * here the window is defined standard boiler plate

root = tk.Tk()
root.title("Task Logger")
root.geometry("495x276")

# * here is the addition of the task in this function

arr = []

def comfirm():
    task = taskentry.get()
    taskentry.delete(0, 10000000)
  
    taskholder.insert(parent="", index="end", iid=len(arr), text="", values=(len(arr), "• " +task))

    arr.append(task)

def remove():
    taskfordeletion = taskholder.selection()[0]
    taskholder.delete(taskfordeletion)
    print(taskfordeletion)
    arr.pop(int(taskfordeletion))

# * gui / buttons / entry box / treeview

taskholder = ttk.Treeview(root)
taskholder["columns"] = ("ID", "Task")
taskholder.column("#0", width=0, minwidth=25)
taskholder.column("ID", anchor=W, width=30)
taskholder.column("Task", anchor=CENTER, width=470)
taskholder.heading("#0", text="", anchor=W)
taskholder.heading("ID", text="ID:", anchor=W)
taskholder.heading("Task", text="Task:", anchor=CENTER)

taskholder.place(x="0", y="0")

taskentry = tk.Entry(root, width="61")
taskentry.place(x="0", y="252")

taskcomfirm = tk.Button(root, command=comfirm, text="add task", width="25", height="1")
taskcomfirm.place(x="270", y="221")

taskremove = tk.Button(root, command=remove, text="remove selected task", width="25", height="1")
taskremove.place(x="0", y="221")

# * toolbar creation

menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

# * menu commands

def save_text():
    None

def popup(e):
    rcmenu.tk_popup(e.x_root, e.y_root)    

def opendocs():
    pass

# * files 

filemenu = tk.Menu(menubar)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="save as text file", command=save_text)

# * help 

helpmenu = tk.Menu(menubar)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="Documentation", command=opendocs)

# * settings menu

settingsmenu = tk.Menu(menubar)
menubar.add_cascade(label="settings", menu=settingsmenu)

# * right click menu

rcmenu = tk.Menu(root, tearoff=False)
rcmenu.add_command(label="save as text file", command=save_text)

root.bind("<Button-3>", popup)

# * boilerplate

root.mainloop()