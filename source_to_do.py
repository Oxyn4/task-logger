import tkinter as tk

# TODO: upload to github repo / store tasks in a database / improve ui, fix measurements / add a settings area

# * here the window is defined standard boiler plate

root = tk.Tk()
root.title("To do...")
root.geometry("489x500")

# * here is the addition of the task in this function

def comfirm():
    task = taskentry.get()
    taskentry.delete(0, 10000000)

    taskarray = [""]

    length = len(taskarray)
    
    taskholder.insert(length, "•" + task)

    taskarray.append(task)

# * gui / buttons / entry box / listbox

taskholder = tk.Listbox(root, width=60, height=25)
taskholder.place(y=0, x=0)

taskentry = tk.Entry(root, width="41")
taskentry.place(x="0", y="475")

taskcomfirm = tk.Button(root, command=comfirm, text="add task", width="15", height="1")
taskcomfirm.place(x="336", y="469")

# * standard tkinter boiler plate

root.mainloop()