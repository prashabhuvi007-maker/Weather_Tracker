import requests
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = "9d4f6aa5c996882561ee8bd18decd3e5"  # Replace with your key
cities = ["Bengaluru", "Mumbai", "Delhi"]

all_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") == 200:
        data = {
            "city": city,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "temperature": response['main']['temp'],
            "humidity": response['main']['humidity'],
            "description": response['weather'][0]['description']
        }
        all_data.append(data)
        print(f"Fetched data for {city}: {data}")
    else:
        print(f"Error fetching data for {city}: {response.get('message')}")

if all_data:
    df = pd.DataFrame(all_data)
    conn = sqlite3.connect("weather.db")
    df.to_sql("weather_data", conn, if_exists="append", index=False)
    conn.close()
    print("\nData saved to database successfully!")
else:
    print("No valid data to save.")

conn = sqlite3.connect("weather.db")
for city in cities:
    df_city = pd.read_sql(f"SELECT * FROM weather_data WHERE city='{city}'", conn)
    if not df_city.empty:
        plt.plot(df_city['date'], df_city['temperature'], marker='o', label=city)
conn.close()

plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()