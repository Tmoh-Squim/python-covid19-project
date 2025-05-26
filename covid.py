import requests
import json

def get_global_covid_data():
    """Fetches global COVID-19 data from the disease.sh API."""
    api_url = "https://disease.sh/v3/covid-19/all"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching global data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding global JSON: {e}")
        return None

def display_global_data(data):
    """Displays the global COVID-19 data in the terminal."""
    if data:
        print("\n--- Global COVID-19 Statistics ---")
        print(f"Total Cases: {data['cases']:,}")
        print(f"Total Deaths: {data['deaths']:,}")
        print(f"Total Recovered: {data['recovered']:,}")
        print(f"Active Cases: {data['active']:,}")
        print(f"Critical Cases: {data['critical']:,}")
        print(f"Tests Conducted: {data['tests']:,}")
        print(f"Updated: {data['updated']}")
    else:
        print("Failed to retrieve global COVID-19 data.")

def get_country_covid_data(country):
    """Fetches COVID-19 data for a specific country from the disease.sh API."""
    api_url = f"https://disease.sh/v3/covid-19/countries/{country}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {country}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for {country}: {e}")
        return None

def display_country_data(data, country):
    """Displays the COVID-19 data for a specific country in the terminal."""
    if data:
        print(f"\n--- COVID-19 Statistics for {country.capitalize()} ---")
        print(f"Total Cases: {data['cases']:,}")
        print(f"Total Deaths: {data['deaths']:,}")
        print(f"Total Recovered: {data['recovered']:,}")
        print(f"Active Cases: {data['active']:,}")
        print(f"Critical Cases: {data['critical']:,}")
        print(f"Tests Conducted: {data['tests']:,}")
        print(f"Updated: {data['updated']}")
    else:
        print(f"Failed to retrieve COVID-19 data for {country}.")

if __name__ == "__main__":
    while True:
        print("\n--- COVID-19 Data Tracker ---")
        print("1. Get Global Statistics")
        print("2. Get Statistics by Country")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            global_data = get_global_covid_data()
            display_global_data(global_data)
        elif choice == '2':
            country_name = input("Enter the name of the country (e.g., USA, Kenya, Brazil): ").lower()
            country_data = get_country_covid_data(country_name)
            display_country_data(country_data, country_name.capitalize())
        elif choice == '3':
            print("Exiting the tracker. Stay safe!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")