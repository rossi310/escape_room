import streamlit as st
import base64

# Function to display PDF in Streamlit

def display_image(image_url):
    st.image(image_url)

def display_pdf(pdf_url):
    pdf_display = f'<iframe src="{pdf_url}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def display_pdf2(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Define codes and corresponding PDF files for each escape room
escape_room_1 = {
    "3": "pdfs/ESCAPE ROOM 1-Puzzle 2.jpg",
    "1136": "pdfs/ESCAPE ROOM 1-Puzzle 3.jpg",
    "1869": "pdfs/ESCAPE ROOM 1-Puzzle 4.jpg",
    "4135": "pdfs/ESCAPE ROOM 1-Puzzle 5.jpg"
}

escape_room_2 = {
    "8.314":  "pdfs/ESCAPE ROOM 2-puzzle 2.jpg",
    "1136":   "pdfs/ESCAPE ROOM 2-puzzle 3.jpg",
    "6.0221": "pdfs/ESCAPE ROOM 2-puzzle 4.jpg",
    "4135":   "pdfs/ESCAPE ROOM 2-puzzle 5.jpg"
}

escape_room_3 = {
    "298":    "pdfs/ESCAPE ROOM 3-puzzle 2.jpg",
    "1534":   "pdfs/ESCAPE ROOM 3-puzzle 3.jpg",
    "8.314": "pdfs/ESCAPE ROOM 3-puzzle 4.jpg",
    "1275":   "pdfs/ESCAPE ROOM 3-puzzle 5.jpg"
}

escape_room_4 = {
     "5":   "pdfs/ESCAPE ROOM 4-puzzle 2.jpg",
    "4952": "pdfs/ESCAPE ROOM 4-puzzle 3.jpg",
    "3157": "pdfs/ESCAPE ROOM 4-puzzle 4.jpg",
    "1275": "pdfs/ESCAPE ROOM 4-puzzle 5.jpg"
}

escape_room_5 = {
     "3157":        "pdfs/ESCAPE ROOM 5-puzzle 2.jpg",
    "phosphorus":   "pdfs/ESCAPE ROOM 5-puzzle 3.jpg",
    "6.0221":       "pdfs/ESCAPE ROOM 5-puzzle 4.jpg",
    "1225":         "pdfs/ESCAPE ROOM 5-puzzle 5.jpg"
}

escape_room_6 = {
     "3":     "pdfs/ESCAPE ROOM 6-puzzle 2.jpg",
    "1534":   "pdfs/ESCAPE ROOM 6-puzzle 3.jpg",
    "6.0221": "pdfs/ESCAPE ROOM 6-puzzle 4.jpg",
    "1077":   "pdfs/ESCAPE ROOM 6-puzzle 5.jpg"
}

# Create tabs
tab1, tab2, tab3, tab4 , tab5, tab6 = st.tabs(["Escape Room 1", "Escape Room 2", "Escape Room 3", "Escape Room 4","Escape Room 5","Escape Room 6"])

with tab1:
    code1 = st.text_input("Enter code for Escape Room 1")
    if code1 in escape_room_1:
        st.write("code correct")
        display_image(escape_room_1[code1])
        #display_pdf(escape_room_1[code1])
    else:
        st.write("Enter a valid code to display the PDF.")

with tab2:
    code2 = st.text_input("Enter code for Escape Room 2")
    if code2 in escape_room_2:
        st.write("code correct")
        display_image(escape_room_2[code2])
        #display_pdf(escape_room_2[code2])
    else:
        st.write("Enter a valid code to display the PDF.")

with tab3:
    code3 = st.text_input("Enter code for Escape Room 3")
    if code3 in escape_room_3:
        display_image(escape_room_3[code3])
       
    else:
        st.write("Enter a valid code to display the PDF.")

with tab4:
    code4 = st.text_input("Enter code for Escape Room 4")
    if code4 in escape_room_4:
        display_image(escape_room_4[code4])
       
    else:
        st.write("Enter a valid code to display the PDF.")
with tab5:
    code5 = st.text_input("Enter code for Escape Room 5")
    if code5 in escape_room_5:
        display_image(escape_room_5[code5])
      
    else:
        st.write("Enter a valid code to display the PDF.")
with tab6:
    code6 = st.text_input("Enter code for Escape Room 6")
    if code6 in escape_room_6:
        display_image(escape_room_6[code6])
      
    else:
        st.write("Enter a valid code to display the PDF.")
