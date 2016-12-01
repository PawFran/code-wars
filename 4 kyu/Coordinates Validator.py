def is_valid_coordinates(coordinates):
    if any(c.isalpha() for c in coordinates):
        return False
    try:
        coordinates = [float(str.strip()) for str in coordinates.split(",")]
    except ValueError:
        return False

    if len(coordinates) != 2 or abs(coordinates[0]) > 90 or abs(coordinates[1]) > 180:
        return False

    return True


# print is_valid_coordinates("23.245, 1e1")
# print is_valid_coordinates("N23.43345, E32.6457")

x = 2
print [2, 2] < [3, 1]