import mainFile as mf
import streamlit as st

animals = ['Dog']
with open('names.txt') as file:
    data = file.read()
    data_list = data.splitlines()
    data_list = set(data_list)
    for i in data_list:
        animals.append(i)


st.title('Pet(:dog:) Name Generator')



type = st.sidebar.selectbox('What is your pet?',options=(animals),index=0)

color = st.sidebar.text_area(label = "What color is your "+ type +"?",max_chars=10)
if(st.sidebar.button(label = 'Generate',type = 'primary')):
        names = mf.generateName(type=type, color=color)
        st.text(names['name'])

