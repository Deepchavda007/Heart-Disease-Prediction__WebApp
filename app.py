import pickle
import streamlit as st


heart_disease_model = pickle.load(open(
    'heart_disease_model.sav', 'rb'))
st.title('Heart Disease Prediction')

st.text(" SEX : ( Male = 1 | Female = 0 )")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', max_value=70, min_value=0)

with col2:
    sex = st.number_input('Sex', max_value=1, step=1, min_value=0)

with col3:
    cp = st.number_input('Chest Pain types', max_value=3, step=1, min_value=0)

with col1:
    trestbps = st.number_input(
        'Resting Blood Pressure', max_value=200, min_value=0)

with col2:
    chol = st.number_input('Serum Cholestoral in mg/dl',
                           max_value=500, min_value=0)

with col3:
    fbs = st.number_input(
        'Fasting Blood Sugar > 120 mg/dl', max_value=1, step=1, min_value=0)

with col1:
    restecg = st.number_input(
        'Resting Electrocardiographic results', max_value=1, step=1, min_value=0)

with col2:
    thalach = st.number_input(
        'Maximum Heart Rate achieved', max_value=200, min_value=0)

with col3:
    exang = st.number_input('Exercise Induced Angina',
                            max_value=1, step=1, min_value=0)

with col1:
    oldpeak = st.number_input(
        'ST depression induced by exercise', max_value=5.0, step=0.5, min_value=0.0)

with col2:
    slope = st.number_input(
        'Slope of the peak exercise ST segment', max_value=2, step=1, min_value=0)

with col3:
    ca = st.number_input(
        'Major vessels colored by flourosopy', max_value=2, step=1, min_value=0)

with col1:
    thal = st.number_input(
        'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', max_value=3, step=1, min_value=0)

# code for Prediction
heart_diagnosis = ''


# creating a button for Prediction

if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
        st.error(heart_diagnosis)
    else:
        heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
        st.balloons()
