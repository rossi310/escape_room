import streamlit as st
import base64

# Function to display PDF in Streamlit

def display_pdf2(pdf_url):
    pdf_display = f'<iframe src="{pdf_url}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Define codes and corresponding PDF files for each escape room
escape_room_1 = {
    "3": "https://escaperoom-haphnydaaex9964auhtoxj.streamlit.app/pdfs/ESCAPE ROOM 1-Puzzle 2.pdf",
    "1136": "/pdfs/ESCAPE ROOM 1-Puzzle 3.pdf",
    "1869": "../pdfs/ESCAPE ROOM 1-Puzzle 4.pdf",
    "4135": "pdfs/ESCAPE ROOM 1-Puzzle 5.pdf"
}

escape_room_2 = {
    "8.314": "pdfs/ESCAPE ROOM 1-Puzzle 2.pdf",
    "1136": "pdfs/ESCAPE ROOM 1-Puzzle 3.pdf",
    "1869": "pdfs/ESCAPE ROOM 1-Puzzle 4.pdf",
    "4135": "pdfs/ESCAPE ROOM 1-Puzzle 5.pdf"
}

escape_room_3 = {
    "code5": "path/to/pdf5.pdf",
    "code6": "path/to/pdf6.pdf"
}

escape_room_4 = {
    "code7": "path/to/pdf7.pdf",
    "code8": "path/to/pdf8.pdf"
}

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Escape Room 1", "Escape Room 2", "Escape Room 3", "Escape Room 4"])

with tab1:
    code1 = st.text_input("Enter code for Escape Room 1")
    if code1 in escape_room_1:
        st.write("code correct")
        display_pdf(escape_room_1[code1])
    else:
        st.write("Enter a valid code to display the PDF.")

with tab2:
    code2 = st.text_input("Enter code for Escape Room 2")
    if code2 in escape_room_2:
        display_pdf(escape_room_2[code2])
    else:
        st.write("Enter a valid code to display the PDF.")

with tab3:
    code3 = st.text_input("Enter code for Escape Room 3")
    if code3 in escape_room_3:
        display_pdf(escape_room_3[code3])
    else:
        st.write("Enter a valid code to display the PDF.")

with tab4:
    code4 = st.text_input("Enter code for Escape Room 4")
    if code4 in escape_room_4:
        display_pdf(escape_room_4[code4])
    else:
        st.write("Enter a valid code to display the PDF.")
