todos = []

while True:
    user_action = input("Type add, show, complete edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}.{item}")

        case "edit":
            number = int(input("Number of todo to edit: "))
            index = number - 1
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo

        case "complete":
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break

print("Bye!")
