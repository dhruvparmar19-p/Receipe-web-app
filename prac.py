import streamlit as st
import requests

# Set up the Google Custom Search API client
with open("API_KEY.txt", "r") as f:
    api_key = f.read().strip()
with open("search_engine_ID.txt", "r") as f:
    cx = f.read().strip()

# Set up the Streamlit app
st.title("Recipe Finder")
query = st.multiselect("Select the ingredients:", ["chicken", "rice", "broccoli", "soy sauce"])

# Perform the web search using the Google Custom Search API
search_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q=recipe+with+{'+'.join(query)}"
response = requests.get(search_url)
data = response.json()

# Display the search results
if  data["items"]:
    result = data["items"][0]
    st.subheader(result["title"])
    st.write(result["snippet"])
    st.image(result["pagemap"]["cse_image"][0]["src"])
else:
    st.write("No recipe found.")