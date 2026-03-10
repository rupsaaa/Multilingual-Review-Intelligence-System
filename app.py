'''To run:
venv\Scripts\activate 
streamlit run app.py'''

import streamlit as st
from predict import predict_sentiment

st.set_page_config(page_title="Multilingual Review Intelligence System")

st.title("🌍 Multilingual Review Intelligence System")
st.write("Enter your review in any language:")

user_input = st.text_area("Review")

if st.button("Analyze Sentiment"):
    if user_input.strip() != "":
        translated_text, sentiment = predict_sentiment(user_input)

        st.subheader("Translated Text:")
        st.write(translated_text)

        st.subheader("Predicted Sentiment:")
        if sentiment.lower().strip() == "positive":
            st.success("Positive 😊")
        else:
            st.error("Negative 😡")
    else:
        st.warning("Please enter a review.")
