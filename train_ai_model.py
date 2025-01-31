import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Reliance Stock Data Fetch
symbol = "RELIANCE.NS"
stock = yf.Ticker(symbol)
data = stock.history(period="1y")["Close"].values

# Data Normalization
scaler = MinMaxScaler()
data = scaler.fit_transform(data.reshape(-1, 1))

# Data Preparation for LSTM
X, y = [], []
for i in range(5, len(data)):
    X.append(data[i-5:i])
    y.append(data[i])

X, y = np.array(X), np.array(y)

# LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(5, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, y, epochs=50, batch_size=16)

# Save Model
model.save("ai_trading_model.h5")
print("Model Training Done!")
