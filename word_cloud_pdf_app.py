import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import pdfplumber
import pandas as pd
from collections import Counter

# Function to extract text from PDF
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Title
st.title("Word Cloud Generator")

# Upload file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Read the uploaded PDF file
    text = extract_text_from_pdf(BytesIO(uploaded_file.getvalue()))

    if text is not None:
        # Generate the word cloud
        wc = WordCloud(width=800, height=800, background_color='white', min_font_size=10)
        word_cloud = wc.generate(text)

        # Display the word cloud
        st.subheader("Word Cloud")
        fig, ax = plt.subplots()
        ax.imshow(word_cloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

        # Display the table with word details
        st.subheader("Word Details")
        words = text.split()
        word_count = Counter(words)
        df = pd.DataFrame.from_dict(word_count, orient='index', columns=['Count'])
        df.index.name = 'Word'
        df = df.reset_index()
        df = df.sort_values(by='Count', ascending=False)
        st.write(df)
    else:
        st.error("Unable to decode the uploaded file. Please try a different file.")


        hey ChatGPT, act as a Web Application Developer, write a complete code for me in python using important python
libraries to make a web application using streamlit, The app i would like to make is as follows:
1- Aim of the app: The main aim is to build an app where a user Will upload a document in the form of .docx, .pdf, .txt,
and/or any other document format. The user Will get a word cloud from that document.
2- The app should be able to handle different encodings.
Follow this workflow:

1- Title of the app is "Sadi Word Cloud di app"
2- Ask the user to upload a single or multiple files
3- Do not use stop words inside the word cloud, and provide a checkbox to activate this option
4- Enlist the top 50 words and ask the user to add additional stop words and then remove them from word cloud.
5- Make a word cloud from that file
6- Make a table with the frequency of each word sorting it into descending order and print the table
7- At the end give me options to add my social media accounts
Show me complete code for this app, please do not produce errors.