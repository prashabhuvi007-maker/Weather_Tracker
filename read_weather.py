import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("weather.db")

# Read all data, ordered by date (latest first)
df = pd.read_sql("SELECT * FROM weather_data ORDER BY date DESC", conn)

# Display the latest entries (you can change the number)
print("Latest weather data:")
print(df.head())  # Shows top 5 latest entries

# Close the database connection
conn.close()