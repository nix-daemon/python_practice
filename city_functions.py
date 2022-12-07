def city_function(city, country, population=''):
    """Generate a neatly formatted city name"""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()
