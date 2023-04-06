while True:
    user_action = input("Type add, show, complete edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}.{item.capitalize()}")

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
