# Trading AI GUI App

## 📌 Introduction
This **Trading AI GUI App** is a Python-based application that helps traders analyze stock and crypto markets using AI. The app predicts **Stop-Loss (SL), Target Price, and Profit & Loss probability** based on past data and patterns. It provides a user-friendly **Graphical User Interface (GUI)** for better usability.

---

## 🚀 Features
- **Fetch Live Market Data** (Stock & Crypto Prices)
- **AI-based Stop-Loss & Target Price Prediction**
- **Profit/Loss Probability Analysis**
- **User Input for Custom SL & Target**
- **Graphical UI for Better Trading Experience**

---

## 🛠️ Tech Stack
- **Python** (Backend & AI Model)
- **Tkinter** (GUI Development)
- **yFinance** (Stock Market Data)
- **pandas, numpy** (Data Processing)
- **scikit-learn** (ML Model for SL & Target Prediction)

---

## 📂 Project Structure
```
Trading_AI_GUI/
│── train_ai_model.py      # AI Model Training Script
│── trading_gui.py         # GUI-Based Trading Application
│── requirements.txt       # Required Libraries
│── stock_list.csv         # List of Stock Symbols
│── README.md              # Documentation
```

---

## 🔧 Installation
### 1️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run AI Model Training Script
```bash
python train_ai_model.py
```

### 3️⃣ Run the GUI Application
```bash
python trading_gui.py
```

---

## 🎯 How It Works
1. **Start the GUI App** (`trading_gui.py`)
2. **Select Stock or Crypto** from the dropdown menu
3. **Click on 'Predict' Button**
4. AI Model will **Suggest SL & Target** based on past data
5. You can **Modify SL/Target Manually**
6. View **Profit & Loss Probability** before trading

---

## 🔮 Future Enhancements
- **Auto Buy/Sell Trading Signals**
- **Deep Learning Model for Better Accuracy**
- **Web-Based Version for Multi-Platform Support**
- **Live Market News & Insights**

---

## 🤝 Contributing
Pull requests are welcome! If you have suggestions or find any bugs, feel free to **open an issue**.

---
🔥 Happy Trading with AI! 🚀

