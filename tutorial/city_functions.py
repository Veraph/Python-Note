def city_country(city, country, population = ''):
    '''return a str combine city and country'''
    if population:
        geo = city+', '+country+'-population '+str(population)
    else:
        geo = city+', '+country
    return geo