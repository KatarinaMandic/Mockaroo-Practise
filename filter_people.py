from classes.DB import DB
import PySimpleGUI as sg

sg.theme('DarkAmber')

countries = DB.select_distinct_countries()

main_layout = [
    [sg.Text('Country', size = (8,1)),
     sg.Combo(countries, key = '_COMBO_COUNTRY_', default_value=countries[0])],
    [sg.Text('Name', size = (8,1)),
     sg.Radio('Ascending', group_id="g1", key = '_RB_ASC_', default=True),
     sg.Radio('Descending', group_id="g1", key = '_RB_DESC_')],
    [sg.Button('Filter', key = '_FILTER_COUNTRY_')],
    [sg.Listbox([], key = '_LIST_RESULTS_', size = (35,7))],
    [sg.Button('Details', key = '_DETAILS_')]
]

details_layout = [
    [sg.Button('Back', key = '_BACK_')],
    [sg.Text('First Name', size = (8,1)),
     sg.InputText('', key='_FN_')],
    [sg.Text('Last Name', size = (8,1)),
     sg.InputText('', key='_LN_')],
    [sg.Text('E-mail', size = (8,1)),
     sg.InputText('', key='_EM_')],
    [sg.Text('Location', size = (8,1)),
     sg.InputText('', key='_LOC_')],
    [sg.Text('Birthday', size = (8,1)),
     sg.InputText('', key='_BD_')],
    [sg.Text('AVG Salary', size = (8,1)),
     sg.InputText('', key='_AVGS_')]
]

all_layouts = [
    [
        sg.Column(main_layout, key = '_L_MAIN_', visible=True),
        sg.Column(details_layout, key = '_L_DETAILS_', visible=False)
    ]
]

window = sg.Window('Filter People',
layout=all_layouts, font=('Arial', 16),
size=(500,400))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == '_DETAILS_':
        window['_L_MAIN_'].update(visible = False)
        window['_L_DETAILS_'].update(visible = True)
        person = values['_LIST_RESULTS_'][0]
        window['_FN_'].update(value = person.first_name)
        window['_LN_'].update(value=person.last_name)
        window['_EM_'].update(value=person.email)
        window['_LOC_'].update(value=f'{person.city}, {person.country} ({person.country_code})')
        window['_BD_'].update(value=person.birthday)
        window['_AVGS_'].update(value=person.average_salary)
    if event == '_BACK_':
        window['_L_MAIN_'].update(visible = True)
        window['_L_DETAILS_'].update(visible = False)
    if event == '_FILTER_COUNTRY_':
        country = values['_COMBO_COUNTRY_']
        order = "ASC" if values['_RB_ASC_'] == True else "DESC"
        people = DB.select_people_for_country(country, order)
        window['_LIST_RESULTS_'].update(values = people)


window.close()
