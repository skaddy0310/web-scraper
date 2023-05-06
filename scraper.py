import streamlit as sl 
import requests
from bs4 import BeautifulSoup as bs 

sl.set_page_config(page_title="web scraper", page_icon="data:image/png;base64,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")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
sl.markdown(hide_menu_style, unsafe_allow_html=True)

images = []
url = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
sl.markdown("<h1 style = 'text-align:center;'>web scraper</h1>", unsafe_allow_html=True)

with sl.form("main-form"):
    keyword = sl.text_input("# Enter the keyword")
    submit = sl.form_submit_button("submit")

if submit:
    col1,col2,col3 = sl.columns(3)
    page = requests.get(f"https://www.istockphoto.com/search/2/image?family=creative&phrase={keyword}", headers = headers)
    soup = bs(page.content,"lxml")
    rows = soup.find_all("div", class_= "ABVClgVJTdOPXmIa63fN")
    print("checking \n\n\n\n")
    for i in rows:
        images = i.find("img", class_="yGh0CfFS4AMLWjEE9W7v")
        url.append(images["src"])
    for m in url:
        sl.image(m,width=700)
      
