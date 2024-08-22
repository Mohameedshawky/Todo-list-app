def get_user_action():
    user_action = input("add, show, edit, complete, reset or exit :")
    user_action = user_action.strip().lower()
    return user_action


def save_todos(todos, fileName):
    with open(fileName, 'w') as file:
        file.writelines(todos)
    print("Your todos have been saved. Don't forget to come back later.")
    print('=' * 20)


def _show_todos(todos):
    for index, todo in enumerate(todos):
        todo = todo.strip('\n')
        print(f"{index + 1}){todo}")


def _get_todo_index(todos, status):
    match status:
        case 'edit':
            print("Choose which number of todo to edit :")
        case 'complete':
            print("Enter which number of todo is finished:")
    while True:
        _show_todos(todos)
        index = input()
        try:
            index = int(index)
            if not (index >= 1 and index <= len(todos)):
                raise IndexError
        except ValueError:
            print(f"Enter only a number of your todo to {status}")
            continue
        except IndexError:
            print("Enter a valid value number of todo")
            continue
        break
    return index


def add_todo(todos):
    todo = input("Enter a todo :").strip().capitalize() + '\n'
    if todo in todos:
        print(f"This todo: '{todo.strip()}' already exists in your todo list.")
        return
    todos.append(todo)
    print("Todo added successfully.")


def show_todos(todos):
    if todos:
        _show_todos(todos)
        print(f"You have {len(todos)} todos left.")
    else:
        print("You have no todos.")


def edit_todo(todos):
    index = _get_todo_index(todos, 'edit')
    confirmation = input("Are you sure you want to edit this todo? Press 'YES' to confirm or 'NO' to discard: ").strip().lower()
    if confirmation in ('yes', 'y'):
        new_todo = input("Enter a new  todo :").strip().capitalize() + '\n'
        todos[index - 1] = new_todo
        print("Todo edited successfully.")
    elif confirmation in ('no', 'n'):
        print("Edit canceled.")
    print("successfully")


def complete_todo(todos):
    index = _get_todo_index(todos, 'complete')
    completed_todo = todos.pop(index - 1).strip()
    print(f"'{completed_todo}' was completed successfully.")


def reset_todos(todos):
    confirmation = input("Are you sure? This will delete all your todos. Press 'YES' to confirm or 'NO' to discard: ").strip().lower()
    if confirmation in ('yes', 'y'):
        todos.clear()
        print("All todos have been deleted.")
    elif confirmation in ('no', 'n'):
        print("Reset canceled.")
