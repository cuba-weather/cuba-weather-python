from locations import locations

locations = sorted(locations, key=len)


def get_location(user_input: str) -> str:
    lower_input = user_input.lower()
    for location in locations:
        if lower_input in location.lower():
            return location
    return user_input
