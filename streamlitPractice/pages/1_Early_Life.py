import streamlit as sd

sd.sidebar.success('Early Life')

sd.snow()
label = 'Hello, I am Siddhant, and I just turned 19!'
sd.snow()
sd.write(f"# {label}")
with sd.expander('Short Video'):
    sd.video('streamlitPractice/invideo-ai-1080 Meet Sid_ The Multifaceted Cartoon Chara 2024-07-25.mp4')
    sd.snow()
sd.snow()
with sd.expander('My personal photos'):

    sd.image('streamlitPractice/Screenshot 2024-07-23 at 22.54.09.png')
    sd.image('streamlitPractice/IMG_4891.jpeg')
    sd.image('streamlitPractice/IMG_4751.jpeg')
    sd.image('streamlitPractice/IMG_4868.jpeg')
    sd.snow()
sd.snow()

with sd.expander('My Github'):

    sd.text('https://github.com/SiddyWiddy')


