try:
    from .locations import locations
except:
    from locations import locations

locations = sorted(locations, key=len)


def distance(s1, s2):
    d = {}
    for i in range(-1, len(s1) + 1):
        d[i, -1] = i + 1
    for j in range(-1, len(s2) + 1):
        d[-1, j] = j + 1
    for i, cs1 in enumerate(s1):
        for j, cs2 in enumerate(s2):
            cost = int(cs1 != cs2)
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
            if not i or not j:
                continue
            if cs1 != cs2:
                continue
            d[i, j] = min(d[i, j], d[i - 2, j - 2] + cost)
    return d[len(s1) - 1, len(s2) - 1]


def get_location(user_input: str) -> str:
    lower_input = user_input.lower()
    for location in locations:
        if lower_input in location.lower():
            return location
    return user_input


def get_suggestion(user_input: str) -> str:
    lower_input = user_input.lower()
    best_location = locations[0].lower()
    best_distance = distance(lower_input, best_location)
    for i in range(1, len(locations)):
        actual_location = locations[i]
        actual_distance = distance(user_input, actual_location)
        if actual_distance < best_distance:
            best_location = actual_location
            best_distance = actual_distance
    return best_location
