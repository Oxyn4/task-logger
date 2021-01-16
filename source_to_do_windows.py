from tkinter import *
from tkinter import ttk as ttk
from tkinter import filedialog
import tkinter as tk



# TODO: upload to github repo / store tasks in a database / improve ui, fix measurements / add a settings area 
# TODO: store tasks in a dat file / improve ui, fix measurements / need to add settings to mentubar 
# TODO: remove task feature

# * here the window is defined standard boiler plate

root = tk.Tk()
root.geometry("495x276")
root.title("Task Logger - New File ")

# * here is the addition of the task in this function

arr = []

def comfirm(e):
    task = taskentry.get()
    taskentry.delete(0, 10000000)
  
    taskholder.insert(parent="", index="end", iid=len(arr), text="", values=(len(arr), "• " + task))

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

taskcomfirm = tk.Button(root, command=lambda: comfirm(0), text="add task", width="25", height="1")
taskcomfirm.place(x="270", y="221")

taskremove = tk.Button(root, command=remove, text="remove selected task", width="25", height="1")
taskremove.place(x="0", y="221")

# * toolbar creation

menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

# * menu commands

def new_list():
    for record in taskholder.get_children():
        taskholder.delete(record)
        arr.clear()
        titlestatus = "New file"

def save_as_text(e):
    file_to_be_saved = tk.filedialog.asksaveasfilename(defaultextension=".txt", initialdir="This PC/Documents", title="Save File", filetypes=[("Text Files", "*,txt")])
    if file_to_be_saved:
        name = file_to_be_saved
        root.title(f'Task logger - {file_to_be_saved}' )  

    file_to_be_saved = open(file_to_be_saved, "w")

    for items in arr:
        file_to_be_saved.write(str(items) + "\n")
        

    file_to_be_saved.close()
    

def popup(e):
    rcmenu.tk_popup(e.x_root, e.y_root) 

def open_file():
    new_list()

    importedfile = tk.filedialog.askopenfilename(initialdir="~/Documents", title="Open File", filetypes=[("Text Files", "*.txt")])
    file = importedfile
    root.title(f'Task logger - {file}' )   

    file2 = open(file, 'r')
    line = file2.readline() 
    linecount = 0

    while line:    
        print(line)

        taskholder.insert(parent="", index="end", iid=len(arr), text="", values=(len(arr), "• " + line))
        line = file2.readline() 
        linecount += 0
        arr.append(line)

def openhelpdocs():
    pass

def keydelete(e):
    selec = taskholder.selection()[0]
    taskholder.delete(selec)
    arr.pop(int(selec))

def settingswindow():
    settingsroot = tk.Tk()
    settingsroot.title("settings")
    settingsroot.geometry("260x250")

    r = IntVar()

    theme_selection = tk.Label(settingsroot, text="choose your theme:")
    theme_selection.grid(row=0, column=1)

    Radiobutton(settingsroot, text="dark", variable=r, value=1).grid(column=0, row=1)
    Radiobutton(settingsroot, text="light", variable=r, value=2).grid(column=1, row=1)
    Radiobutton(settingsroot, text="blue", variable=r, value=3).grid(column=2, row=1)

    theme_selection = tk.Label(settingsroot, text="choose your font size:")
    theme_selection.grid(row=4, column=1)

    Radiobutton(settingsroot, text="Small", variable=r, value=1).grid(column=0, row=5)
    Radiobutton(settingsroot, text="Medium", variable=r, value=2).grid(column=1, row=5)
    Radiobutton(settingsroot, text="Large", variable=r, value=3).grid(column=2, row=5)

    settingsroot.mainloop()

# * files 

filemenu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="New list", command=new_list)
filemenu.add_command(label="Save as text file", command=save_as_text)
filemenu.add_command(label="Open text file", command=open_file)

# * help 

helpmenu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="Documentation", command=openhelpdocs)

# * settings menu

settingsmenu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="settings", menu=settingsmenu)
settingsmenu.add_command(label="settings", command=settingswindow)

# * right click menu

rcmenu = tk.Menu(root, tearoff=False)
rcmenu.add_command(label="save as text file", command=save_as_text)

# * keybinds

root.bind("<Delete>", keydelete)
root.bind("<Button-3>", popup)
root.bind("<BackSpace>", keydelete)
root.bind("<Return>", comfirm)
root.bind("<Control-s>", save_as_text)
root.bind("<Control-o>", open_file)

# * boilerplate

root.mainloop()