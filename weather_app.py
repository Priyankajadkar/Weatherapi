import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"  # Replace with the correct API URL

def get_weather_data(date):
    url = f"{API_BASE_URL}?date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_weather_temperature():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_weather_data(date)
    if weather_data:
        print(weather_data)  # Print the entire API response to inspect the data

        # Print all keys in the response
        print("Available keys:", weather_data.keys())

        # Find the correct key for temperature and update the print statement accordingly
        # For example, if the key for temperature is 'main'['temp'], modify the line below:
        # print(f"Temperature on {date}: {weather_data['main']['temp']} °C")

def get_wind_speed():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_weather_data(date)
    if weather_data:
        print(f"Wind Speed on {date}: {weather_data['wind']['speed']} m/s")

def get_pressure():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_weather_data(date)
    if weather_data:
        print(f"Pressure on {date}: {weather_data['pressure']} hPa")

def main():
    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_weather_temperature()
        elif choice == "2":
            get_wind_speed()
        elif choice == "3":
            get_pressure()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
