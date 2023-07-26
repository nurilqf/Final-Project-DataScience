# main Python app
import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app

html_temp = """
            <div style="background-color:#006e7f;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Stroke Prediction App </h1>
		    <h4 style="color:white;text-align:center;">by Garuda Team</h4>
		    </div>
            """

desc_temp = """
            ### Stroke Prediction App
            This app will be used by healthcare analysts to predict whether patients are affected by a stroke or not.
            #### Data Source
            - https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
            #### App Content
            - Machine Learning Section
            """



def main():
    st.title("Main App")
    stc.html(html_temp)

    menu = ["Home","Machine Learning"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        st.subheader("Machine Learning Testing")
        run_ml_app()
   
if __name__ == '__main__':
    main()