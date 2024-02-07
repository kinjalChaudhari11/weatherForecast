import requests
##using OpenWeatherMap, and the Current Weather Forcast (free)
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"Weather in {city}: {weather}, Temperature: {temp}°C"
    else: 
        return "Error: Unable to fetch weather data"
    
def main(): 
    api_key = "YOUR_API_KEY"  ##I have to keep my key private, but you can go to Open Weather Map and get one for free!
    city = input("Enter a city name: ")
    weather_info = get_weather(api_key, city)
    print(weather_info)

if __name__ == "__main__":
    main()
