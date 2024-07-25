import requests
import streamlit as sd
from datetime import datetime
import time

sd.sidebar.success('Covid 19 Data')

c = sd.date_input('Enter a date: ')

def display_message(message, delay=0.01):
    placeholder = sd.empty()
    full_message = ""
    for char in message:
        full_message += char
        placeholder.text(full_message)
        time.sleep(delay)


with sd.expander("See Date selected"):
    sd.write(c)

with sd.expander("See Data/Information"):

    date_object = datetime.strptime(str(c), '%Y-%m-%d')
    if date_object > datetime.strptime('2021-03-07', '%Y-%m-%d'):
        display_message("No data available!")
    else:
        r = requests.get('https://api.covidtracking.com/v2/us/daily/{}/simple.json'.format(c))
        sd.write(r.json())

        outcomes = r.json()['data']['outcomes']
        hospitalized = outcomes['hospitalized']
        hospitalized_currently = hospitalized['currently']
        hospitalized_in_ICU_currently = hospitalized['in_icu']['currently']
        hospitalized_on_ventillator_currently = hospitalized['on_ventilator']['currently']
        deathsTotal = outcomes['death']['total']

        states = r.json()['data']['states']

        cases = r.json()['data']['cases']['total']

        tests = r.json()['data']['testing']['total']




        selection = sd.multiselect('Choose what data you want specifically',[
            'states','cases','tests','outcomes','hospitalised','hospitalised currently',
            'hospitalised in icu currently','hospitalised on ventilator currently',
            'Total Deaths'
        ])

        display_message(selection)
        if 'states' in selection:
            display_message('states: ' + str(states))
        if 'cases' in selection:
            display_message('cases: ' + str(cases))
        if 'tests' in selection:
            display_message('tests: '+ str(tests))
        if 'outcomes' in selection:
            display_message("outcomes: " + str(outcomes))
        if 'hospitalised' in selection:
            display_message("hospitalised: " +str(hospitalized))
        if 'hospitalised currently' in selection:
            display_message('hospitalised currently: ' + str(hospitalized_currently))
        if 'hospitalised in icu currently' in selection:
            display_message('hospitalised in icu currently: '+ str(hospitalized_in_ICU_currently))
        if 'hospitalised on ventilator currently' in selection:
            display_message('hospitalised on ventilator currently: '+str(hospitalized_on_ventillator_currently))
        if 'Total Deaths' in selection:
            display_message('Total Deaths: ' + str(deathsTotal))



#March 7th 2021 -> 2021-03-07