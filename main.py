import FreeSimpleGUI as sg
import functions as f


tasks = f.get_tasks()

sg.theme('Black')

layout = [[sg.Text('To-Do List')], [sg.InputText(tooltip='Enter a task', key='Input'), sg.Button('Add', key='Add')],
          [sg.Listbox(values=tasks, key='List', enable_events=True, size=(40,10))], [sg.Button('Complete', key='Complete'),
          sg.Button('Edit', key='Edit'), sg.Button('Exit', key='Exit')],
          ]

window = sg.Window('To-Do List', layout=layout)

while True:
    f.readFile()
    event, values = window.read()
    match event:
        case 'List':
            marked_task = values['List'][0]
            window['Input'].update(value=marked_task)

        case sg.WIN_CLOSED:
            break

        case 'Add':
            new_task = values['Input']
            if new_task != '':
                tasks.append(new_task)
                window['Input'].update('')
                f.write_tasks(tasks)
                window['List'].update(values=tasks)

        case 'Complete':
            try:
                wanted_task = values['List'][0]
                tasks.remove(wanted_task)
                window['List'].update(values=tasks)
                window['Input'].update('')
                f.write_tasks(tasks)
            except IndexError:
                sg.popup('Please pick a task', font=('Helvetica', 12))

        case 'Edit':
            try:
                wanted_task = values['List'][0]
                new_task = values['Input']
                if new_task != '':
                    index = tasks.index(wanted_task)
                    tasks[index] = new_task
                    window['List'].update(values=tasks)
                    window['Input'].update('')
                    f.write_tasks(tasks)
            except IndexError:
                sg.popup('Please pick a task', font=('Helvetica', 12))

        case 'Exit':
            break

window.close()
