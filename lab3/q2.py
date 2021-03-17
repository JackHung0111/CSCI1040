# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab3 Q2


def find_killer(suspects_dict, victims):
    for killer in suspects_dict:
        if (all(name in suspects_dict[killer] for name in victims)):
            return killer


dic = {
 'Jackson': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']
}
dead = ['Lucas', 'Bill']

print(find_killer(dic,dead))