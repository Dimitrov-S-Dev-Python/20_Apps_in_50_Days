def get_todos(filepath="todos.txt"):
    """
    Read a text file
    :param filepath:
    :return: List of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """
    Write the to-do items list in the text file.
    :param todos_arg:
    :param filepath:
    :return: None
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

