import os

def get_population(data):

    country = input('Select the country to consult: ')
    country_data = [i for i in data if i['Country/Territory'] == country]
    data_got = {key: int(value) for key, value in country_data[0].items() if 'Population' in key and 'Percentage' not in key}
    return data_got

def get_percentage(data):

    user_choice = input('sellect the region: ')
    new_list = list(filter(lambda region: region['Continent'] == user_choice, data))
    percentage_countries = {data['Country/Territory']: float(data['World Population Percentage']) for data in new_list }
    return percentage_countries

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

