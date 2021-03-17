# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab3 Q1


def fillable(stock, merch, n):
    for name in stock:
        if name == merch:
            if n < stock[name]:
                return True
    return False

'''
stock = {
 'football': 4,
 'boardgame': 10,
 'Lego': 1,
 'doll': 5,
}
print(fillable(stock, 'football', 3))
print(fillable(stock, 'Lego', 2))
print(fillable(stock, 'action figure', 1))
'''