while True:
    user_action = input("Type add, show, complete edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}.{item.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {todo_to_remove} was removed from the list.")

        except IndexError:
            print("There is no item with taha number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
