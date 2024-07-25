
import streamlit as st
import requests
import streamlit as st
import matplotlib.pyplot as plt
import requests





import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

st.sidebar.success('Visualisation')


x = st.date_input('Pick a valid date before 7th March 2021!')
date_object = datetime.strptime(str(x), '%Y-%m-%d')
if date_object > datetime.strptime('2021-03-07', '%Y-%m-%d'):
    st.write("No data available!")
else:

    r = requests.get('https://api.covidtracking.com/v2/us/daily/{}/simple.json'.format(x))

    outcomes = r.json()['data']['outcomes']
    hospitalized = outcomes['hospitalized']
    hospitalized_currentlyData = hospitalized['currently']
    hospitalized_in_ICU_currentlyData = hospitalized['in_icu']['currently']
    hospitalized_on_ventillator_currentlyData = hospitalized['on_ventilator']['currently']
    deathsTotal = outcomes['death']['total']

    # Input fields for user to update data
    hospitalized_currently = st.number_input('Enter the total number of currently hospitalized patients:', min_value=0,
                                             value=int(hospitalized_currentlyData), step=1)
    hospitalized_in_ICU_currently = st.number_input('Enter the number of patients currently in ICU:', min_value=0, value=int(hospitalized_in_ICU_currentlyData),
                                                    step=1)
    hospitalized_on_ventilator_currently = st.number_input('Enter the number of patients currently on ventilators:',
                                                           min_value=0, value=int(hospitalized_on_ventillator_currentlyData), step=1)

    # Compute other hospitalizations
    other_hospitalizations = hospitalized_currently - (hospitalized_in_ICU_currently + hospitalized_on_ventilator_currently)

    # Data for the pie chart
    labels = ['ICU', 'Ventilator', 'Other']
    sizes = [hospitalized_in_ICU_currently, hospitalized_on_ventilator_currently, other_hospitalizations]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0.1, 0)  # explode 1st and 2nd slice

    # Check for validity of data
    if other_hospitalizations < 0:
        st.error(
            'The sum of ICU and ventilator patients cannot exceed the total number of currently hospitalized patients.')
    else:
        # Plot
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the plot
        st.pyplot(fig1)
