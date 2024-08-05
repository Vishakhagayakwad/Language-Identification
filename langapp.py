
import streamlit as st
import pickle

# Load the pre-trained model and CountVectorizer
model_filename = 'language_model.pkl'
cv_filename = 'transform1.pkl'

clf = pickle.load(open(model_filename, 'rb'))
cv = pickle.load(open(cv_filename, 'rb'))

# Title of the web app
st.title('Language Detector')

st.write("Enter a text snippet to predict its language")

user_input = st.text_area("Enter Text:")

if st.button("Predict Language"):
    if user_input:
        data = cv.transform([user_input]).toarray()
        output = clf.predict(data)
        st.write(f"The predicted language is: {output[0]}")
    else:
        st.write("Please enter some text for prediction.")
