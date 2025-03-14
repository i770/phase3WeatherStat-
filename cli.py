from models import add_location, get_all_locations, delete_location, add_weather_record, get_all_weather_records, delete_weather_record
from tabulate import tabulate

def main_menu():
    while True:
        print("\nWeatherStat CLI - Weather Statistics Tracker")
        print("1. Add Location")
        print("2. View All Locations")
        print("3. Delete Location")
        print("4. Add Weather Record")
        print("5. View All Weather Records")
        print("6. Delete Weather Record")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city: ")
            country = input("Enter country: ")
            add_location(city, country)
            print(f"Location '{city}, {country}' added successfully!")

        elif choice == "2":
            locations = get_all_locations()
            print(tabulate([[l.id, l.city, l.country] for l in locations], headers=["ID", "City", "Country"]))

        elif choice == "3":
            location_id = int(input("Enter location ID to delete: "))
            if delete_location(location_id):
                print("Location deleted successfully!")
            else:
                print("Location not found!")

        elif choice == "4":
            location_id = int(input("Enter location ID: "))
            temperature = float(input("Enter temperature: "))
            humidity = float(input("Enter humidity: "))
            wind_speed = float(input("Enter wind speed: "))
            add_weather_record(location_id, temperature, humidity, wind_speed)
            print("Weather record added successfully!")

        elif choice == "5":
            records = get_all_weather_records()
            print(tabulate([[r.id, r.location_id, r.temperature, r.humidity, r.wind_speed, r.date] for r in records], 
                           headers=["ID", "Location ID", "Temp (°C)", "Humidity (%)", "Wind Speed (km/h)", "Date"]))

        elif choice == "6":
            record_id = int(input("Enter weather record ID to delete: "))
            if delete_weather_record(record_id):
                print("Weather record deleted successfully!")
            else:
                print("Record not found!")

        elif choice == "7":
            print("Exiting WeatherStat CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
