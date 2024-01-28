from function import get_todos, write_todos

import time
clock = time.strftime("%b %d ,%Y %H:%M:%S")
print("time is : ", clock)

while True:
    user_action = input("type add,show,edit,complete or exit: \n")
    # user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos, )

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1
            todos = get_todos()

            new_todo = input("enter new todo: ")
            todos[number - 1] = new_todo + '\n'
            write_todos(todos, )


        except ValueError:
            print("your command is not correct")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            write_todos(todos, )
            message = f"todo {todo_to_remove} was removed from the list. "
            print(message)
        except IndexError:
            print("invalid index .")
            continue

    elif 'exit' in user_action:
        break
