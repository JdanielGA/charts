import csv

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