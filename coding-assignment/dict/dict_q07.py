#Create a dictionary that maps country codes to country names and write a function to retrieve the country name by its code.

country_codes = {'US': 'United States', 'CA': 'Canada', 'MX': 'Mexico'}
def get_country_name(code):
    return country_codes.get(code, 'Unknown Code')
print(get_country_name('CA'))
