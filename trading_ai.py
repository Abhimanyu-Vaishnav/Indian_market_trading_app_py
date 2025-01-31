import tkinter as tk
from tkinter import Label, Button
import yfinance as yf
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load Trained AI Model
model = load_model("ai_trading_model.h5")
scaler = MinMaxScaler()

# Function to Get Price & Predict Next Target
def get_price():
    symbol = entry.get()  # User se stock symbol le
    stock = yf.Ticker(symbol)
    data = stock.history(period="30d")["Close"].values

    # Current Price
    price = data[-1]
    price_label.config(text=f"Current Price: ₹{price:.2f}")

    # AI Prediction
    scaled_data = scaler.fit_transform(np.array(data).reshape(-1, 1))
    prediction = model.predict(scaled_data[-5:].reshape(1, 5, 1))
    predicted_price = prediction[0][0] * scaler.data_range_ + scaler.data_min_

    target_label.config(text=f"Predicted Target: ₹{predicted_price:.2f}")

    # Stop-Loss Calculation
    stop_loss = price - (price * 0.03)  # 3% SL
    sl_label.config(text=f"Suggested Stop-Loss: ₹{stop_loss:.2f}")

# GUI Window
root = tk.Tk()
root.title("AI Trading App")
root.geometry("400x300")

Label(root, text="Enter Stock Symbol:").pack()
entry = tk.Entry(root)
entry.pack()

Button(root, text="Get Price & Prediction", command=get_price).pack()

price_label = Label(root, text="Current Price: ₹0")
price_label.pack()

target_label = Label(root, text="Predicted Target: ₹0")
target_label.pack()

sl_label = Label(root, text="Suggested Stop-Loss: ₹0")
sl_label.pack()

root.mainloop()
