import streamlit as st
import time


def upload_data(tabname_local, link_local, filename=".//.venv/Tabs.txt"):
    with open(filename, 'a') as file_local:
        if "https://" not in link_local:
            link_local = "https://" + link_local
        file_local.write(f"{tabname_local},{link_local}\n")


def read_data(filename=".//.venv/Tabs.txt"):
    try:
        with open(filename, 'r') as file_local:
            tabs = [line.strip().split(",") for line in file_local.readlines()]
    except FileNotFoundError:
        tabs = []
    return tabs


st.title(f"Hello user!")

st.info("To change the theme color, go to the 3 dots and click settings.    "
        " To delete a link, click the checkbox next to it, then click the checkbox again. This site is made by Aiden W!")

col1, col2 = st.columns(2)

tabs = read_data()

# Maintain a list of checkboxes and their corresponding link boxes
checkboxes = []

with col1:
    for i, tab in enumerate(tabs):
        if len(tab) >= 2:
            # Create a checkbox for each link box
            checkbox = st.checkbox(f"Remove {tab[0]}")
            checkboxes.append((checkbox, i))
            st.link_button(label=tab[0], url=tab[1], help=tab[1])

# Remove the selected link box when its checkbox is checked
for checkbox, i in checkboxes:
    try:
        if checkbox:
            del tabs[i]
            break
    except IndentationError:
        st.write("somehow, the script isn't working.")

# Rewrite data file after deletion
try:
    with open(".//.venv/Tabs.txt", 'w') as file_local:
        for tab in tabs:
            file_local.write(f"{tab[0]}, {tab[1]}\n")
except IndexError:
    st.rerun()

with st.form("New link"):
    tabname = st.text_input(label="New tab name:", help="Input the new tab's name!")
    url = st.text_input(label="URL to site:", help="Copy and paste the full link of the tab you want to save!")
    submit = st.form_submit_button(label="Submit")

if submit:
    upload_data(tabname, url)
    st.rerun()
