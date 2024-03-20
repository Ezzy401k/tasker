
# Task Counter

This Python program provides a graphical user interface (GUI) for managing project details. It allows users to input project names, difficulties, and days completed, and saves the information to a CSV file. The GUI displays the existing projects in a listbox with formatting based on difficulty and completion progress.

## How it Works

1. The user inputs project details (name, difficulty, and day) using entry widgets and spinboxes.
2. Upon clicking the "SAVE" button, the program saves the project details to a CSV file and updates the listbox with the new project information.
3. The listbox displays each project's name, difficulty level represented by stars, and completion progress.

## Features

- Input fields for project name, difficulty, and day.
- Saving project details to a CSV file.
- Displaying project details in a listbox with formatting.
- Scrollbar for navigating through the list of projects.

## Requirements

- Python 3
- pandas library (for data manipulation)
- Tkinter library (for GUI)

## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the pandas library using pip:

```bash
pip install pandas
```

3. Clone the repository:

```bash
git clone https://github.com/Ezzy401k/tasker.git
```

4. Navigate to the project directory:

```bash
cd tasker
```

5. Run the program:

```bash
python tasker.py
```

6. Enter the project details in the respective input fields.
7. Click the "SAVE" button to save the project details.
8. View the updated list of projects in the listbox.

## Author

[Esrael Mekdem](https://github.com/Ezzy401k)
