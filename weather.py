import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        description = weather["description"]
        print(f"Temperature: {temp}")
        print(f"Weather description: {description}")
    else:
        print("City not found.")

city = input("Enter city name: ")
get_weather(city)
