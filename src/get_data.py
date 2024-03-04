import os
import sys

from location_client import LocationClient
from weather_client import WeatherClient

# Set parameters
n_locations = 5
date_from = "2018-01-01"
date_to = "2023-12-31"

# Make a directory to store the data
src_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.abspath(os.path.join(src_path, os.pardir))
data_path = os.path.join(project_path, "data")
os.makedirs(data_path, exist_ok=True)

# Get location data and load to data folder
location_client = LocationClient()
location_df, location_ids = location_client.get_random_location_data(
    n_locations=n_locations
)
location_df = location_df.rename(
    columns={"showOnMap": "show_on_map", "locationSources": "location_sources"}
)
location_df.to_csv(os.path.join(data_path, "location_data.csv"), index=False)

# Get weather data for 5 random locations and load to data folder
weather_client = WeatherClient()
weather_df = weather_client.get_weather_data_multiple_locations(
    location_ids, date_from, date_to
)
weather_df = weather_df.rename(
    columns={
        "location_id": "location_id",
        "Time": "time",
        "Cloud_area_fraction": "cloud_area_fraction",
        "Precipitation_amount": "precipitation_amount",
        "Relative_humidity": "relative_humidity",
        "Wind_direction": "wind_direction",
        "Wind_speed": "wind_speed",
        "Temperature": "temperature",
        "Air_pressure": "air_pressure",
        "Weather_icon": "weather_icon",
    }
)
weather_df.to_csv(os.path.join(data_path, "weather_data.csv"), index=False)
