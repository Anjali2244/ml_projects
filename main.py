#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle
import streamlit as st


infile = open('ClassLog', 'rb')
lr = pickle.load(infile)
infile.close()

st.title("Machine Learning Project")
st.header("Brain Stroke Prediction")

gender = st.selectbox("Gender", ("Male", "Female"))
if gender == "Male":
    gender = 1
else :
    gender = 0

age = st.number_input("Enter your Age")

hypertension = st.number_input("Input if you have hypertension as either 1 for Yes or 0 for No as int")

heart_disease = st.number_input("Input if you have heart_disease as either 1 for Yes or 0 for No as int")

married = st.selectbox("Have you ever been married?", ("Yes", "No"))
if married == "Yes":
    married = 1
else :
    married = 0

job_status = st.selectbox("Your current work type", ("Private", "Self-employed", "Govt_job", "children"))
if job_status == "Private" :
    job_status = 1
elif job_status == "Self-employed" :
    job_status = 2
elif job_status == "Govt_job" :
    job_status = 0
else :
    job_status = 3

residence = st.selectbox("Your Residence type", ("Urban", "rural"))
if residence == "Urban" :
    residence = 1
else :
    residence = 0

glucose = st.number_input("Your Average glucose level ")

bmi = st.number_input("Your BMI")

smoke = st.selectbox("Ever Smoked", ("formerly_smoked", "never smoked", "smokes", "unknown"))
if smoke == "formerly_smoked" :
    smoke = 1
elif smoke == "never smoked":
    smoke = 2
elif smoke == "smokes":
    smoke = 3
else :
    smoke = 0

if st.button("Submit"):
    output = lr.predict([[gender,age,hypertension,heart_disease,married,job_status,residence,glucose,bmi,smoke]])
    if str(output) == "1" :
        st.write("Could have stroke")
    else :
        st.write("No stroke")

