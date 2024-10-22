import streamlit as st
from style_funcs import hide_nav, sidebar, formatting_for_str
from streamlit_local_storage import LocalStorage


st.set_page_config(page_title='NJHS Attendance Program - Student List', layout="wide", page_icon='')

localS = LocalStorage()
student_list = []

if "student_names" not in st.session_state:
    st.session_state["student_names"] = []

hide_nav()
sidebar()

st.title("Student List", anchor=False)
st.divider()

st.header("Input:", anchor=False)
with st.form("student_form"):
    st.write("Copy and paste names into here and click save when done")
    st.image("images/student_input_ex.png", use_column_width="always", caption="Example input")
    #student_text = st.text_area("InputBox", value=formatting_for_str(str(localS.getItem("student_names"))),
                                # label_visibility="collapsed", height=300)
    exists = st.form_submit_button("Save")
    # if exists is not None:
        # student_list = student_text.split("\n")
        # localS.setItem("student_names", student_list)

        # student_list = localS.getItem("student_names")
        # with open("masterlist.csv", "w", newline="") as f:
            # for i in student_list:
                # if i != "":
                    # f.write(i + "\n")
