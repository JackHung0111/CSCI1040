# 1155108381
# Quiz Q4

class WordCounter:
    def __init__(self, filename):
        with open(filename) as f:
            self.string = f.read().split()
            self.string2 = []
            for word in self.string:
                self.string2.append(word.lower().replace(",","").replace(".","").replace(";","").replace("!",""))
            print(self.string2)

        
    trivial_words = ['in', 'at', 'on', 'of', 'to', 'for', 'a', 'an', 'the', 'and']

    def frequency(self):
        dict1 = {}
        for word in self.string2:
            if not(word in self.trivial_words):
                dict1[word] = self.string2.count(word)
                while (word in self.string2):
                    self.string2.remove(word)
        return dict1


import json
wc = WordCounter("q4data.txt")
print(json.dumps(wc.frequency(), indent=4, sort_keys=True))

        
    
