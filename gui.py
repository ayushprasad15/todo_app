import PySimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter todo.txt", key="todo.txt ")
add_button = sg.Button("add")
window = sg.Window("My to-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("arial", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break


window.close()
