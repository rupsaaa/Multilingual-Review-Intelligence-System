import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
import pickle

# Load dataset
df = pd.read_csv("data/reviews.csv")

# Convert sentiment to binary
df['sentiment'] = df['sentiment'].map({'positive':1, 'negative':0})

# Tokenization
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(df['review'])

# SAVE TOKENIZER AFTER FITTING
with open("model/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

sequences = tokenizer.texts_to_sequences(df['review'])
padded = pad_sequences(sequences, maxlen=100)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    padded, df['sentiment'], test_size=0.2, random_state=42
)

# Build RNN Model
model = Sequential()
model.add(Embedding(5000, 64, input_length=100))
model.add(SimpleRNN(64))
model.add(Dense(1, activation='sigmoid'))

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=5, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

# Save model
model.save("model/sentiment_model.h5")