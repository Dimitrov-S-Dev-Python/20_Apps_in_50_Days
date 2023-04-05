todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)

        case "edit":
            number = int(input("Number of todo to edit: "))
            index = number - 1
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo
        case "exit":
            break

print("Bye!")
