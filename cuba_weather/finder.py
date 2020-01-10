from Levenshtein import distance
from locations import locations

locations = sorted(locations, key=len)


def get_location(user_input: str) -> str:
    lower_input = user_input.lower()
    for location in locations:
        if lower_input in location.lower():
            return location
    best_location = locations[0].lower()
    best_distance = distance(lower_input, best_location)
    for i in range(1, len(locations)):
        actual_location = locations[i]
        actual_distance = distance(user_input, actual_location)
        if actual_distance < best_distance:
            best_location = actual_location
            best_distance = actual_distance
    return best_location
