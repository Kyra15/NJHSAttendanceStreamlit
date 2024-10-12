import streamlit as st
from style_funcs import hide_nav, hide_anchor_links

st.set_page_config(page_title='NJHS Attendance Program', layout="wide", page_icon='')

hide_nav()

st.sidebar.title("NJHS Attendance Program")

st.sidebar.page_link("streamlit_app.py", label="Home")
st.sidebar.page_link("pages/program.py", label="Student List")
st.sidebar.page_link("pages/program.py", label="Program")
st.sidebar.divider()
st.sidebar.header("Link to Code:", anchor=False)
st.sidebar.write("Made by Kyra Movva")
st.sidebar.link_button("Github Repo", "https://github.com/Kyra15/NJHSAttendanceStreamlit")
st.sidebar.write("")
st.sidebar.subheader("Email me if anything breaks!", anchor=False)
st.sidebar.link_button("kyra.movva@gmail.com", "mailto:kyra.movva@gmail.com")

st.title("Home", anchor=False)
st.divider()
st.header("Instructions", anchor=False)
st.subheader("To set up program (only do for first use):", anchor=False)
st.write("At the beginning of the year, you'll most likely get a list with every members' name. "
         "Alphabetize that list, (look up a website for it if you need to) and copy it. "
         "It should be in a format like the photo below.")

st.columns(3)[1].image("/Users/kyramovva/NJHSAttendance/images/instruct1.jpeg", width=250)
st.write("On this website, go to the \"Program\" section and look for the box that says \"Student List.\""
         "Paste the list into that textbox.")


st.subheader("If program is already set up:")
st.write("Once you create your google form for the attendance and link that to a spreadsheet, "
         "export the sheet by going to File -> Download -> Comma Seperated Values (.csv).")
st.columns(3)[1].image("/Users/kyramovva/NJHSAttendance/images/instruct1.jpeg", width=250)
st.write("The csv file should have been saved to your device. "
         "Now, input the file into this website by going to the \"Program\" section and "
         "dragging and dropping (computer only) the file into this website where it says \"Input File.\"")
st.columns(3)[1].image("/Users/kyramovva/NJHSAttendance/images/instruct1.jpeg", width=250)
st.write("Click the \"Check Attendance\" button and wait until it finishes processing.")
st.write("")
st.write("If there are issues with the form, which will most likely come from typos or names not matching up, "
         "the names with errors will be outputted in the \"Errors\" box. "
         "Go back to the google sheet that your google form is connected to and fix the names with errors. "
         "After you've fixed the errors, redownload the file and try the program again. "
         "Keep repeating this until the \"Errors\" box is empty.")
st.columns(3)[1].image("/Users/kyramovva/NJHSAttendance/images/instruct1.jpeg", width=250)
st.write("The names of people who came to the meeting but aren't members of "
         "NJHS will also be outputted if you need them too :)")

st.write("Once everything is good, click the \"Download Updated Attendance\" button. "
         "The new file should be saved to your computer. Go to the Google Sheet link called \"NJHS Middleman.\" "
         "Go to File -> Import and drag and drop the updated attendance file into there. Hit replace current sheet. "
         "Now, copy the entire second column. Go to your main attendance spreadsheet (the one on schoology!) "
         "and paste in the column.")
st.columns(3)[1].image("/Users/kyramovva/NJHSAttendance/images/instruct1.jpeg", width=250)
st.subheader("That's it!", anchor=False)

