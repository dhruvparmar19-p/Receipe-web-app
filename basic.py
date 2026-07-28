import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit import set_page_config
import json
import base64


set_page_config(page_title = "Tastopia", page_icon="logo.jpeg")

@st.cache_data
def get_img_as_base64(file):
    with open(file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("ol.jpeg")    
page_by_img = f"""
<style>
 [data-testid ="stAppViewContainer"]  {{
 background-image: url("data:image/png;base64,{img}");
 background-position: center;
 }}
[data-testid ="stHeader"] {{
background: rgba(0,0,0,0);
}}
<style>
"""
st.markdown(page_by_img, unsafe_allow_html = True)

def get_label_value(label):
     list.append(f"{label}")
    
    
    
st.header("Tastopia")


#Connection with Google.....
key = open("API_KEY.txt").read()
search_id = open("search_engine_ID.txt").read()

item1 = ['Bread','oats','Milk','egg','butter','nuts','garlic','onion','sugar','flour','rice','soy sauce','vegetable oil','honey','potato','peanut butter','onion powder','carrot','tomato','oregano','chilly flex']
selected_type1 = st.multiselect("Which ingredient do you want to choose",options = item1)
#st.write("You choose this ingredient", selected_type1)

st.divider()

item2 = ['Apple','orange','strawberry','Banana','Watermelon','Pineapple','pomegranate','Grape','Cocunut','Peach','Pair','Dates','Raisin','Papaya','Melon','Dragonfruit']
selected_type2 = st.multiselect("Which Fruit do you want to choose",options = item2)
#st.write("You choose this ingredient", selected_type2)

st.divider()

item3 = ['Olive oil','Vegetable oil','coconut oil','peanut oil','Frying oil','corn oil','virgin coconut oil','flaxseed oil','hazelnut oil']
selected_type3 = st.multiselect("Which Oil do you want to choose",options = item3)
#st.write("You choose this ingredient", selected_type3)

st.divider()

item4 = ['orange juice','club soda','coffee','espresso','pineapple juice','apple juice','coke','coconut water','pomegranate juice','lemonade']
selected_type4 = st.multiselect("Which Beverages do you want to choose",options = item4)
#st.write("You choose this ingredient", selected_type4)

st.divider()

items5 = ["vegan", "vegetarian", "gluten-free", "dairy-free","Non-vegetarian"]
dietary_restrictions = st.multiselect("Select your dietary restrictions",options = items5)

search_url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={search_id}&q=recipe+with+{'+'.join(selected_type1+selected_type2+selected_type3+selected_type4)}+{'+'.join(dietary_restrictions)}+site:allrecipes.com+-inurl:recipe+-inurl:review"

response = requests.get(search_url)
data = response.json()

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options = ["Home","Contact","About"],
        icons = ["house","person","envelope"],
        menu_icon = "cast",
        default_index = 0,
    )
  
if selected == "Home" :
        search = st.button("Search...")
        if search:
           
           recipe_list = data["items"][1:9]
           for recipe in recipe_list:

                #with st.container(height = 300): 
                    st.subheader(recipe["title"])
                    st.write(recipe["snippet"])
                    if "pagemap" in recipe and "cse_image" in recipe["pagemap"] and len(recipe["pagemap"]["cse_image"]) > 0:
                            st.image(recipe["pagemap"]["cse_image"][0]["src"], width=200)
                    else:
                            st.write("*********No image for this result**************")
           
if selected == "Contact":
    st.write("E-mail us at: Receipe123@gmail.com")
    
    
if selected == "About":
    st.write("Welcome to our Recipe Web App, your one-stop solution for discovering and creating delicious dishes from around the world! Our app is built using Python and provides a user-friendly interface for searching and filtering recipes based on ingredients, cooking time, and cuisine type. With a wide range of recipes from various sources, you can easily find inspiration for your next meal or discover new flavors and techniques to expand your culinary skills. Our Recipe Web App also allows you to create and save your own recipes, complete with photos, ingredients, and step-by-step instructions. You can share your creations with friends and family or keep them private for your own use. With our intuitive recipe builder, you can easily organize your recipes and create shopping lists for your next grocery trip. Whether you're a seasoned chef or a beginner cook, our Recipe Web App has something for everyone. We believe that cooking should be fun and accessible, and our app is designed to make it easy to find and create delicious meals that fit your lifestyle and preferences. Try it out today and join our community of food lovers and home cooks!")    







    