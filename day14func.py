def get_todos(filepath="todo.txt"):
    """Read a text file and return the list of 
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todo(todos,filepath = "todo.txt"):
    """write the to-do item in list"""
    with open(filepath, 'w') as file:
        file.writelines(todos)

