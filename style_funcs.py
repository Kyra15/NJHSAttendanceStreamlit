import streamlit as st


def hide_nav():
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)


def sidebar():
    st.sidebar.title("NJHS Attendance Program")

    st.sidebar.page_link("streamlit_app.py", label="Home")
    st.sidebar.page_link("pages/student_list.py", label="Student List")
    st.sidebar.page_link("pages/program.py", label="Program")
    st.sidebar.divider()
    st.sidebar.header("Link to Code:", anchor=False)
    st.sidebar.write("Made by Kyra Movva")
    st.sidebar.link_button("Github Repo", "https://github.com/Kyra15/NJHSAttendanceStreamlit")
    st.sidebar.write("")
    st.sidebar.subheader("Email me if anything breaks!", anchor=False)
    st.sidebar.link_button("kyra.movva@gmail.com", "mailto:kyra.movva@gmail.com")


def formatting_for_str(str_format):
    # print("before", str_format, type(str_format))
    str_format = str_format.split(", ")
    final_list = []
    for i in str_format:
        i = i.replace("[", "").replace("]", "").replace("'", "")
        final_list.append(i)
        # print(i)
    # print("formatted", final_list, type(final_list))
    final_str = "\n".join(final_list)
    return final_str
