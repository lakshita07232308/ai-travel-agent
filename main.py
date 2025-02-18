import streamlit as st
import requests

# Function to get the current temperature of the city
def get_temperature(city):
    api_key = "7824f30d1fb4d6fce5ce1da63555e23a"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['main']['temp']
        else:
            st.error(f"Error fetching weather data: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error during weather data fetch: {e}")
        return None

# Function to provide clothing recommendation based on temperature
def get_clothing_recommendation(temperature):
    if temperature is None:
        return "No temperature data available."
    if temperature < 0:
        return "Wear a heavy winter coat, gloves, and scarf."
    elif 0 <= temperature < 10:
        return "Wear a jacket and warm clothes."
    elif 10 <= temperature < 20:
        return "Wear a sweater or light jacket."
    else:
        return "Wear light clothes (t-shirt, shorts)."

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/a1b646ed60002f2c5d3d9a92/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            conversion_rate = data['conversion_rates'].get(to_currency)
            if conversion_rate:
                return amount * conversion_rate
            else:
                st.error(f"Conversion rate for {to_currency} not found.")
        else:
            st.error(f"Failed to retrieve data. Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"Error during conversion: {e}")
    
    return None

# Streamlit App
def main():
    st.title("AI Travel Agent")
    
    # Temperature Section
    st.header("Weather and Clothing Recommendation")
    city = st.text_input("Enter the city name:")
    
    if city:
        temperature = get_temperature(city)
        if temperature is not None:
            st.success(f"The current temperature in {city} is {temperature}°C.")
            recommendation = get_clothing_recommendation(temperature)
            st.info(f"Clothing Recommendation: {recommendation}")
    
    # Currency Conversion Section
    st.header("Currency Converter")
    amount = st.number_input("Enter the amount of money you want to convert:", min_value=0.0, step=0.01)
    from_currency = st.text_input("From Currency (e.g., USD):").upper()
    to_currency = st.text_input("To Currency (e.g., EUR):").upper()
    
    if st.button("Convert Currency"):
        if amount and from_currency and to_currency:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                st.success(f"The converted amount is {converted_amount:.2f} {to_currency}.")
            else:
                st.error("Currency conversion failed.")

if __name__ == "__main__":
    main()
