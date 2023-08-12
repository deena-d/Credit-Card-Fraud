import numpy as np
import pickle
import streamlit as st

# Loading model
loaded_model = pickle.load(open('D:/web_app/trained.sav', 'rb'))

# Creating function
def ccpred(input_data):
    input_data_as_numpy_array = np.array(input_data, dtype=float)  # Convert input to numeric values
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "Normal Transaction"
    else:
        return "Fraudulent Transaction"

def main():
    st.title("Credit card fraud detection")

    # Getting data
    Time = st.text_input("Time required for transaction")
    V1 = st.text_input("1st transaction")
    V2 = st.text_input("2st transaction")
    V3 = st.text_input("3st transaction")
    V4 = st.text_input("4st transaction")
    V5 = st.text_input("5st transaction")
    V6 = st.text_input("6st transaction")
    V7 = st.text_input("7st transaction")
    V8 = st.text_input("8st transaction")
    V9 = st.text_input("9st transaction")
    V10 = st.text_input("10st transaction")
    Amount = st.text_input("Total amount transaction")

    # Code for prediction
    credittest = ''

    # Creating button for prediction
    if st.button('Credit Card Test Result'):
        credittest = ccpred([Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, Amount])

    st.success(credittest)

main()
