# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab3 Q3

def word_diff(a,b):
    diff = 0
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]:
            diff += 1
    return diff


class Dictionary:
    def __init__(self, words):
        self.words = words
    def find_most_similar(self, search_key):
        # your code here
        min_diff = len(search_key)
        similar = ""
        for word in self.words:
            diff = word_diff(word,search_key) + abs(len(word)- len(search_key))
            if diff < min_diff:
                min_diff = diff
                similar = word
        return similar


fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])

print(fruits.find_most_similar('strawbery')) # prints "strawberry"
print(fruits.find_most_similar('bherry')) # prints "cherry"

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
print(things.find_most_similar('coddwars')) # prints "codewars"

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
print(languages.find_most_similar('heaven')) # prints "python" (last letter matched)
print(languages.find_most_similar('javascript')) # prints "javascript" (same words are obviously the most similar ones)

a = Dictionary(["note", "notes", "noted", "notify", "notified"])
print(a.find_most_similar('not'))
