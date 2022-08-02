import streamlit as st


def cloud():
    st.title("Streamlit cloud")
    st.markdown("---")

    st.markdown("""
    - Allows deploying apps created with Streamlit.
    - Is free to use.
    - Requires only signing-in using github and choosing values from 3 dropdowns.
    - Doesn't require DevOps related knowledge and displays almost only funny logs.
    """)

    col1, col2 = st.columns(2)
    col1.subheader("Deployment")
    col1.image('images/deploy.png')
    col2.subheader("Logs")
    col2.text("""
    [client] Spinning up manager process...
    [client] Inflating balloons...
    [client] Unpacking Comic Sans RAR files...
    [client] Loading "Under construction" GIF...
    [client] Compiling <blink> tags...
    """)


def config():
    st.title("Our very first app")
    st.markdown("---")
    st.code("""
    import streamlit as st

    def earth():
        st.markdown("Hello **Earth**!")

    def mars():
        st.markdown("Hello **Mars**!")

    def venus():
        st.markdown("Hello **Venus**!")    

    def main():
        st.set_page_config(
            page_title="Planets",
            page_icon="🌍",
            layout="wide",
        )
        pages = {
            'Earth': earth,
            'Mars': mars,
            'Venus': venus
        }
        name = st.sidebar.radio('Menu', pages.keys(), index=0)
        pages[name]()

    if __name__ == '__main__':
        main()                        
            """, language="python")
    st.markdown("[Live demo](https://share.streamlit.io/jkarolczak/streamlit-planets/main/planets.py)")


def introduction():
    st.title("What Streamlit is?")
    st.markdown("---")
    st.subheader("The fastest way to build and share data apps.")
    st.markdown("""
    - Streamlit turns data scripts into shareable web apps in minutes. 
    - All in Python. 
    - All for free. 
    - No front‑end experience required.
    """)
    st.caption("Source: https://streamlit.io/")
    st.markdown("""
    - It does magic.
    """)


def magic():
    st.title("Magic")
    st.markdown("---")
    st.markdown("""
    If you are lazy you don't have to remember output types like `st.dataframe` or `st.plotly`. 
    You can use `st.write` and Streamlit will do the magic in the background. But of course, it
    is not the whole magic I'm talking about. If you really have no time and the deadline is
    approaching you can forget about writing functions calls. 
    
    The code below shouldn't work, should it?
    
    Check it out on [live demo](https://share.streamlit.io/jkarolczak/streamlit-magic/main/magic.py)
    """)
    st.code("""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
# This is a magic document title
---
It uses some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df 

x = 10
'x', x  

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig              
""")


def summary():
    st.title("Summary")
    st.markdown("---")
    st.markdown(
        "You can find this presentation with the source code on [**github.com/jkarolczak/streamlit-presentation**](github.com/jkarolczak/streamlit-presentation)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Pros")
        st.markdown("""
        - it's in Python
        - requires no knowledge about web development    
        - allows creating apps in a few minutes and lines of code
        - it's so intuitive that this presentation was created using this technology
        - easily integrates with many visualization tools
        - does many things in the background and you don't have to remember about them
        - there is a dedicated tool for deployments
        - despite features enumerated in this presentation, it has many others like caching, styling or statefulness
        """)
        for i in range(10): st.text("")
        st.markdown("*Presentation created by Jacek Karolczak*")

    with col2:
        st.header("Cons")
        st.markdown("""
        - doesn't allow you to fully control the app
        - a few times in this presentations I used snippets like:
        """)
        st.code("for i in range(7): st.text(\"\")")
        st.markdown("""
        - it's possible to glitch the app (try to use `st.slider` with a range from 0 to 1e10)
        """)
    with col3:
        st.image('images/qr.png')
        st.image('images/meme2.jpg')


def why():
    st.title("Motivation")
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.markdown("""
    One day you may want to:
    - share a Machine Learning model with the World,
    - participate in a hackathon and have a little time to create complete solution,
    - create working mockup for web developers as a template for production solution
    
    and despite this excellent course you are not an internet applications expert and you:
    - cannot expand acronyms like `HTML`, `CSS` or `JS`,\*
    - have no aesthetic sense,\*
    - don't know what protocols like `HTTP` and `SSL` actually do,\*
    - suffer lack of time,\*
    - know almost nothing about requests and their types.\*
    
    *\*select all that apply*
    """)
    col2.image('images/meme.jpg')
