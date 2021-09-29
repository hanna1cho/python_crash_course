def city_country (city, country):
    location = f"{city}, {country}"
    return location.upper()


favorite = city_country('new york', 'usa')
home = city_country('seoul', 'south korea')
travel = city_country('kyoto', 'japan')
print(favorite)
print(home)
print(travel)

print("\n")

def make_album (artist, album_title, soungcount=None):    
    album = {'Artist' : artist, 'Album Title' : album_title.title()}

    if soungcount:
        album['# of Songs'] = soungcount

    return album

kpop = make_album('IU', 'pink dream', 11)
america = make_album('Katy Perry', 'hot n cold')
jazz = make_album('michael buble', 'merry christmas')

print(kpop)
print(america)
print(jazz)


while True:
    print("\nPlease provide album information or enter 'q' to quit.")

    artist_name = input("Who is the artist? ")
    
    if artist_name == 'q':
        break

    album_name = input("What is the ablum called? ")
    album_length = input("How many songs? ")

    album_info = make_album(artist_name, album_name, album_length)

    print(album_info)