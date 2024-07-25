



import streamlit as sd
import time


def display_message(message, delay=0.1):
    placeholder = sd.empty()
    full_message = ""
    for char in message:
        full_message += char
        placeholder.text(full_message)
        time.sleep(delay)

if sd.button('Display Data'):
    sd.write("Fetching data, please wait...")
    time.sleep(0.4)  # Simulate a delay for fetching data
    display_message("Here is the data for my education, including detailed information on various", delay=0.1)
    display_message("subjects, grades, and overall academic performance.",delay=0.1)

    sd.image('streamlitPractice/Screenshot 2024-07-25 at 17.28.20.png')
    sd.sidebar.success('Education')
    with sd.expander('See Education'):
        sd.write('Finished High School in 2023')

        progress_text = "Images loading. Please wait..."
        my_bar = sd.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
        my_bar.empty()
        sd.image('streamlitPractice/Screenshot 2024-07-24 at 19.46.27.png')

