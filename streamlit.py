import pickle
import streamlit as st
model=pickle.load(open(r"C:\Users\diyan\Documents\Machine learning\Supervised\Regression\Linear regression\hiring_model",'rb'))
experience=st.number_input('enter experience')
test_score=st.number_input('enter test score')
interview_score=st.number_input('enter interview score')

if st.button('check'):
    predicted=model.predict([[experience,test_score,interview_score]])
    st.success(predicted)