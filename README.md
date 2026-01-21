# Text Emotion Detection using NLP

This project performs **emotion detection from text input** using a **pre-trained transformer-based NLP model**.  
It classifies text into emotions such as **joy, sadness, anger, fear, surprise, and neutral**.

---

## 🚀 Features
- Detects emotions from user-entered text
- Uses a pre-trained **DistilRoBERTa** model
- No training required
- Simple and clean Python implementation
- Easy to extend into web applications

---

## 🛠️ Tech Stack
- Python
- Hugging Face Transformers
- PyTorch

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PrasadDesai04/text-emotion-detection.git
cd text-emotion-detection

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run
python emotion_detector.py


Enter any sentence when prompted and the model will output emotion probabilities.

📌 Example Input
I am feeling very sad and disappointed today.

Example Output
sadness : 0.87
anger   : 0.08
joy     : 0.03
fear    : 0.01

🧠 How It Works

The input text is passed to a pre-trained transformer model

The model converts text into embeddings

A classification head predicts emotion probabilities

🔮 Future Improvements

Web interface using Streamlit or Flask

Emotion + sentiment analysis

CSV/Database logging

Multilingual support

👤 Author

Prasad Desai

⭐ Why This Project?

This project demonstrates practical usage of NLP and transformer models for real-world applications such as chatbots, mental health analysis, and feedback systems.
