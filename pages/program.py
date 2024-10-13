import streamlit as st
from style_funcs import hide_nav, sidebar
from pages.student_list import LocalStorageManager
import pandas as pd
from pyscript import main


st.set_page_config(page_title='NJHS Attendance Program - Student List', layout="wide", page_icon='')

hide_nav()
sidebar()

localS = LocalStorageManager()


def process_file():
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe.to_csv("attendance_sheet.csv", index=False)
        return True
    else:
        return False


st.title("Program", anchor=False)
st.divider()

with open("attendance_sheet.csv", "w") as f:
    f.write("")

st.header("Attendance Upload:", anchor=False)
uploaded_file = st.file_uploader(label="", label_visibility="collapsed")


if not process_file():
    st.warning("Please upload a file!")
else:
    st.success("Uploaded!")
    main()

    st.header("Attendance Marked", anchor=False)
    st.dataframe(pd.read_csv("returntable.csv"), width=500)

    st.subheader("Errors:", anchor=False)
    st.write("If you need to change this, either change it through the google sheet directly or on the csv file")
    st.dataframe(pd.read_csv("errors.txt"), width=500)

    st.subheader("Extras:", anchor=False)
    st.write("People that showed up to the meeting but aren't members")
    st.dataframe(pd.read_csv("extras.txt"), width=500)


st.divider()

st.header("Google Sheets:", anchor=False)
st.write("Input your attendance sheet here:")
st.write("Make sure to add the email \"njhs-sheet-editor@njhsattendence.iam.gserviceaccount.com\" "
         "as an editor to your sheet")
st.write("Also make sure to set the viewing permissions to \"Anyone with the Link\"")
sheets_name = st.text_input("Name:")
sheets_link = st.text_input("Link:")
localS.setItem("sheets_link", sheets_link)
localS.setItem("sheets_name", sheets_name)
