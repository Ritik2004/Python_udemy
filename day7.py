
while True:
    user_action = input("Type add,show,edit or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter') + "\n"

            file = open('todo.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

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
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input('Number of the todo to complete:'))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Hey, u entered unknown command!")

print('Bye!')
