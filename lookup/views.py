import json
from django.shortcuts import render
import requests


def home(request):
    # Check if the request method is POST (when user submits the form)
    if request.method == "POST":
        # Capture the zip code entered by the user
        zipcode = request.POST["zipcode"]
        
        # Make an API request to fetch air quality data (using a hardcoded zip code for now)
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" +zipcode +"&distance=25&API_KEY=C58D426A-7DE1-413A-9875-74EF0473708A"
        )

        try:
            # Try to parse the JSON response from the API
            api = json.loads(api_request.content)
        except Exception as e:
            # In case of error, set the API variable to an error message
            api = "Error......"

        # Check if the API response is valid and if data is available
        if api and isinstance(api, list) and len(api) > 0 and 'Category' in api[0]:
            # Process the air quality category data and assign descriptions and colors based on the category
            category_name = api[0]['Category']['Name']
            if category_name == "Good":
                category_description = "(0-50) Satisfactory"
                category_color = "good"
            elif category_name == "Moderate":
                category_description = "(51-100) Acceptable"
                category_color = "moderate"
            elif category_name == "USG":
                category_description = "(101-150) Maybe Affected"
                category_color = "usg"
            elif category_name == "Unhealthy":
                category_description = "(151-200) Health Effect"
                category_color = "unhealthy"
            elif category_name == "Very Unhealthy":
                category_description = "(201-300) Health Alert"
                category_color = "very-unhealthy"
            elif category_name == "Hazardous":
                category_description = "(301-500) Health Warning"
                category_color = "hazardous"
        else:
            # If no valid data is available, set default values
            category_description = "No data available"
            category_color = "no-data"

        # Create context dictionary with all necessary variables to pass to the template
        context = {
            'api': api,
            'category_description': category_description,
            'category_color': category_color,
        }

        # Return the rendered response, passing the context dictionary to the template
        return render(request, 'home.html', context)

    # If the method is GET or some other method, render the page with an empty context
    return render(request, 'home.html')


def about(request):
    # if request.method == "POST":
    #     # Capture the zip code entered by the user
    #     zipcode = request.POST["zipcode"]
        
    #     # Make an API request to fetch air quality data (using a hardcoded zip code for now)
    #     api_request = requests.get(
    #         "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" +zipcode +"&distance=25&API_KEY=C58D426A-7DE1-413A-9875-74EF0473708A"
    #     )

    #     try:
    #         # Try to parse the JSON response from the API
    #         api = json.loads(api_request.content)
    #     except Exception as e:
    #         # In case of error, set the API variable to an error message
    #         api = "Error......"

    #     # Check if the API response is valid and if data is available
    #     if api and isinstance(api, list) and len(api) > 0 and 'Category' in api[0]:
    #         # Process the air quality category data and assign descriptions and colors based on the category
    #         category_name = api[0]['Category']['Name']
    #         if category_name == "Good":
    #             category_description = "(0-50) Satisfactory"
    #             category_color = "good"
    #         elif category_name == "Moderate":
    #             category_description = "(51-100) Acceptable"
    #             category_color = "moderate"
    #         elif category_name == "USG":
    #             category_description = "(101-150) Maybe Affected"
    #             category_color = "usg"
    #         elif category_name == "Unhealthy":
    #             category_description = "(151-200) Health Effect"
    #             category_color = "unhealthy"
    #         elif category_name == "Very Unhealthy":
    #             category_description = "(201-300) Health Alert"
    #             category_color = "very-unhealthy"
    #         elif category_name == "Hazardous":
    #             category_description = "(301-500) Health Warning"
    #             category_color = "hazardous"
    #     else:
    #         # If no valid data is available, set default values
    #         category_description = "No data available"
    #         category_color = "no-data"

    #     # Create context dictionary with all necessary variables to pass to the template
    #     context = {
    #         'api': api,
    #         'category_description': category_description,
    #         'category_color': category_color,
    #     }

    #     # Return the rendered response, passing the context dictionary to the template
    #     return render(request, 'about.html', context)

    # # If the method is GET or some other method, render the page with an empty context
    
    return render(request,'about.html')