# 🌍 Multilingual Review Intelligence System

A Machine Learning based system that analyzes product reviews written in **multiple languages** and predicts whether the sentiment is **Positive or Negative**.

The system automatically **translates reviews into English** before performing sentiment analysis using a **Neural Network model built with TensorFlow/Keras**.

---

# 📌 Project Overview

Many online platforms receive reviews from users across the world in different languages. Traditional sentiment analysis models usually work only for English text.

This project solves that problem by:

1. Accepting reviews in **any language**
2. **Translating them to English**
3. Performing **sentiment analysis**
4. Displaying the **translated text and sentiment prediction**

---

# 🧠 Features

• Multilingual review input  
• Automatic translation to English  
• Neural network sentiment analysis  
• Web interface built with **Streamlit**  
• Real-time prediction  
• Tokenizer persistence for consistent predictions

---

# 🏗️ Project Architecture

<img width="1024" height="1536" alt="architecture" src="https://github.com/user-attachments/assets/5cc9db54-029e-4f52-8941-e83264c5c2bd" />

---

# 📂 Project Structure
```
Multilingual_Review_Intelligence_System/
│
├── data/
│   └── reviews.csv
│
├── model/
│   ├── sentiment_model.h5
│   └── tokenizer.pkl
│
├── train_model.py        # Script to train the sentiment model
├── predict.py            # Handles prediction logic
├── translate.py          # Translates multilingual reviews to English
├── app.py                # Streamlit frontend application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

# ⚙️ Technologies Used

### Programming Language
Python

### Libraries

- pandas
- numpy
- scikit-learn
- tensorflow / keras
- streamlit
- openai API
- langdetect

---

# 🤖 Machine Learning Model

The sentiment classification model uses a **Recurrent Neural Network (RNN)** architecture.

### Model Architecture

Embedding Layer  
↓  
SimpleRNN Layer  
↓  
Dense Output Layer (Sigmoid)

### Training Details

Optimizer: Adam  
Loss Function: Binary Crossentropy  
Epochs: 5  
Batch Size: 32

---

# 🔄 Prediction Workflow

1️⃣ User enters review text  
2️⃣ Review is translated into English  
3️⃣ Text is tokenized using trained tokenizer  
4️⃣ Sequence is padded  
5️⃣ Model predicts sentiment probability  
6️⃣ Sentiment is displayed as Positive or Negative

---

# 🚀 How to Run the Project

### Step 1: Clone Repository
    https://github.com/rupsaaa/Multilingual-Review-Intelligence-System.git

### Step 2: Navigate to Project   
    cd Multilingual-Review-Intelligence-System

### Step 3: Create Virtual Environment
    python -m venv venv

### Step 4: Activate Environment

### Windows:
    venv\Scripts\activate

### Mac/Linux:
    source venv/bin/activate

### Step 5: Install Dependencies
    pip install -r requirements.txt

### Step 6: Train Model (Optional)
      python train_model.py
      
### Step 7: Run Streamlit App
      streamlit run app.py


---

## 🖥️ Application Output

<img width="1919" height="1079" alt="Screenshot 2026-03-10 085156" src="https://github.com/user-attachments/assets/3f9c156a-207c-4517-a702-1b5fc9e10fce" />

<img width="1919" height="1079" alt="Screenshot 2026-03-10 085547" src="https://github.com/user-attachments/assets/acc828a4-633a-4212-b986-059fd498d2b1" />

---

# ⚠️ Limitations

• Current model uses SimpleRNN which may not capture long-term dependencies  
• Accuracy ~80–85% depending on dataset  
• Translation quality may affect sentiment prediction  

---

# 🔮 Future Improvements

• Replace RNN with **LSTM or Transformer models**  
• Add **Fake Review Detection**  
• Implement **Sentiment Confidence Score**  
• Support **Neutral sentiment class**  
• Train on larger multilingual datasets  

---

# 👩‍💻 Author

Rupsa Bhattacharjee  

---
    
  




