import requests
from PIL import Image
from io import BytesIO

api_key = " YOUR API_KEY"


def get_current_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_forecast(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast?"
        f"q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_weather_icon(icon_code):

    icon_url = (
        f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    )

    response = requests.get(icon_url)

    image = Image.open(BytesIO(response.content))

    return image


def celsius_to_fahrenheit(temp):

    return (temp * 9 / 5) + 32


def format_hourly_forecast(forecast_data):

    hourly = ""

    for item in forecast_data["list"][:6]:

        time = item["dt_txt"][11:16]

        temp = item["main"]["temp"]

        weather = item["weather"][0]["main"]

        hourly += (
            f"{time:<8}"
            f"{temp:.1f}°C"
            f"    {weather}\n"
        )

    return hourly


def format_daily_forecast(forecast_data):

    daily = ""

    dates = []

    for item in forecast_data["list"]:

        date = item["dt_txt"][:10]

        if date not in dates:

            dates.append(date)

            temp = item["main"]["temp"]

            weather = item["weather"][0]["main"]

            daily += (
                f"{date}\n"
                f"{temp:.1f}°C"
                f"   {weather}\n\n"
            )

        if len(dates) == 5:
            break

    return daily