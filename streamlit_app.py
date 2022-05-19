import streamlit
streamlit.title("Here is my title")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

streamlit.header('Breakfast Menu')
import requests
fruityvice_response = requests.get("http://fruityvice.com/api/furit/watermelon")
streamlit.text(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
