from PIL import Image

import streamlit as st

from pages import *
   
    
def main():
    favicon = Image.open('images/logo-put.png')
    st.set_page_config(
        page_title="Streamlit",
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    pages = {
            'Introduction': introduction,
            'Why?': why,
            'Create an app': config,
            'Elements - text': types_text,
            'Elements - inputs': types_inputs,
            'Elements - tables': types_tables,
            'Elements - plots': types_plots,
            'Elements - others': types_others,
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
    