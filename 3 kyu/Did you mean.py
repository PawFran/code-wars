
# match longest common substring
from difflib import SequenceMatcher
a = "Now is the time for all good men to come to the aid of their party."
b = "All good men are created equal."
a = 'rkacypviuburk'
b = 'zqdrhpviqslik'
s = SequenceMatcher(None, a, b)
res = s.find_longest_match(0, len(a), 0, len(b))
print a[res[0]: res[0] + res[2]]



# compute similarity

class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        # re-write it to work recursively
        minimum = -1
        similar = ''
        for word in words:
            to_remove, to_add = 0, 0
            last_found_term, last_found_word = -1, -1
            for i in range(len(term)):
                pos = word.find(term[i], last_found_word + 1)
                if pos != -1:
                    to_add += pos - last_found_word - 1
                    last_found_word = pos
                else:
                    to_remove += 1

            to_add += len(word) - last_found_word - 1
            res = to_remove + to_add
            if minimum == -1 or res < minimum:
                minimum = res
                similar = word
            print res

        return similar

# words = ['npyrgrpbdfqhhncdi', 'hirldidcuzbyb', 'riyhpvimgaliuxr', 'eglanhfredaykxr', 'znystgvifufptxr', 'ajacizfrgxfumzpvi', 'xikoctmrhpvi', 'ggcvrtxrtnafw', 'pxyousorusjxxbt', 'tdvibqccxr', 'fxjskybblljqr', 'hkldhadcxrjbmkmcdi', 'emvquxrvvlvwvsi', 'fxpvfhfrujjaifr', 'hwzsemiqxjwfk', 'iqkyztorburjgiudi', 'jhjyasikwyufr', 'cwhyyzaorpvtnlfr', 'ljxzjjorwgb', 'qojfrlhufr', 'fgtrjakzlnaebxr', 'nnsoamjkrzgldi', 'xrgdgqfrldwk', 'zqdrhpviqslik', 'hrwuhmtxxvmygb', 'ntwmwwmicnjvhtt', 'tklquxrnhfiggb', 'jcocndjkyb', 'afirbipbmkamjzw', 'dyhxgviphoptak', 'mhmkakybpczjbb', 'ucxmdeudiycokfnb', 'xuwahveztwoor', 'lnjhrzfrosinb', 'qifwqgdsijibor', 'kqijoorfkejdcxr', 'ppctybxgtleipb', 'clxmqmiycvidiyr', 'osbednerciaai', 'psaysnhfrrqgxwik', 'cfvruditwcxr', 'vkholxrvjwisrk', 'dihhiczkdwiofpr', 'cpnqknjyviusknmte', 'karpscdigdvucfr', 'xffrkbdyjveb', 'loogviwcojxgvi', 'pdyjrkaylryr', 'iroezmixmberfr', 'sefsknopiffajor']
words = ['pdyjrkaylryr', 'zqdrhpviqslik']
test_dict = Dictionary(words)
print test_dict.find_most_similar('rkacypviuburk')
# 'xffrkbdyjveb' should equal 'zqdrhpviqslik'