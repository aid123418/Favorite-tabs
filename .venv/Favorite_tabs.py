import streamlit as st
import time
import pandas
import hashlib

def upload_data(tabname_local, url_local, filename="Tabs.csv"):
    # Use SHA-256 hash of the URL as the filename
    hashed_filename = hashlib.sha256(url_local.encode()).hexdigest()
    with open(filename, 'a') as file:
        file.write(f"{tabname_local},{url_local},{hashed_filename}" + '\n')

st.title(f"Hello user!")

st.info("To change the theme color, go to the 3 dots and click settings.")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("Tabs.csv", header=None, sep=',', names=["tabname", "url", "hashed_filename"], on_bad_lines='skip')
with col1:
    for index, row in df[:6].iterrows():
        link = row["url"]
        title = row["tabname"]
        st.link_button(url=link, label=title)
    with st.form("New link"):
        tabname = st.text_input(label="New tab name:", help="Input the new tab's name!")
        url = st.text_input(label="URL to site:", help="Copy and paste the full link of the tab you want to save!")
        submit = st.form_submit_button(label="Submit")

if submit:
    upload_data(tabname, url)
    st.rerun()

with col3:
    clock = time.strftime("%b, %a %d")
    st.subheader(f"It is {clock} right now!")