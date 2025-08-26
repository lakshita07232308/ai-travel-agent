# AI Travel Agent 

A simple web application built with Streamlit that acts as a helpful travel agent. It provides real-time weather information with clothing recommendations and includes a currency converter to assist with your travel planning.

## Features

* **Real-time Weather:** Enter any city name to get the current temperature in Celsius.
* **Clothing Recommendations:** Receive practical advice on what to wear based on the local temperature.
* **Currency Converter:** Convert amounts between different currencies using up-to-date exchange rates.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.7+
* An API key from [OpenWeatherMap](https://openweathermap.org/api)
* An API key from [ExchangeRate-API](https://www.exchangerate-api.com/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/ai-travel-agent.git](https://github.com/your-username/ai-travel-agent.git)
    cd ai-travel-agent
    ```

2.  **Create a `requirements.txt` file** with the following content:
    ```
    streamlit
    requests
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    Open the Python script and replace the placeholder API keys with your own.

    * Find this line for the weather feature and insert your key:
        ```python
        api_key = "7824f30d1fb4d6fce5ce1da63555e23a"  # Replace with your OpenWeatherMap API key
        ```

    * Find this line for the currency feature and insert your key:
        ```python
        url = f"[https://v6.exchangerate-api.com/v6/a1b646ed60002f2c5d3d9a92/latest/](https://v6.exchangerate-api.com/v6/a1b646ed60002f2c5d3d9a92/latest/){from_currency}" # Replace with your ExchangeRate-API key
        ```

---

##  Usage

1.  **Run the Streamlit application** from your terminal:
    ```sh
    streamlit run your_script_name.py
    ```

2.  **Open your web browser** and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

3.  **Use the App:**
    * **For Weather:** Enter a city name in the first text box to see the current temperature and a clothing recommendation.
    * **For Currency:** Enter the amount, source currency (e.g., USD), and target currency (e.g., INR), then click the "Convert Currency" button.

## Technologies Used

* **Python**: Core programming language.
* **Streamlit**: For creating the interactive web application.
* **Requests**: For making HTTP requests to external APIs.
* **OpenWeatherMap API**: To fetch real-time weather data.
* **ExchangeRate-API**: To fetch currency conversion rates.
