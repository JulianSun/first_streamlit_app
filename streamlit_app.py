import streamlit
streamlit.title("Here is my title")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("http://fruityvice.com/api/fruit/"+ fruit_choice)


