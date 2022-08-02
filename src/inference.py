import json
import pandas as pd
import pickle
import streamlit as st
import sys
from time import sleep

sys.path.append("../")
from model import Model


def draw_predictions(content: str):
    with st.spinner("Inference in progress. Please wait."):
        sleep(5)
    st.markdown("---")
    with open('model.pkl', 'rb') as fp:
        model = pickle.load(fp)
    col1, col2 = st.columns(2)
    results = model.infer(content)
    pd.options.plotting.backend = "plotly"

    with col1:
        st.success("Inference succeeded. Observe the predictions below.")
        st.download_button("Download predicitons", results.to_csv(), file_name="predicitons.csv")
        st.plotly_chart(results.plot())
        st.plotly_chart(results.hist())
        st.dataframe(results)

    with col2:
        st.code("""
def draw_predictions(content: str):
    with open('model.pkl', 'rb') as fp:
            model = pickle.load(fp)
    results = model.infer(content)
    pd.options.plotting.backend = "plotly"
    st.success("Inference succeeded. Observe the predicitons below.")
    st.download_button("Download predicitons", results.to_csv(), file_name="predicitons.csv")
    st.plotly_chart(results.plot())
    st.plotly_chart(results.hist())
    st.dataframe(results)
    """, language="python")


def inference():
    st.title("Model inference")
    st.markdown("---")
    st.header("Input")
    col1, col2 = st.columns(2)

    form = col1.form("inference_form")
    file_val = form.file_uploader("Input data", type="json")
    if form.form_submit_button():
        try:
            content = json.loads(file_val.getvalue().decode('utf8'))
            with col1.expander('Uploaded content'):
                st.write(content)
        except:
            st.error("Uploading file is mandatory!")
        try:
            draw_predictions(content)
        except:
            pass

    col2.code("""
form = st.form("inference_form")
file_val = form.file_uploader("Input data", type="json")
if form.form_submit_button():
    try:
        content = json.loads(file_val.getvalue().decode('utf8'))
        with st.expander('Uploaded content'):
            st.write(content)
        draw_predictions(content)       
    except:
        st.error("Uploading file is mandatory!")
""")
