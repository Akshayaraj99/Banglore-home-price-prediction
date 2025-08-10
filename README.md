#  Bangalore Home Price Prediction

##  Overview  
This project predicts house prices in Bangalore based on various features such as location, size, total square feet, and number of bathrooms.  
It uses a **Machine Learning model built with Linear Regression** to estimate property prices.  
The backend is developed with **Python (Flask)**, and the frontend is built using HTML, CSS, and JavaScript.  

## Features  
- Predict house prices based on user input.  
- Data cleaning and preprocessing pipeline.  
- Model trained using `scikit-learn`.  
- Web interface built with Flask.  

## Technologies Used  
- Python  
- Pandas, NumPy, Matplotlib, Scikit-learn  
- Flask (for deployment)  
- HTML, CSS, JavaScript  

##  Project Structure  
BHP/
│-- Model/
│   ├── bangalore_home_prices_model.pickle
│   ├── columns.json
│-- Server/
│   ├── server.py
│   ├── util.py
│-- Client/
│   ├── app.html
│   ├── app.js
│   ├── app.css

## Dataset  
The dataset was sourced from Kaggle's Bangalore house price data and contains features like:  
- Location  
- Size (BHK)  
- Total square feet  
- Number of bathrooms  
- Price  

## Installation & Usage  
1. **Clone the repository**  
```bash
git clone git@github.com:Akshayaraj99/Banglore-home-price-prediction.git
cd Banglore-home-price-prediction

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the server locally**
python server.py

## Access the app
https://mybhpapp.duckdns.org/


