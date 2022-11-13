# h/w: 8-4, 8-5
# H/W: 8-7, 8-8
# H/W: 8-15

print('############ exercise 8-4 ###############')


def make_shirt(size, text_to_print='I love Python'):
    '''
    Print message and size of the shirt
    :return:
    '''
    print(f'The size of your shirt is: {size}.')
    print(f"The message to be printed on your shirt is: \n\t\t'{text_to_print}'")


make_shirt('large')
make_shirt(size='medium')
make_shirt('X-small', 'Python 4ever')
make_shirt(text_to_print='Python 4ever!!!!!!!!', size='XL')

print('############ exercise 8-5 ###############')


def describe_city(city_name, country_name="Italy"):
    '''print a simple sentence and accept city and default country name'''
    print(f'{city_name.title()} is located in {country_name.title()}.')


describe_city('padova')
describe_city(city_name='Venice')
describe_city('berlin', 'germany')

print('############ exercise 8-7 ###############')


def make_album(artist, title):
    return {'Artist Name': artist, 'album Title': title}
    # return 5+6
    # return 234 > 456
    # return album = 45 # this is the assigning action, not good to put in the Return


print("executing the function in the print statement: ", make_album('Adele', 'NY'))
album1 = make_album('Adele', 'NY')
print('printing album1:', album1)


def make_album1(firstname, lastname, title):
    return {'First Name': firstname,
            'Last Name': lastname,
            'album Title': title}


print('Second Album:', make_album('Tupac', 'California'))
print('Third album:', make_album('Justin Beiber', 'Changes'))

print(make_album1('Justin', 'Beiber', 'Changes'))
album2 = make_album1('Justin', 'Beiber', 'Changes')
print(album2['First Name'] + ' ' + album2['Last Name'])


def make_album_tracks(artist, title, tracks=0):
    album = {'Artist Name': artist, 'album Title': title}
    if tracks > 0:
        # add tracks key value pair to dictionary
        album['Num_tracks'] = tracks
    return album

album3 = make_album_tracks('Beyonce', 'Renaissance')
album4 = make_album_tracks('Beyonce', 'Lemonade', 12)

print("album3:", album3)
print("album4:", album4)
# album3.setdefault()

print("--------------------- 8-8 while loop ---------------")
is_next = ''
while is_next != 'n':
    artist = input("Enter the artist name: ")
    alb = input("Enter the album name: ")
    trck = input("Enter the track numbers: ")
    trck = int(trck)
    album3 = make_album_tracks(artist, alb, trck)

    print("album3:", album3)
    is_next = input("do you want to continue? y/n: ")

print("--------------------- 8-8 while loop completed---------------")

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
        Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


# H/W: Problem-solving (amazon):
# write a functions that return letters with counts, i.e. how many times each letter is used in the string (word, sentence, bigger text ..)
# Sample Input and Output: 'hello' -> {'h':1, 'e':1, 'l':2, 'o':1}
# album['letter'] += tracks  # adding the value to a previous value of the key in the dictionary
# album['letter'] = album['letter'] + tracks

