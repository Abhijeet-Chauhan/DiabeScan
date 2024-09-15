import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components

'''Made By Abhijeet'''


loaded_model = pickle.load(open('C:/Users/abhij/Desktop/Projects/ML/trained_model.sav', 'rb'))


def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


navbar_html = """
    <style>
    .navbar {
        padding: 10px;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .navbar a {
        color: black;
        margin: 0 20px;
        text-decoration: none;
    }
    .navbar a img {
        vertical-align: middle;
        width: 24px;
        height: 24px;
    }
    .navbar a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="navbar">
        <a href="https://github.com/abhijeet-chauhan" target="_blank">
            <img src="https://img.icons8.com/material-outlined/24/000000/github.png" alt="GitHub"/> 
        </a>
    </div>
"""

def main():
    st.title('DiabeScan 💉')


    components.html(navbar_html, height=50, scrolling=False)

    try:
        Pregnancies = float(st.text_input('Number of Pregnancies', ''))
        Glucose = float(st.text_input('Glucose Level', ''))
        BloodPressure = float(st.text_input('Blood Pressure value', ''))
        SkinThickness = float(st.text_input('Skin Thickness value', ''))
        Insulin = float(st.text_input('Insulin Level', ''))
        BMI = float(st.text_input('BMI value', ''))
        DiabetesPedigreeFunction = float(st.text_input('Diabetes Pedigree Function value', ''))
        Age = float(st.text_input('Age of the Person', ''))
        
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        

        if st.button('Diabetes Test Result'):
            diagnosis = diabetes_prediction(input_data)
            st.success(diagnosis)
    except ValueError:
        st.error("Please enter valid numerical values for all inputs.")


    footer_html = """
    <style>
    .footer {
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
        border-top: 1px solid #ddd;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ by Group 6️⃣</p>
    </div>
    """
    components.html(footer_html, height=50, scrolling=False)

if __name__ == '__main__':
    main()
