# To-Do List App

## Description

A simple command-line to-do list application written in Python. This app allows you to add, show, edit, complete, and reset your to-do items. The application stores the to-do items in a text file.

## Files

- **`main.py`**: The main script that runs the to-do list application.
- **`todos_function.py`**: Contains the functions for managing to-do items.
- **`storage.txt`**: A text file used for storing the to-do list data.

## Functions

### `get_user_action()`
Prompts the user for input to choose an action. It asks the user to select one of the available actions and returns the user's choice.

### `add_todo()`
Adds a new to-do item to the list. The function prompts the user to enter a new to-do, checks if it already exists, and appends it to the list if it does not.

### `show_todos()`
Displays all to-do items. It lists each to-do item with its index and prints the total number of remaining todos.

### `edit_todo()`
Edits an existing to-do item. The function prompts the user to select the index of the to-do to edit, then allows them to input a new value to replace the existing to-do item.

### `complete_todo()`
Marks a to-do item as complete (removes it from the list). The function prompts the user to select the index of the to-do item to complete and then removes it from the list.

### `reset_todos()`
Clears all to-do items. The function asks for user confirmation before removing all items from the to-do list.

### `save_todos()`
Saves the current list of to-dos to a file. It writes the contents of the to-do list to the specified file, preserving the current state of the list.


## File Handling

The application uses a text file named `storage.txt` to store the to-do items. 

- **`storage.txt`**: This file contains the list of to-do items. Each line in the file represents a separate to-do item.
- If **`storage.txt`** is not found, the application will start with an empty to-do list and create a new **`storage.txt`** file when items are added.

The application handles reading from and writing to **`storage.txt`** to ensure that the to-do list persists between runs.
