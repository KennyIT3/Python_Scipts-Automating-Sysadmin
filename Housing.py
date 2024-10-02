import requests

def track_housing_affordability(state):
    base_url = 'https://hud.opendata.arcgis.com/datasets/8e3c7a1d984b47d5bbaa4d0ce8622d8f_0.geojson'
    response = requests.get(base_url)
    data = response.json()
    
    if 'features' in data:
        state_data = [feature['properties'] for feature in data['features'] if feature['properties']['STATE'] == state]

        if state_data:
            for entry in state_data:
                city = entry['CITY']
                median_income = entry['MEDIAN_INCOME']
                median_home_value = entry['MEDIAN_HOME_VALUE']
                print(f"City: {city}, Median Income: {median_income}, Median Home Value: {median_home_value}")
        else:
            print(f"No housing affordability data available for {state}")
    else:
        print("Error: Data format not as expected. Please check the API response.")

track_housing_affordability('NC')