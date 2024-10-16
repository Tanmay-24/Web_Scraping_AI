import streamlit as st
from scrape import (scrape_website,extract_body_content,clean_body_content,split_dom_content)
from bs4 import BeautifulSoup

st.title("AI WEB SCRAPER")
url=st.text_input("Enter a website URL")


if st.button("Scrape Site"):
    st.write("Scraping data from the website...")
    result=scrape_website(url)
    print(result)


  