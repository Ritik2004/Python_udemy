from day14func import get_todos, write_todo

while True:
    user_action = input("Type add,show,edit or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todo(todos)

    elif user_action.startswith("show"):
        
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todo(todos)

        except ValueError:
            print("Your command is not value")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            iAndex = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index) 

            write_todo(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item at that number")
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, u entered unknown command!")

print('Bye!')
