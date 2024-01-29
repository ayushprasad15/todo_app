import PySimpleGUI as sg

label = sg.Text("enter feet: ")
input_box = sg.InputText(tooltip="feets")

label_i = sg.Text("enter inches: ")
input_box_i = sg.InputText(tooltip="inches")

convert = sg.Button("convert")

window = sg.Window("my convertor", layout=[[label, input_box], [label_i, input_box_i], [convert]])


window.read()
window.close()