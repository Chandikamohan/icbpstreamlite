import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
 
st.write(f"## Disease Prediction Application")
st.write("Author: Chandika Mohan_ICBP KT")
 
 
# Loaded the model
heat_disease_model = pickle.load(open("models/heart_disease_model1.sav", "rb"))
diabetes_model = pickle.load(open("models/diabetes_model.sav", "rb"))
parkinsons_model = pickle.load(open("models/parkinsons_model.sav", "rb"))

with st.sidebar:
    selected = option_menu("Choose the Disease", ["Haert Disease Prediction", "Diabetes Prediction","Parkinsons Preciction"])
 
 
if selected == "Haert Disease Prediction":
    st.write(f"## Heart Disease Prediction")
 
    # Code of Heart disease prediction
    # Heart disease
    st.write("Please Provide your Details")
    # Created the columns
    col1, col2  = st.columns(2)
    # Taking User Inputs
    with col1:
        age = st.text_input("Type your age")
        sex = st.text_input("Type your age for Male:1 and Female: 0")
        cp = st.text_input("Type your cp")
        trestbps = st.text_input("Type your trestbps")
        chol = st.text_input("Type your chol")
        fbs = st.text_input("Type your fbs")
        restecg = st.text_input("Type your restecg")
 
    with col2:
        thalach = st.text_input("Type your thalach")
        exang = st.text_input("Type your exang")
        oldpeak = st.text_input("Type your oldpeak")
        slope = st.text_input("Type your slope")
        ca = st.text_input("Type your ca")
        thal = st.text_input("Type your thal")
 
    if st.button("Predict"):
        data = [age, sex, cp, trestbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]
        data_array = np.array(data, dtype=float).reshape(1,-1)
        prediction = heat_disease_model.predict(data_array)
        st.write(f"## Prediction: {prediction}")
 
 
 
if selected == "Diabetes Prediction":
    st.write(f"## Diabetes Prediction")
    # Take User inputs
    col1, col2, col3= st.columns(3)
   
    with col1:
        Pregnancies = st.text_input('No of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI')
 
    if st.button("Predict"):
        data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]
        data_array = np.array(data, dtype=float).reshape(1,-1)
        prediction = diabetes_model.predict(data_array)
        st.write(f"## Prediction: {prediction}")
if selected == "Parkinsons Preciction":
    st.write(f"## Parkinsons Preciction")
    # Take User inputs
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('Fo(Hz)')
        RAP = st.text_input('RAP')
        APQ3 = st.text_input('APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        PPQ = st.text_input('PPQ')
        APQ5 = st.text_input('APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
       
    with col3:
        flo = st.text_input('Flo(Hz)')
        DDP = st.text_input('DDP')
        APQ = st.text_input('APQ')
        DFA = st.text_input('DFA')
 
       
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
        Shimmer = st.text_input('Shimmer')
        DDA = st.text_input('DDA')
        spread1 = st.text_input('spread1')
       
    with col5:
        Jitter_Abs = st.text_input('Jitter(Abs)')
        Shimmer_dB = st.text_input('Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')  
 