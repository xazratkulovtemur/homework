import requests


API_KEY="1111130df60433193532d2f5a658ad4f"
CITY="Tashkent"
URL=f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response=requests.get(URL)
print(response.json())
if response.status_code==200: 
    data=response.json()
    temprature=data['main']['temp']
    humidity=data['main']['humidity']
    sea_level=data["main"]["sea_level"]

    print(f"Temprature in Tashkent: {temprature}°C")
    print(f"Humidity in Tashkent: {humidity}%")
    print(f"Sea level in Tashkent: {sea_level}m/s")
else:
    print("Error: Check API key or City name!")