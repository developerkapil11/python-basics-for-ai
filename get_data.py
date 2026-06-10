import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate Dates
today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

def getCurrentWeather(lat,long,start_date,end_date):

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={long}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
    )

    res = requests.get(url)
    data = res.json();
    return data['daily']

daily_data = getCurrentWeather(30.392655,76.870003,start_date, end_date)

#--------------------Pandas----------------------------
# Create DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date String to dateTime
df['date'] = pd.to_datetime(df['date'])

print(df)

#--------------------Matplotlib-------------------------
#visualize the data (create simple line chart)

# Create the Plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and Title
plt.xlabel('Date')
plt.ylabel('Temprature (°C)')
plt.title('Haryana Weather - Past 7 Days')
plt.legend()

# Rotate X-axis Label for Readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot 
plt.savefig('weather_chart.png')
#plt.show()

#----------------------OS-----------------------------

if not os.path.exists('data'):
    os.makedirs('data')

# Save the CSV file in new directory data

df.to_csv('data/haryana_weather_report_last7Days.csv', index=False)
print('Data Saved Successfully')