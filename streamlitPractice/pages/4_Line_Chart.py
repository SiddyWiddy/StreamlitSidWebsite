import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.sidebar.success('Visualisation')

import time
with st.spinner('Wait for it processing please. Wait for 2 seconds around: '):
    time.sleep(2)

# Function to fetch data
def fetch_data(date):
    url = f'https://api.covidtracking.com/v2/us/daily/{date}/simple.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Generate date range
x = st.date_input('Enter start date : ')
y = st.date_input('Enter end date: ')

start_date = datetime(x.year, x.month, x.day)
end_date = datetime(y.year, y.month, y.day)

# Directly use the start_date and end_date as they are already datetime objects
start_datemin = datetime(2020, 4, 1)
end_datemax = datetime(2021, 3, 7)

if (start_date >= end_date or start_date < start_datemin or end_date > end_datemax):
    st.write('No data available. Data only available between 1st April 2020 to 7th March 2021.')
else:
    date_range = pd.date_range(start_date, end_date)

    st.write('Hospitalisations loading. please be patient: ')

    # Fetch and process data
    data = []
    for single_date in date_range:
        formatted_date = single_date.strftime('%Y-%m-%d')
        result = fetch_data(formatted_date)
        if result and 'data' in result and 'outcomes' in result['data'] and 'hospitalized' in result['data']['outcomes']:
            current_hospitalized = result['data']['outcomes']['hospitalized'].get('currently', 0)
            data.append({'date': formatted_date, 'hospitalized_currently': current_hospitalized})
        else:
            data.append({'date': formatted_date, 'hospitalized_currently': None})

    # Create DataFrame
    df = pd.DataFrame(data)
    df.set_index('date', inplace=True)

    # Plotting the data
    with st.spinner('Wait for it processing please: '):
        time.sleep(5)
    st.line_chart(df)

    st.write('Done')
