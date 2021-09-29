favorite_places = {
    "Michael" : ['Seoul', 'Taipei', 'London'],
    "Hannah" : ['Paris', 'Shangahi'],
    'Christine' : ['Frankfurt'],
    'Chuck' : ['Tokyo', 'Osaka'],
    'Marry' : ['Dallas' , 'Sydney']
}

for person, cities in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for city in cities:
        print(f"\t{city}")

print("\n") 

#replace values in dict

favorite_places['Hannah'][1] = 'New York'
print(favorite_places)



favorite_cities = {
    "Michael" : {
        'City': 'Seoul',
        'Country': 'South Korea',
        'Continent' : 'Asia'
        },
    "Jane" : {
        'City': 'Tokyo',
        'Country': 'Japan',
        'Continent' : 'Asia'
        },
    'Christine' : {
        'City': 'London',
        'Country': 'United Kingdom',
        'Continent' : 'Europe'
        }
    }

for person, info in favorite_cities.items():
    print (f"\nHere is the information about {person}'s favorite city:")
    city = f"{info['City']}, {info['Country']}"
    print(f"\t{city}")

