import function
import PySimpleGUI as sg

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add_button=sg.Button("add")
window = sg.Window("My to-Do App", layout=[label, input_box, add_button])
window.read()
window.close()
