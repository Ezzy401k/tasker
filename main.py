from tkinter import *
import pandas as pd

# Define a font
FONT = ("Arial", 15, "normal")

# Create the main tkinter window
window = Tk()
window.title("Task Counter")  # Set the title of the window
window.config(bg="dark slate gray")  # Set the background color of the window
window.minsize(300, 400)  # Set the minimum size of the window
window.maxsize(300, 400)  # Set the maximum size of the window


# Function to receive project details from the user
def receive():
    global data  # Access the global variable 'data'
    name_st = name_in.get()  # Get the project name from the entry widget
    diff = difficulty_in.get()  # Get the difficulty from the spinbox
    day_int = day_in.get()  # Get the day from the spinbox
    # Create a new row with the project details
    new_row = pd.DataFrame({'name': [name_st], 'diff': [diff], 'day': [day_int]})
    # Concatenate the new row with the existing data and save to CSV
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv("projects.csv", index=False)  # Save the updated data to a CSV file
    update_listbox()  # Update the listbox to reflect the changes


# Function to update the listbox with project details
def update_listbox():
    listbox.delete(0, END)  # Clear the existing content of the listbox
    projects = []
    # Iterate over each row in the data and format the project details
    for _, row in data.iterrows():
        d = '⭐' * int(row['diff'])  # Construct stars based on the difficulty level
        da = int(row['day'])  # Get the project day
        n = row['name']  # Get the project name
        # Format the project details string
        item = f"Day {da}/100, {n}, Difficulty: {d}"
        projects.append(item)  # Append the formatted string to the projects list
    for item in projects:
        listbox.insert(END, item)  # Insert each item into the listbox


# Create labels, entry widgets, and spinboxes for project details input
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

# Read data from the CSV file
data = pd.read_csv("projects.csv", index_col=False)
print(data)  # Print the data to verify

# Create a button to save project details
save = Button(text="SAVE", command=receive)
save.config(width=10, background="dim gray", foreground="light goldenrod")
save.place(x=110, y=120)

# Create a listbox to display project details
listbox = Listbox(width=48, height=15, borderwidth=2, relief="solid")
listbox.place(x=4, y=150)

# Create a scrollbar for the listbox
scrollbar = Scrollbar(window, orient=VERTICAL)
scrollbar.place(x=276, y=153, height=240)

# Configure listbox to use the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Update the listbox with existing project details
update_listbox()

# Run the tkinter event loop
window.mainloop()
