
while True:
    user_action = input("Type add,show,edit or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter') + "\n"

            # file = open('todo.txt','r')
            # todos = file.readlines()
            # file.close()

            #below is the better approach to write above logic
            with open("todo.txt", 'r') as file:
                todos = file.readlines()
            todos.append(todo)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todo.txt','r') as file:
               todos = file.readlines()

            # Below approaches are used to remove '/n' after every entry
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            #below is a list comprehension approach
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number-1

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Number of the todo to complete:'))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print("Hey, u entered unknown command!")

print('Bye!')
