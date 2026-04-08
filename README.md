# 🚀 AI Trigram Word Predictor & Sentence Completer  

A smart and interactive **Natural Language Processing (NLP)** application that predicts the next word in a sentence using a **Trigram Language Model**.  

This project combines **probabilistic modeling**, **incremental learning**, and a **modern GUI** to deliver an intuitive and adaptive text prediction experience.

---

## 📌 Overview  

The AI Trigram Word Predictor analyzes sequences of words and predicts the most likely next word based on previously seen patterns.  

It is designed for:
- Learning NLP fundamentals  
- Understanding language models  
- Building interactive AI-based applications  

---

## ✨ Features  

### 🔹 Trigram Language Model  
- Predicts next word using:  
  P(w₃ | w₁, w₂)  
- Uses contextual probability of the previous two words  

### 🔹 Laplace (Add-One) Smoothing  
- Handles unseen word combinations  
- Prevents zero probability issues  

### 🔹 Incremental Learning 🧠  
- Users can teach new sentences directly  
- Model adapts to personal writing style  
- Example: `"My name is Malaika"`  

### 🔹 Modern GUI (Tkinter)  
- Dark-themed, visually appealing interface  
- Interactive buttons for predictions  
- Real-time user feedback  

### 🔹 Pre-training Support (IMDb Dataset)  
- Compatible with **aclImdb movie review dataset**  
- Enhances vocabulary and prediction accuracy  

---

## 🛠️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/YOUR_USERNAME/Trigram-Word-Predictor.git
cd Trigram-Word-Predictor
```

### 2️⃣ Install Dependencies  
Make sure Python is installed, then run:
```bash
pip install nltk
```

### 3️⃣ Prepare Dataset (Optional)  
- Download the **aclImdb dataset**  
- Place the `aclImdb` folder inside the project directory  

> 💡 If you skip this step, you can still train the model using the GUI's Incremental Learning feature.

---

## 🚀 How to Use  

### ▶️ Run the Application  
```bash
python word-predictor.py
```

### ✍️ Predict Words  
- Enter at least **two words**  
- Top 3 predictions will appear as buttons  

### 🔘 Complete Sentence  
- Click any suggested word  
- It will be appended to your text  

### 🧠 Train the Model  
- Enter a custom sentence  
- Click **"Add to Memory 🧠"**  
- Model learns and updates instantly  

---

## 📊 Technical Details  

The probability of the next word is calculated using:

P(w₃ | w₁, w₂) = (count(w₁, w₂, w₃) + α) / (count(w₁, w₂) + α × V)

Where:  
- w₁, w₂, w₃ = sequence of words  
- α = smoothing parameter (Laplace smoothing)  
- V = vocabulary size  

---

## 🧠 Key Concepts Used  

- Natural Language Processing (NLP)  
- N-gram Language Models  
- Probability & Statistics  
- Laplace Smoothing  
- GUI Development with Tkinter  

---

## 📂 Project Structure  

```
Trigram-Word-Predictor/
│── word-predictor.py
│── README.md
│── aclImdb/ (optional dataset)
│── requirements.txt (optional)
```

---

## 🎯 Future Improvements  

- Add Bigram & Neural Language Models  
- Improve UI with advanced frameworks (e.g., PyQt / Web App)  
- Add real-time auto-complete suggestions  
- Integrate deep learning models (LSTM / Transformers)  

---