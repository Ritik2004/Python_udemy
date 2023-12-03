todos = []
while True:
    user_action = input("Type add,show or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, u entered unknown command!")

print('Bye!')
