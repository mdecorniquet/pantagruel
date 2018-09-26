import PySimpleGUI as sg

with sg.FlexForm('Select File to import') as form:
    form_rows = [
                 [sg.Text('Nom du fichier')],
                 [sg.Input(), sg.FileBrowse()],
                 [sg.OK(), sg.Cancel()]
                ]
    (button, (filename,)) = form.LayoutAndRead(form_rows)

print(button, filename)