import streamlit as st
import numpy as np

#load ML package
import joblib
import os

gen = {'Male':1, 'Female':0}
mer = {'Yes':1, 'No':0}
work = {'Private':1, 'Self-employed':1, 'Govt_job':1, 'children':1, 'Never_worked':1}
resi = {'Urban':1, 'Rural':0}
smoke = {'formerly smoked':1, 'never smoked':1, 'smokes':1, 'unknown':1}
        
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
        
@st.cache(allow_output_mutation=True)
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model

def run_ml_app():

    st.subheader("Input Your Data")
    gender = st.selectbox('Gender', ["Male", "Female"])
    age = st.number_input('Age')
    hypertension = st.radio('hypertension', [0,1])
    heart_disease = st.radio('Heart Disease', [0,1])
    ever_married = st.selectbox("Ever Married", ['Yes', 'No'])
    work_type = st.selectbox("Work Type", ['Private','Self-employed','Govt_job','children','Never_worked'])
    Residence_type = st.selectbox("Residence Type",['Urban','Rural'])
    avg_glucose_level = st.number_input("Avg Glucose Level")
    bmi = st.number_input("BMI")
    smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes', 'unknown'])
    Diabetes = st.radio("Diabetes",[0,1])

    with st.expander("Your Selected Options"):
        result = {
            'Gender':gender,
            'Age':age,
            'Hypertention':hypertension,
            'Heart Disease':heart_disease,
            'Ever Married': ever_married,
            'Residence Type': Residence_type,
            'Avg Glucose Level':avg_glucose_level,
            'BMI':bmi,
            'Diabetes': Diabetes,
            'work_type_Govt_job':0,
            'work_type_Never_worked':0,
            'work_type_Private':0,
            'work_type_Self-employed':0,
            'work_type_children':0,
            'smoking_status_Unknown':0,
            'smoking_status_formerly smoked':0,
            'smoking_status_never smoked':0,
            'smoking_status_smokes':0,
            'work type' : work_type,
            'smoking status' :smoking_status,
        }

#Change Work_Type and smoking_status value
    for i in result.values():
        if i == "Private" :
          result['work_type_Private'] = 1
        elif i == "Self-employed" :
          result['work_type_Self-employed'] = 1
        elif i == "Govt_job" :
          result['work_type_Govt_job'] = 1
        elif i == "children" :
          result['work_type_children'] = 1
        elif i == "Never_worked" :
          result['work_type_Never_worked'] = 1
        elif i == "unknown" :
          result['smoking_status_Unknown'] = 1
        elif i == "formerly smoked" :
          result['smoking_status_formerly smoked'] = 1
        elif i == "never smoked" :
          result['smoking_status_never smoked'] = 1
        elif i == "smokes" :
          result['smoking_status_smokes'] = 1
          
    #st.write(result)

#Erase unnecessary columns
    result.pop('work type')
    result.pop('smoking status')
    result

    encoded_result = []
    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif type(i) == float:
            encoded_result.append(i)
        elif i in ["Male", "Female"]:
            res = get_value(i, gen)
            encoded_result.append(res)
        elif i in ["Yes", "No"]:
            res = get_value(i, mer)
            encoded_result.append(res)
        elif i in ["Private", "Self-employed", "Govt_job", "children","Never_work"]:
            res = get_value(i, work)
            encoded_result.append(res)
        elif i in ['Urban','Rural']:
            res = get_value(i, resi)
            encoded_result.append(res)
        elif i in ["formerly smoked", "never smoked", "smokes","unknown"]:
            res = get_value(i, smoke)
            encoded_result.append(res)
   

    #st.write(encoded_result)

# prediction section
    st.subheader('Prediction Result')
    single_sample = np.array(encoded_result).reshape(1,-1)
    #st.write(single_sample)

    model = load_model("model_RandFor.pkl")

    prediction = model.predict(single_sample)
    pred_proba = model.predict_proba(single_sample)
    #st.write(prediction)
    #st.write(pred_proba)
    pred_probability_score = {'1':round(pred_proba[0][1]*100,4),
                                '0':round(pred_proba[0][0]*100,4)}
    
    
    if st.button('Prediction Test'):
        if prediction == 1:
          st.warning("Wow, your risk of having a stroke is very large. Let's change our lifestyle to be healthier!")
          #st.write(pred_probability_score)
        else:
          st.success("Congratulations, your risk of stroke is very small!  Keep up the spirit to maintain a healthy lifestyle!")
          #st.write(pred_probability_score)