import streamlit
import pandas
import snowflake.connector
import requests 
from urllib.error import URLError

streamlit.title('My First App')
streamlit.title('My Parent\'s New Healthy Dinner🍽️')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('Smoothie')
streamlit.text('Oatmeal')
streamlit.text('Egg')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# read csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#Create the repeatable code block(called Function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return  fruityvice_normalized

#New section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:   
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




streamlit.header("The fruit load list contains:")
#snowflake_related functions
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
         return my_cur.fetchall()
        
