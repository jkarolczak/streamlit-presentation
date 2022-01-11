import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def types_inputs():
    st.title("Streamlit element types - inputs")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.form("person_form"):    
            name_val = st.text_input("Name")
            sex_val = st.radio("Sex", ["Female", "Male", "Other"])
            tel_val = st.number_input("Telephone", 100000000, 999999999)
            date_val = st.date_input("Preferred contact date")
            if st.form_submit_button():
                if sex_val == "Female": title = "Ms. "    
                elif sex_val == "Male": title = "Mr. "
                else: title = ""    
                st.success(f"""
                Dear {title}{name_val}, \n
                We're glad that you have submitted the form. Our employee will call you on {date_val}, on phone number {tel_val}.\n
                Best regards,\n
                The Boring Company
                """)
    
    with col2:
        st.code(r'''
with st.form("person_form"):    
    name_val = st.text_input("Name")
    sex_val = st.radio("Sex", ["Female", "Male", "Other"])
    tel_val = st.number_input("Telephone", 100000000, 999999999)
    date_val = st.date_input("Preferred contact date")
    if st.form_submit_button():
        if sex_val == "Female": title = "Ms. "    
        elif sex_val == "Male": title = "Mr. "
        else: title = ""    
        st.success(f"""
        Dear {title}{name_val},
        We're glad that you have submitted the form. Our employee will call you on {date_val}, on phone number {tel_val}.
        Best regards,
        The Boring Company
        """)
        ''')
        
    with st.expander("Docs"):
        col1, col2 = st.columns(2)
        col1.markdown("""
        - [Form Streamlit API reference](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
        - [Form submit button Streamlit API reference](https://docs.streamlit.io/library/api-reference/control-flow/st.form_submit_button)
        """)  
        
        col2.markdown("""
        - [Checkbox Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
        - [Radio Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.radio)
        - [Selectbox Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
        - [Multiselect Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
        - [Slider Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.slider)
        - [Selectslider Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
        - [Text input Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)
        - [Number input Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.number_input)
        - [Date input Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.date_input)
        - [Time input Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.time_input)
        - [File input Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
        - [Color picker Streamlit API reference](https://docs.streamlit.io/library/api-reference/widgets/st.color_picker)
        
        """) 
    
    
def types_others():
    st.title("Streamlit element types - others")
    st.markdown("---")
    st.markdown("Streamlit supports many others tools for visualization and data manipulation. Below you can see only some of them.")
    st.caption("Map")
    df = pd.DataFrame([[52.394067, 16.918323], [52.403791, 16.949524]], columns=['lat', 'lon'])
    st.map(df, zoom=11)
    col1, col2, col3 = st.columns(3)
    col1.caption("3dmol")
    col1.image('https://github.com/napoles-uach/streamlit_3dmol/blob/master/BRQqqfZ2lU.gif?raw=true')       
    col2.caption("Graphviz")
    col2.graphviz_chart('''
        digraph {
            "Create SOTA model" -> "Share it using Streamlit"
        }                   
    ''')
    col3.caption("Image cropper")
    col3.image('https://github.com/turner-anderson/streamlit-cropper/blob/master/img/demo.gif?raw=true')
    col1, col2, col3 = st.columns(3)
    col1.caption("Drawable canvas")
    col1.image('https://github.com/andfanilo/streamlit-drawable-canvas/blob/develop/img/demo.gif?raw=true')
    col2.caption("Ace code editor")
    col2.image('https://raw.githubusercontent.com/okld/streamlit-ace/main/preview.png')
    col3.caption("Annotated text")
    col3.image('https://raw.githubusercontent.com/tvst/st-annotated-text/master/example.png')
    
    
def types_plots():
    st.title("Streamlit element types - plots")
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.markdown(r"""
    Streamlit supports plotting libraries like:
    - [Plotly](https://plotly.com/python/)
    - [Pyplot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html)
    - [Altair](https://altair-viz.github.io/)
    - [Vega](https://vega.github.io/vega/)
    - [Bokeh](https://bokeh.org/)
    - [Pydeck](https://pydeck.gl/)
    """)
    col2.markdown("""
    There are standalone plotting functions defined in Streamlit:
    - `st.line_chart`
    - `st.area_chart`
    - `st.bar_chart`
    """)
    col1, col2 = st.columns(2)
    
    df = pd.DataFrame({'x': np.linspace(0, 20, 1000)})
    df['sine'] = np.sin(df['x'])
    fig = px.line(df, x='x', y='sine', template='simple_white', height=400)
    fig.update_layout(margin=dict(l=5, r=5, t=5, b=5))
    col1.plotly_chart(fig, use_container_width=True)
    col1.code("""
    fig = px.line(df, x='x', y='sine', title="Sine function")
    st.plotly_chart(fig, use_container_width=True)
    """)  

    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    col2.area_chart(df, height=400)
    col2.code("""
    st.area_chart(df, height=400)      
    """)
    
    with st.expander("Docs"):
        col1, col2 = st.columns(2)
        col1.markdown("""
        - [Plotly Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart)
        - [Pyplot Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.pyplot)
        - [Altair Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
        - [Vega Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.vega_lite_chart)
        - [Bokeh Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.bokeh_chart)
        - [Pydeck Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
        """)   
        col2.markdown("""
        - [`st.line_chart` Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)
        - [`st.area_chart` Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.area_chart)
        - [`st.bar_chart` Streamlit API reference](https://docs.streamlit.io/library/api-reference/charts/st.bar_chart)
        """)  


def types_tables():
    st.title("Streamlit element types - tables")
    st.markdown("---")
    df = pd.DataFrame(
        np.random.randint(1, 24, (50, 20)),
        columns=[f"{i+1}_{t}" for i, t in enumerate(['meaningless', 'dummy','nonsensical', 'silly', 'ridiculous'] * 4)]
    )
    df = df.style.highlight_max(color='cyan')
    st.dataframe(df, height=450)
    st.code("""
    st.dataframe(df, height=450)  
    """, language="python")
    
    with st.expander("Docs"):
        st.markdown("[Streamlit API reference](https://docs.streamlit.io/library/api-reference/data/st.dataframe)")
        st.help(st.dataframe)


def types_text():
    st.title("Streamlit element types - text")
    st.markdown("---")
    st.title("Streamlit supports many text elements")
    st.code("st.title(\"Streamlit supports many text elements\")", language="python")
    st.header("On this slide you can see differences between them")
    st.code("st.title(\"On this slide you can see differences between them\")", language="python")
    st.subheader("And get know how to use them in your own app")
    st.code("st.subheader(\"And get know how to use them in your own app\")", language="python")
    st.markdown("If you find the *above* style inconvenient you can use **markdown** and $\LaTeX$ if you want to pretend scientist")
    st.code("st.markdown(\"If you find the *above* style inconvenient you can use **markdown** and $\LaTeX$ if you want to pretend scientist\")")
    st.latex(r"\arctan{1} + \sum_{i=1}^{\infty} i = \frac{\pi}{4} - \frac{1}{12}")
    st.code("st.latex(r\"\\arctan{1} + \\sum_{i=1}^{\\infty} i = \\frac{\\pi}{4} - \\frac{1}{12}\")")
    st.caption("This is a caption and it claims that above you can observe many text elements and code used in the source file to display them")
    st.code("st.caption(\"This is a caption and it claims that above you can observe many text elements and code used in the source file to display them\")", language="python")
    
    with st.expander("Docs"):
        st.markdown("""
        - [Markdown Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.markdown)
        - [Title Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.title)
        - [Header Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.header)
        - [Subheader Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.subheader)
        - [Caption Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.caption)
        - [Code Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.cod)
        - [Text Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.text)
        - [Latex Streamlit API reference](https://docs.streamlit.io/library/api-reference/text/st.latex)
        """)   
