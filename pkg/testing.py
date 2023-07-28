import csv
import matplotlib.pyplot as plt

def read_csv(path):
    
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)                           #reading only the header in the file
        data = []

        for row  in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)

        return data
    
def get_percentage(data):

    user_choice = input('sellect the region: ')
    new_list = list(filter(lambda region: region['Continent'] == user_choice, data))
    percentage_countries = {data['Country/Territory']: float(data['World Population Percentage']) for data in new_list }
    return percentage_countries

def generate_bar_chart(data_got):

    labes = list(data_got.keys())
    values = list(data_got.values())

    fig, ax = plt.subplots()
    ax.bar(labes, values)
    plt.show()

def generate_pie_chart(data_got):

    labes = list(data_got.keys())
    values = list(data_got.values())

    fig, ax = plt.subplots()
    ax.pie(values, labels=labes)
    ax.axis('equal')
    plt.show()
    

data = read_csv('./Documents/world_population.csv')
percentage = get_percentage(data)
generate_pie_chart(percentage)