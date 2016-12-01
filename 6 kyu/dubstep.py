import re

def song_decoder(song):
    s = re.sub('(WUB)+', ' ', song).strip()
    return s

print song_decoder("AWUBBWUBC")