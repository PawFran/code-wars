def telephoneWords (digitString):
    letters = []
    for digit in digitString:
        if digit == '2':
            letters.extend(['A', 'B', 'C'])
        elif digit == '3':
            letters.extend(['D', 'E', 'F'])
        elif digit == '4':
            letters.extend(['G', 'H', 'I'])
        elif digit == '5':
            letters.extend(['J', 'K', 'L'])
        elif digit == '6':
            letters.extend(['M', 'N', 'O'])
        elif digit == '7':
            letters.extend(['P', 'Q', 'R', 'S'])
        elif digit == '8':
            letters.extend(['T', 'U', 'V'])
        elif digit == '9':
            letters.extend(['W', 'X', 'Y', 'Z'])

    print letters

telephoneWords("0002")