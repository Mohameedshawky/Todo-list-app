# To-Do List App

## Description

A simple command-line to-do list application written in Python. This app allows you to add, show, edit, complete, and reset your to-do items. The application stores the to-do items in a text file.

## Files

- **`main.py`**: The main script that runs the to-do list application.
- **`todos_function.py`**: Contains the functions for managing to-do items.
- **`storage.txt`**: A text file used for storing the to-do list data.

## Features

- **Add To-Do Items**: Allows users to add new items to their to-do list. Duplicate items are detected and not added again.
- **Show To-Do Items**: Displays all current to-do items with their indices and the number of remaining todos.
- **Edit To-Do Items**: Lets users edit an existing to-do item by selecting its index and providing a new value.
- **Complete To-Do Items**: Marks a to-do item as complete by removing it from the list.
- **Reset To-Do List**: Clears all items from the to-do list after user confirmation.
- **Persistent Storage**: Uses a text file (`storage.txt`) to save and load the list of to-dos, ensuring data is preserved between sessions.

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


## Error Handling

The application includes basic error handling to manage user input and file operations:

- **File Not Found**: If **`storage.txt`** is not found when the application starts, it initializes an empty to-do list and prints a message informing the user.
- **Invalid Input**: When the user provides invalid input for editing or completing a to-do item (e.g., non-numeric values or out-of-range indices), the application displays an error message and prompts the user to enter valid input.
- **Confirmation Prompts**: Before resetting the to-do list or editing an item, the application asks for user confirmation to prevent accidental data loss.
