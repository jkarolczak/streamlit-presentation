from PIL import Image

import streamlit as st

from pages import *
   
    
def main():
    favicon = Image.open('images/logo-put.png')
    st.set_page_config(
        page_title="Streamlit",
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    pages = {
        'Introduction': introduction,
        'Why?': why,
        'Create an app': config,
        'Types - text': types_text,
        'Types - inputs': types_inputs,
        'Types - tables': types_tables,
        'Types - plots': types_plots,
        'Types - others': types_others,
        'Layout': layout,
        'Status': status,
        'Model inference': inference,
        'Magic': magic,
        'Streamlit cloud': cloud,
        'Summary': summary
    }
    name = st.sidebar.radio('Agenda', pages.keys(), index=0)
    pages[name]()
 
    
if __name__ == '__main__':
    main()
    