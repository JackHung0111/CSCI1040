# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab3 Q5

class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page
        
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
        
    # returns the number of pages
    def page_count(self):
        return int(self.item_count() / self.item_per_page) + (self.item_count() % self.item_per_page > 0)
        
    # returns the number of items on the current page. page_index is zero-based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        elif self.page_count() - page_index == 1:
            return int(self.item_count() % self.item_per_page)
        else:
            return self.item_per_page


    # determines which page an item is on (zero-based indexes)
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        else:
            return int(item_index / self.item_per_page)

'''
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # prints 2
print(helper.item_count()) # prints 6
print(helper.page_item_count(0)) # prints 4
print(helper.page_item_count(1)) # last page, prints 2
print(helper.page_item_count(2)) # prints -1 since the page is invalid

# page_index() takes an item index and returns the page that it belongs to
print(helper.page_index(5)) # prints 1 (zero based index)
print(helper.page_index(2)) # prints 0
print(helper.page_index(20)) # prints -1
print(helper.page_index(-10)) # prints -1 because negative indexes are invalid
'''