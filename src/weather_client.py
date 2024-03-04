import requests
import pandas as pd


class WeatherClient(object):
    def __init__(self) -> None:
        self.base_url = "http://api.uvar.no/processor/location_weather_range"

    def get_weather_data_one_location(
        self, location_id: str, date_from: int, date_to: int
    ) -> pd.DataFrame | None:
        """Get weather data from one location."""

        if not isinstance(location_id, str):
            print(f"location_id must be a string. Got {type(location_id)}")
            raise

        try:
            response = requests.get(
                f"{self.base_url}?locationId={location_id}&from={date_from}%2000:00:00&to={date_to}%2001:00:00"
            ).json()
            weather_df = pd.DataFrame(response)
            weather_df.insert(0, "location_id", location_id)
            print(f"Fetch weather data for location_id: {location_id}")
        except requests.exceptions.RequestException as e:
            print(e)

            return None

        return weather_df

    def get_weather_data_multiple_locations(
        self, location_ids: list[str], date_from: int, date_to: int
    ) -> pd.DataFrame:
        """Get weather data from multiple locations."""

        weather_df = pd.DataFrame()
        for location_id in location_ids:
            data = self.get_weather_data_one_location(location_id, date_from, date_to)

            if data is not None:
                weather_df = pd.concat([weather_df, data])

        return weather_df
