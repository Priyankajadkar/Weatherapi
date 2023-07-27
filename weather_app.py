import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temperature_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'] == date:
            return item['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("\nMenu:")
        print("1. Get weather temperature for a date")
        print("2. Get wind speed for a date")
        print("3. Get pressure for a date")
        print("0. Exit")

        choice = input("Enter your choice (0/1/2/3): ")

        if choice == '1':
            date = input("Enter the date (e.g., 2023-07-25 12:00:00): ")
            temperature = get_temperature_by_date(data, date)
            if temperature is not None:
                print(f"Temperature at {date}: {temperature}°C")
            else:
                print("Data not available for the given date.")

        elif choice == '2':
            date = input("Enter the date (e.g., 2023-07-25 12:00:00): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed at {date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date.")

        elif choice == '3':
            date = input("Enter the date (e.g., 2023-07-25 12:00:00): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure at {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
