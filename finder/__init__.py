f = open('finder/locations.txt')

locations = sorted(f.read().split('\n'), key=len)

def get_location(user_input):
    lower_input = user_input.lower()

    for l in locations:
        if l.lower().find(lower_input) != -1:
            return l

    raise Exception('{0} no se encuentra en la base de datos'.format(user_input))