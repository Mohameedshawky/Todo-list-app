from todos_function import get_user_action,add_todo,show_todos,edit_todo,complete_todo,reset_todos,save_todos

try:
    with open(r"storage.txt", 'r') as file:
        todos = file.readlines()
except FileNotFoundError:
    todos = []
    print("storage.txt not found. Starting with an empty todo list.")

while True:
    user_action = get_user_action()

    match user_action:
        case 'add':
            add_todo(todos)

        case 'show':
            show_todos(todos)
            print('=' * 20)

        case 'edit':
            edit_todo(todos)

        case 'complete':
            complete_todo(todos)

        case 'reset':
            reset_todos(todos)

        case 'exit':
            save_todos(todos, 'storage.txt')
            break

        case whatever:
            print("undefined choice please Enter only from those: ")

