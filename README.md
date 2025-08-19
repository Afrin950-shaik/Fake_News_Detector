# Fake News Detection App

A simple **Fake News Detection Web App** built with **Python, Streamlit, and Scikit-learn**.  
It uses a **Machine Learning model (LinearSVC)** with **TF-IDF Vectorizer** to classify news headlines as **FAKE or REAL**.

---

##  Features
- Enter any news headline and check if it’s fake or real.
- Built with **Streamlit** for an interactive web UI.
- Trained using **TF-IDF + LinearSVC** model.
- Lightweight and easy to run locally.

---

##  Project Structure
```
Fake-News-Detection/
│
├── app.py                # Streamlit web app
├── fake_news_model.pkl   # Trained ML model
├── analysis.ipynb        # Jupyter notebook (training & analysis)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

##  Installation & Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/fake-news-detection.git
   cd fake-news-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

##  Requirements
- Python 3.8+
- scikit-learn
- streamlit
- pandas
- numpy

(These are already listed in `requirements.txt`)

---



##  Future Improvements
- Deploy the app on **Streamlit Cloud / Heroku / Render**.
- Support for full news articles, not just headlines.
- Try deep learning models for better accuracy.

---

##  Author
- Shaik Afrin

