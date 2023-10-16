import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/get_temperature/{city}")
def get_temperature(city: str):
    api_key = "a4f99c1929b95644f2a2b342b0e2b84d"  # Replace with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Create the API request URL
    complete_url = f"{base_url}q={city}&appid={api_key}"

    # Send the request and get the response
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200:
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        return {"temperature": temperature_celsius}
    else:
        return {"error": "City not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
