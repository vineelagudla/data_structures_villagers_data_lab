"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    
    data = open(filename)
    for line in data:
        villagers_species = line.split("|")
        species_list = line.split("|")
        villagers_species = species_list[1]
        species.add(villagers_species)
        

    #TODO: replace this with your code
    #print(species_list)
    return species
all_species("villagers.csv")



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    data = open(filename)
    
    for line in data:
        list_of_data = line.rstrip().split("|")
        villagers_name = list_of_data[0]
        species_name = list_of_data[1]
                
        if search_string in ("All", species_name):
            villagers.append(villagers_name)
        

    # TODO: replace this with your code
    #print(sorted(villagers))
    return sorted(villagers)
get_villagers_by_species("villagers.csv", search_string="All")



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    data = open(filename)

    for line in data:

        list_of_data = line.rstrip().split("|")
        villagers_name = list_of_data[0]
        hobby = list_of_data[3]

        if hobby == "Fitness":
            fitness.append(villagers_name)
        
        elif hobby == "Nature":
            nature.append(villagers_name)
        
        elif hobby == "Education":
            education.append(villagers_name)

        elif hobby == "Music":
            music.append(villagers_name)

        elif hobby == "Fashion":
            fashion.append(villagers_name)

        elif hobby == "Play":
            play.append(villagers_name)
            
    # TODO: replace this with your code
    # print([sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)])
    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]
all_names_by_hobby("villagers.csv")



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data = open(filename)

    for line in data:
        list_of_data = line.rstrip().split("|")
        tup = tuple(list_of_data)
        all_data.append(tup)

    # TODO: replace this with your code

    return all_data
all_data("villagers.csv")



def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        list_of_data = line.rstrip().split("|")
        name = list_of_data[0]
        villagers_motto = list_of_data[-1]
    
        if name == villager_name:
            print(villagers_motto)
            return villagers_motto

find_motto("villagers.csv", "Kiki")



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded_villagers = set()
    common_personality = None

    data = open(filename)
    
    for line in data:
        list_of_data = line.rstrip().split("|")
        name = list_of_data[0]
        personality = list_of_data[2]

        if name == villager_name:
            common_personality = personality
            break
    
    for line in data:
        list_of_data = line.rstrip().split("|")
        name = list_of_data[0]
        personality = list_of_data[2]
    
        if personality == common_personality:
            likeminded_villagers.add(name)
    
    print(likeminded_villagers)
    return likeminded_villagers
    # TODO: replace this with your code

find_likeminded_villagers("villagers.csv", "Teddy")
