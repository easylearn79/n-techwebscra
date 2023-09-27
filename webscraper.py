import streamlit as st
from bs4 import BeautifulSoup as bd
import requests
import pickle


st.title("N-Tech :red[Web Scraper]")
url = st.text_input("Enter URL")
scrap = st.button("Scrap")

hts = 'https://'
ht = 'http://'


# Sidebar

st.sidebar.title(":blue[Web Scrapping Made Easy]")
st.sidebar.text('The libraries used in creating this')
st.sidebar.text('webscraper')
st.sidebar.text('1.requests 2.BeautifulSoup')
mm = st.sidebar.multiselect("select scraping option Pre-defined Values",
                            ["Title", "Head", "Body", "Div", "A-href", "TB"]
                            )

if scrap:
    if url == '':
        st.text('Enter a URL')
    elif hts in url:
        page = requests.get(url)
        soup = bd(page.content, 'html.parser')
        pt = soup.prettify()
        st.write(pt)
    elif ht in url:
        page = requests.get(url)
        soup = bd(page.content, 'html.parser')
        pt = soup.prettify()
        if st.button('Not Secure Click to Access'):
            st.write(pt)

    else:
        page = requests.get(hts + url)
        soup = bd(page.content, 'html.parser')
        pt = soup.prettify()
        st.write(pt)


for options in mm:
    if options == "Title":
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        title = soup.title()
        st.write(title)
    if options == 'Head':
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        head = soup.head()
        st.write(head)
    if options == "Body":
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        body = soup.body()
        st.write(body)
    if options == "Div":
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        all_div = soup.find_all('div')
        st.write(all_div)
    if options == 'A-href':
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        a = soup.find_all('a')
        st.write(a)
    if options == "TB":
        page = requests.get(ht + url)
        soup = bd(page.content, 'html.parser')
        tb = soup.find(id='li')
        st.write(tb)

search_tag = st.sidebar.text_input("Scrap by Tag")

if st.sidebar.button('Scrap_By_TAG'):
    page = requests.get(ht + url)
    soup = bd(page.content, 'html.parser')
    si = soup.find_all(search_tag)
    st.write(si)


search_class = st.sidebar.text_input("Scrap by Class")
if st.sidebar.button('Scrap_By_Class'):
    page = requests.get(ht + url)
    soup = bd(page.content, 'html.parser')
    sc = soup.find_all(class_=search_class)
    st.write(sc)
search_id = st.sidebar.text_input("Scrap by ID")

if st.sidebar.button('Scrap_By_Id'):
    page = requests.get(ht + url)
    soup = bd(page.content, 'html.parser')
    si = soup.find_all(id=search_id)
    st.write(si)
