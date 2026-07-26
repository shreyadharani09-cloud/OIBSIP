import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import weather_app

root = tk.Tk()
root.title("Weather Application")
root.geometry("650x550")
root.resizable(False, False)
current_temperature = None

def get_weather():

    global current_temperature

    city = city_entry.get()

    if city == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter city name"
        )
        return


    weather = weather_app.get_current_weather(city)
    forecast = weather_app.get_forecast(city)


    if weather is None:
        messagebox.showerror(
            "Error",
            "City not found"
        )
        return


    city_name = weather["name"]

    current_temperature = weather["main"]["temp"]

    humidity = weather["main"]["humidity"]

    condition = weather["weather"][0]["description"]

    wind = weather["wind"]["speed"]

    icon_code = weather["weather"][0]["icon"]



    city_value.config(
        text=f"City : {city_name}"
    )


    details_label.config(
        text=f"""
Temperature : {current_temperature} °C
Humidity    : {humidity} %
Weather     : {condition}
Wind Speed  : {wind} m/s
"""
    )

    image = weather_app.get_weather_icon(icon_code)

    image = image.resize((70,70))

    photo = ImageTk.PhotoImage(image)

    icon_label.config(image=photo)
    icon_label.image = photo





    five_day_label.config(text=weather_app.format_daily_forecast(forecast))


    hourly_label.config(text=weather_app.format_hourly_forecast(forecast))


def convert_temperature():

    global current_temperature

    if current_temperature is None:
        return


    fahrenheit = weather_app.celsius_to_fahrenheit(
        current_temperature
    )


    details_label.config(
        text=details_label.cget("text")
        .replace(
            f"{current_temperature} °C",
            f"{fahrenheit:.1f} °F"
        )
    )


title = tk.Label(root,text="WEATHER APPLICATION",font=("Arial",18,"bold"))
title.grid(row=0,column=0,columnspan=2,pady=(8,5))

search_frame = tk.Frame(root)
search_frame.grid(row=1,column=0,columnspan=2,pady=(0,8))

city_label = tk.Label(search_frame,text="City :",font=("Arial",12))
city_label.grid(row=0,column=0,padx=5)

city_entry = tk.Entry(search_frame,width=30,font=("Arial",12))
city_entry.grid(row=0,column=1,padx=5)

get_button = tk.Button(search_frame,text="Get Weather",font=("Arial",11),command=get_weather)
get_button.grid(row=0,column=2,padx=(10,0))

weather_frame = tk.Frame(root)
weather_frame.grid(row=2,column=0,columnspan=2,pady=(5,0))

details_frame = tk.Frame(weather_frame)
details_frame.grid(row=0,column=0,padx=10)

city_value = tk.Label(details_frame,text="City :",font=("Arial",12,"bold"),anchor="w")
city_value.pack(anchor="w",pady=(0,2))

details_label = tk.Label(details_frame,text="",font=("Arial",12),justify="left")
details_label.pack(anchor="w",pady=0)

icon_label = tk.Label(weather_frame)
icon_label.grid(row=0,column=1,padx=(10,0),sticky="n")

convert_button = tk.Button(root,text="Switch to °F",command=convert_temperature)
convert_button.grid(row=3,column=0,columnspan=2,pady=(5,10))

forecast_frame = tk.Frame(root)
forecast_frame.grid(row=4,column=0,columnspan=2,pady=(5,0))

day_frame = tk.Frame(forecast_frame)
day_frame.grid(row=0, column=0, padx=30)
day_title = tk.Label(day_frame,text="5 Days Forecast",font=("Arial",13,"bold"))
day_title.pack()

five_day_label = tk.Label(day_frame,text="",font=("Courier",10),justify="left")
five_day_label.pack()

hour_frame = tk.Frame(forecast_frame)
hour_frame.grid(row=0, column=1, padx=30)
hour_title = tk.Label(hour_frame,text="Hourly Forecast",font=("Arial",13,"bold"))
hour_title.pack()

hourly_label = tk.Label(hour_frame,text="",font=("Courier",10),justify="left")
hourly_label.pack()

root.mainloop()