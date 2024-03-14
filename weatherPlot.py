import pandas as pd
import matplotlib.pyplot as plt

file_path = "Labs\\atlanta_weather.csv"
df = pd.read_csv(file_path)

plt.figure(figsize = (15, 5))

plt.plot(df['Month'], df['High'], 'b--o', label = 'High')
plt.plot(df['Month'], df['Low'], 'g-.^', label = 'Low')

plt.title('Atlanta – Monthly Temperature', fontsize = 20)
plt.xlabel('Month', fontsize = 16)
plt.ylabel('Temperature (Fahrenheit)', fontsize = 16)

max_temp = df['High'].max()
max_temp_month = df.loc[df['High'].idxmax(), 'Month']
plt.annotate('Highest of the year',
            arrowprops=dict(facecolor='red'),
            xy=(max_temp_month, max_temp),
            xytext = (max_temp_month, max_temp - 10))



plt.legend(fontsize = 12)

plt.savefig('atlanta_weather_plot.jpg')

plt.show()
