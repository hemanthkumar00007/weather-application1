import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "5c9925096b15bb7d0e19c43a6845745e"  # Replace with your actual API key

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
        else:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            result_label.config(text=f"{city.title()}\n{weather}\nTemperature: {temp}°C\nHumidity: {humidity}%")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("300x250")

tk.Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(app, font=("Arial", 12), justify="center")
result_label.pack(pady=20)

app.mainloop()
