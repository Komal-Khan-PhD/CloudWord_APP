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


