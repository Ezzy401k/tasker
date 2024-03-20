from tkinter import *
import pandas as pd

FONT = ("Arial", 15, "normal")

window = Tk()
window.title("Task Counter")
window.config(bg="dark slate gray")
window.minsize(300, 400)
window.maxsize(300, 400)


def receive():
    global data
    name_st = name_in.get()
    diff = difficulty_in.get()
    day_int = day_in.get()
    new_row = pd.DataFrame({'name': [name_st], 'diff': [diff], 'day': [day_int]})
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv("projects.csv", index=False)
    update_listbox()


def update_listbox():
    listbox.delete(0, END)  # Clear the existing content of the listbox
    projects = []
    for _, row in data.iterrows():
        d = '⭐' * int(row['diff'])
        da = int(row['day'])
        n = row['name']
        item = f"Day {da}/100, {n}, Difficulty: {d}"
        projects.append(item)
    for item in projects:
        listbox.insert(END, item)  # Insert each item into the listbox


title = Label(text="Git Hub python project", font=FONT)
title.config(foreground="white", background="dark slate gray")
title.place(x=55, y=0)

name = Label(text="Project Name:")
name.config(foreground="wheat", background="dark slate gray")
name.place(x=50, y=30)

name_in = Entry()
name_in.config(background="light slate gray")
name_in.place(x=135, y=31)

difficulty = Label(text="Difficulty:")
difficulty.config(foreground="wheat", background="dark slate gray")
difficulty.place(x=75, y=60)

difficulty_in = Spinbox(from_=1, to=5, width=5)
difficulty_in.config(background="light slate gray")
difficulty_in.place(x=135, y=61)

day = Label(text="Day:")
day.config(foreground="wheat", background="dark slate gray")
day.place(x=100, y=90)

day_in = Spinbox(from_=1, to=100, width=5)
day_in.config(background="light slate gray")
day_in.place(x=135, y=91)

data = pd.read_csv("projects.csv", index_col=False)
print(data)


save = Button(text="SAVE", command=receive)
save.config(width=10, background="dim gray", foreground="light goldenrod")
save.place(x=110, y=120)


listbox = Listbox(width=48, height=15, borderwidth=2, relief="solid")
listbox.place(x=4, y=150)

scrollbar = Scrollbar(window, orient=VERTICAL)
scrollbar.place(x=276, y=153, height=240)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

update_listbox()

window.mainloop()
