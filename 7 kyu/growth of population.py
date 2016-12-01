def nb_year(p0, percent, aug, p):
    count = 0
    current_pop = p0
    while current_pop < p:
        current_pop += current_pop * (percent / 100) + aug
        count += 1

    return count

