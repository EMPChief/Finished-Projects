import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")
exit_button = sg.Button("Exit")

result_label = sg.Text("", size=(20, 1))

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [button, exit_button],
          [result_label]]

sg.theme("green")

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Convert":
        feet = float(values[0])
        inches = float(values[1])
        total_inches = feet * 12 + inches
        result_label.update(f"Total inches: {total_inches}")

window.close()