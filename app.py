import streamlit as st
import joblib

model=joblib.load(r"C:\Users\masthan\fake_news_model.pkl")
vectorizer=joblib.load(r"C:\Users\masthan\tfidf_vectorizer.pkl")

st.title("Fake News Detector")

headline=st.text_input("Enter a news headline:")

if st.button("Predict"):
    if headline.strip() != "":
        vec_input=vectorizer.transform([headline])

        prediction=model.predict(vec_input)[0]

        st.write("Prediction:" ,"Fake News" if prediction=="fake" else "Real News")
    else:
        st.warning("Please enter a headline.")
