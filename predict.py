import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from translate import translate_to_english
import pickle

# Load model
model = load_model("model/sentiment_model.h5")

# Load tokenizer
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def predict_sentiment(text):

    translated_text = translate_to_english(text)
    sequence = tokenizer.texts_to_sequences([translated_text])
    padded = pad_sequences(sequence, maxlen=100)
    prediction = model.predict(padded)[0][0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    return translated_text, sentiment