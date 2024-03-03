# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/surya/OneDrive/Desktop/FINAL PROJECT/SAVED MODEL/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/surya/OneDrive/Desktop/FINAL PROJECT/SAVED MODEL/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/surya/OneDrive/Desktop/FINAL PROJECT/SAVED MODEL/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Create columns for input fields
    col1, col2, col3 = st.columns(3)
    
    # Input fields
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        BMI = st.text_input('BMI value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    # Initialize the prediction result
    diab_diagnosis = ''
    
    # Create a button for prediction
    if st.button('Diabetes Test Result'):
        # Convert input values to numeric
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)
        
        # Make the prediction
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is predicted to have diabetes'
        else:
            diab_diagnosis = 'The person is predicted to not have diabetes'
        
    # Display the prediction result
    st.success(diab_diagnosis)




if selected == 'Heart Disease Prediction':
    
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Create columns for input fields
    col1, col2, col3 = st.columns(3)
    
    # Input fields
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        exang = st.text_input('Exercise Induced Angina')
        
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        oldpeak = st.text_input('ST depression induced by exercise')
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        ca = st.text_input('Major vessels colored by flourosopy')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    # Initialize the prediction result
    heart_diagnosis = ''
    
    # Create a button for prediction
    if st.button('Heart Disease Test Result'):
        # Convert input values to numeric
        age = float(age)
        sex = int(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
        
        # Make the prediction
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is predicted to have heart disease'
        else:
            heart_diagnosis = 'The person is predicted to not have heart disease'
        
    # Display the prediction result
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
# Parkinson's Disease Prediction Page
if selected == "Parkinsons Prediction":
    
    # Page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # Create columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Input fields
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        APQ = st.text_input('MDVP:APQ')
        NHR = st.text_input('NHR')
        RPDE = st.text_input('RPDE')
        spread2 = st.text_input('spread2')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        PPQ = st.text_input('MDVP:PPQ')
        APQ5 = st.text_input('Shimmer:APQ5')
        DDA = st.text_input('Shimmer:DDA')
        HNR = st.text_input('HNR')
        DFA = st.text_input('DFA')
        D2 = st.text_input('D2')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        spread1 = st.text_input('spread1')
        PPE = st.text_input('PPE')
        
    with col4:
        DDP = st.text_input('Jitter:DDP')
        
    with col5:
        # Leave this column empty (for formatting)
        pass
    
    # Initialize the prediction result
    parkinsons_diagnosis = ''
    
    # Create a button for prediction
    if st.button("Parkinson's Test Result"):
        # Convert input values to float
        fo = float(fo)
        fhi = float(fhi)
        flo = float(flo)
        Jitter_percent = float(Jitter_percent)
        Jitter_Abs = float(Jitter_Abs)
        RAP = float(RAP)
        PPQ = float(PPQ)
        DDP = float(DDP)
        Shimmer = float(Shimmer)
        Shimmer_dB = float(Shimmer_dB)
        APQ3 = float(APQ3)
        APQ5 = float(APQ5)
        APQ = float(APQ)
        DDA = float(DDA)
        NHR = float(NHR)
        HNR = float(HNR)
        RPDE = float(RPDE)
        DFA = float(DFA)
        spread1 = float(spread1)
        spread2 = float(spread2)
        D2 = float(D2)
        PPE = float(PPE)
        
        # Make the prediction
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person is predicted to have Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person is predicted to not have Parkinson's disease"
        
    # Display the prediction result
    st.success(parkinsons_diagnosis)

