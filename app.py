import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Creating a UI to enter data from User
st.title("Welcome to Customer Churn Prediction System")
senior=st.radio('Is Customer a Senior Citizen?',['Yes','No'])
partner=st.radio('Is he/she a Partner?',['Yes','No'])
dependents=st.radio('Is your Customer Dependent?',['Yes','No'])
tenure=st.slider('Enter tenure',min_value=0,max_value=100)
phone=st.radio('Do they have Phone Service?',['Yes','No'])
multiple_lines=st.radio('Do they have multiple Lines?',['Yes','No'])
internet=st.selectbox('What is the Internet Service Type?',['DSL','Fiber optic','No'])
online_security=st.radio('Do you provide Online Security?',['Yes','No'])
backup=st.radio('Do you have Online Backup?',['Yes','No'])
device_protection=st.radio('Do you provide Device Protection?',['Yes','No'])
tech_support=st.radio('Do your company have Tech Support?',['Yes','No'])
streaming_tv=st.radio('Is Customer using Streaming TV?',['Yes','No','No internet service'])
streaming_movies=st.radio('Is Customer using Streaming movies?',['Yes','No','No internet service'])
contract=st.selectbox('What is the type of Contract?',['Month-to-month', 'One year', 'Two year'])
paperless=st.radio('Do you provide Paperless Billing?',['Yes','No'])
payment=st.selectbox('What is the Payment Method?',['Electronic check', 'Mailed check', 'Bank transfer (automatic)'])
monthly_charges=st.number_input("Enter Monthly Charges:")
st.write("Montly Charges is:",monthly_charges)
total=st.number_input('Total Charges:')
st.write('Total Charges is :',total)
buttons=st.button('Predict')

# Label Encoding
senior=1 if senior=='Yes' else 0
partner =1 if partner=='Yes' else 0
dependents =1 if dependents=='Yes' else 0
phone =1 if phone=='Yes' else 0
multiple_lines =1 if multiple_lines=='Yes' else 0
online_security =1 if online_security=='Yes' else 0
backup =1 if backup=='Yes' else 0
device_protection =1 if device_protection=='Yes' else 0
tech_support =1 if tech_support=='Yes' else 0

paperless=1 if paperless=='Yes' else 0
internet_dict={'DSL':0,'Fiber optic':1,'No':2}
contract_dict={'Month-to-month':0, 'One year':1, 'Two year':2}
payment_dict={'Electronic check':1, 'Mailed check':2, 'Bank transfer (automatic)':0}
stream={'Yes':2,'No':0,'No internet service':1}
internet=internet_dict[internet]
contract=contract_dict[contract]
payment=payment_dict[payment]
streaming_tv =stream[streaming_tv]
streaming_movies =stream[streaming_movies]
streaming_movies =1 if streaming_movies=='Yes' else 0

# Loading the model
model=joblib.load('model.pt')
df=pd.DataFrame([
    senior,partner,dependents,tenure,phone,multiple_lines,internet,online_security,
                  backup,device_protection,tech_support,streaming_tv,streaming_movies,contract,paperless,payment,monthly_charges,total
]).T
if buttons==True:
    y_pred=model.predict(df)
    if y_pred==0:
        res='Customer will probably Stay 😄'
    else:
        res='Customer may leave the service.⚠️'
    st.write(res)