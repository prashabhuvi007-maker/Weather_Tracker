import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("Weather Tracker Dashboard")

# Connect to the database
conn = sqlite3.connect("weather.db")
df = pd.read_sql("SELECT * FROM weather_data ORDER BY date DESC", conn)
conn.close()

# Show latest data
st.subheader("Latest Weather Data")
st.dataframe(df.head(10))

# Plot temperature trends
st.subheader("Temperature Trend")
for city in df['city'].unique():
    city_data = df[df['city'] == city]
    plt.plot(pd.to_datetime(city_data['date']), city_data['temperature'], label=city)

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
st.pyplot(plt)