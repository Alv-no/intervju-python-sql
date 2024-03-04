import requests
import pandas as pd


class LocationClient(object):
    def __init__(self) -> None:
        self.base_url = "https://api.uvar.no/location/v1/locations/"

    def get_all_location_data(self) -> pd.DataFrame | None:
        """Get data from all locations."""

        try:
            response = requests.get(self.base_url).json()
            response_df = pd.DataFrame(response)
            n_locations = len(response_df)
            print(f"Data from {n_locations} locations fetched.")

            location_ids = response_df["id"].values

        except requests.exceptions.RequestException as e:
            print(e)
            return None

        return response_df, location_ids

    def get_random_location_data(self, n_locations: int):
        """Get data from n random locations."""

        try:
            location_data, _ = self.get_all_location_data()
            location_ids = location_data.sample(n_locations)["id"].values
            location_df = location_data[location_data["id"].isin(location_ids)]
            print(f"{n_locations} random location(s) picked.")

        except IndexError as e:
            print(e)
            return None

        return location_df, location_ids

    def get_name_from_id(self, location_df: pd.DataFrame, location_id: str) -> str:
        """Get name from location_id."""

        try:
            name = location_df[location_df["id"] == location_id]["name"].values[0]
            print(f"Name {name} fetched for location_id: {location_id}")
        except IndexError as e:
            print(e)
            return None

        return name
