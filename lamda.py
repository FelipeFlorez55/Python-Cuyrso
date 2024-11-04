import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        country = []
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            dict_row = dict(zip(header, row))
            country.append(dict_row)
        return country
def populationtcountry(path,country):
    population=[1970,1980,1990,2000,2010,2015,2020,2022]
    countrys = read_csv(path)
    for i in countrys:
        if i['Country'] == country:
            data ={k: v for k, v in i.items() if k != 'Country' and 'Population' in k and k != 'World Population Percentage'}
            p={k:v for k,v in zip(population,data.values())}
            return p
            break
print(populationtcountry('data.csv','Australia'))