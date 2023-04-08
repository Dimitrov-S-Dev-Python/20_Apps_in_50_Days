import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

convert = sg.Button("Convert")
window = sg.Window("Convertor",[[label1, input1],
                                [label2, input2],
                                [convert]])

window.read()
window.close()
