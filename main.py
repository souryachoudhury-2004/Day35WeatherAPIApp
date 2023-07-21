import requests

# 57323afa7038c3ecb0971e935c57463f

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q=Kolkata&appid=b36dd96769ef0caf0a322d5d5f66f443")

response.raise_for_status()

weather_data = response.json()

main_data = response.json()["main"]
temperature = main_data["temp"]-273.15
print(f"Temperature: {round(temperature, 2)} C")
