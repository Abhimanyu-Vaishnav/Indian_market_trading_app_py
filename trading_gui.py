import tkinter as tk
from tkinter import ttk
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Function to fetch stock historical data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="6mo")  # 6 months data
    df["Returns"] = df["Close"].pct_change()  # Calculate daily returns
    return df.dropna()

# Function to predict SL & Target based on past trends
def predict_sl_target(symbol):
    df = get_stock_data(symbol)

    # Creating independent (X) and dependent variable (y)
    df["Day"] = np.arange(len(df))
    X = df[["Day"]]
    y = df["Close"]

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next day's price
    predicted_price = model.predict([[len(df) + 1]])[0]

    # Calculate Suggested SL & Target
    target_price = predicted_price * 1.05  # +5% gain
    stop_loss = predicted_price * 0.95  # -5% loss

    return round(stop_loss, 2), round(target_price, 2), round(predicted_price, 2)

# Function to update GUI with AI predictions
def update_price():
    symbol = stock_var.get()
    live_data = yf.Ticker(symbol).history(period="1d")
    live_price = round(live_data["Close"].iloc[-1], 2)

    # Predict SL & Target
    sl, target, predicted_price = predict_sl_target(symbol)

    price_label.config(text=f"Live Price: ₹{live_price}")
    sl_var.set(sl)
    target_var.set(target)
    ai_pred_label.config(text=f"AI Predicted Price: ₹{predicted_price}")

# GUI Setup
root = tk.Tk()
root.title("AI Trading App")
root.geometry("400x350")

# Load stock symbols
df = pd.read_csv("nse_stocks.csv")
stock_symbols = df["Symbol"].tolist()

stock_var = tk.StringVar()
stock_dropdown = ttk.Combobox(root, textvariable=stock_var, values=stock_symbols)
stock_dropdown.pack(pady=10)
stock_dropdown.set("Select Stock")

# Labels
price_label = tk.Label(root, text="Live Price: ₹0.00", font=("Arial", 12))
price_label.pack(pady=5)

ai_pred_label = tk.Label(root, text="AI Predicted Price: ₹0.00", font=("Arial", 12))
ai_pred_label.pack(pady=5)

# SL & Target Fields
sl_var = tk.StringVar()
target_var = tk.StringVar()

tk.Label(root, text="🔻 Suggested Stop-Loss:").pack()
sl_entry = tk.Entry(root, textvariable=sl_var)
sl_entry.pack()

tk.Label(root, text="🎯 Suggested Target Price:").pack()
target_entry = tk.Entry(root, textvariable=target_var)
target_entry.pack()

# Fetch Button
fetch_btn = tk.Button(root, text="Get AI Prediction", command=update_price)
fetch_btn.pack(pady=10)

root.mainloop()
