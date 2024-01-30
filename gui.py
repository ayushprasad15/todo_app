import PySimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter todo.txt", key="todo")
add_button = sg.Button("add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("edit")

window = sg.Window("My to-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("arial", 20))
"""should be remember key should be equal to values['anything you write'] """
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos' :
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
