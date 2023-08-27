

from dotenv import load_dotenv
import streamlit as st
from pypdf2 import PdfReader


def main():
    load_dotenv()
    st.set_page_config(page_title='Ask your PDF')
    st.header('Ask your PDF!!!')

    # upload file
    pdf = st.file_uploader('Upload your PDF', type='pdf')

    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

if __name__=='__main__':
    main()