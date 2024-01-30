import PySimpleGUI as sg
from inches_mind import convert

label1 = sg.Text("enter feet")
input_block1 = sg.Input(key="feet")

label2 = sg.Text("enter inches")
input_block2 = sg.Input(key="inches")

convert_button = sg.Button("convert")
output_label = sg.Text("",key="output")

window = sg.Window("convertor", layout=[[label1, input_block1], [label2, input_block2], [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


# window.read()
window.close()
