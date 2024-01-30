# import functions
import PySimpleGUI as sg

label = sg.Text("select file to compress: ")
input_box = sg.InputText(tooltip="enter path/select file")
add_button = sg.FileBrowse("choose")

label_d = sg.Text("select destination folder ")
input_box_d = sg.InputText(tooltip="select destination")
add_button_d = sg.FolderBrowse("choose")

button_compress = sg.Button("compress")

window = sg.Window("file zipper",
                   layout=[[label_d, input_box, add_button, [label, input_box_d, add_button_d]], [button_compress]])

window.read()
window.close()
