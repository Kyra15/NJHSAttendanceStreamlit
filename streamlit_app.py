import streamlit as st
from style_funcs import hide_nav, sidebar

st.set_page_config(page_title='NJHS - Home', layout="wide", page_icon='')

hide_nav()
sidebar()

st.title("Home", anchor=False)
st.divider()
st.header("Instructions", anchor=False)
st.subheader("To set up program (only do for first use):", anchor=False)
st.write("At the beginning of the year, you'll most likely get a list with every members' name. "
         "Alphabetize that list and format it like the photo below.")

st.image("images/student_input_ex.png", use_column_width="always")

st.write("On this website, go to the \"Student List\" section."
         "Paste the list into the input textbox and save it.")

st.write("Now, on your google sheet (or make a copy if you want to be safe), "
         "add this email address as an editor: \"njhs-sheet-editor@njhsattendence.iam.gserviceaccount.com\", "
         " and set the viewing permission to \"Anyone with the link.\"")

st.write("Back on this website, go to the program page and paste the link for this google sheet, then hit save.")

st.subheader("If program is already set up:", anchor=False)
st.write("Once you create your google form for the attendance and link that to a spreadsheet, "
         "export the sheet by going to File -> Download -> Comma Seperated Values (.csv).")
st.image("images/exporting_csv.gif", use_column_width="always")
st.write("The csv file should have been saved to your device. "
         "Now, input the file into this website by going to the \"Program\" section and "
         "inputting the file into this website.")
st.image("images/uploading_file.gif", use_column_width="always")
st.write("Click the \"Check Attendance\" button and wait until it finishes processing.")
st.write("")
st.write("If there are issues with the form, which will most likely come from typos or names not matching up, "
         "the names with errors will be outputted in the \"Errors\" box. "
         "Go back to the google sheet that your google form is connected to and fix the names with errors. "
         "After you've fixed the errors, redownload the file and try the program again. "
         "Keep repeating this until the \"Errors\" box is empty.")
st.image("images/fixing_errors.gif", use_column_width="always")
st.write("The names of people who came to the meeting but aren't members of "
         "NJHS will also be outputted if you need them too.")

st.image("images/extras.png", use_column_width="always")

st.write("Now click the process button, and if everything worked correctly, your google sheet should be updated with "
         "either a 1 or a 0 by each name, "
         "depending on whether they were at the meeting or not.")
st.image("images/processing.gif", use_column_width="always")

st.subheader("That's it!", anchor=False)

