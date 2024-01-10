import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_weather():
    api_key = "5c89a723ea546ebe72ffc33e168bedca"  
    city = entry_city.get()
    
    if not city:
        messagebox.showinfo("Error", "Please enter a city.")
        return

    
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temperature}°C\nDescription: {description}")
        else:
            messagebox.showinfo("Error", f"Unable to fetch weather data for {city}.")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")

style = ttk.Style()
style.configure('TEntry', padding=(5, 5, 5, 5))
style.configure('TButton', padding=(5, 5, 5, 5))

frame = ttk.Frame(root, padding=10)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_city = ttk.Label(frame, text="Enter City:")
label_city.grid(row=0, column=0, padx=5, pady=5)

entry_city = ttk.Entry(frame)
entry_city.grid(row=0, column=1, padx=5, pady=5)

button_get_weather = ttk.Button(frame, text="Get Weather", command=get_weather)
button_get_weather.grid(row=1, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()
