# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab1 Q3

principal = 2500
interest_rate = 0.05

def calculate(n):
    return round(principal*((1 + interest_rate) ** n) , 2)

f1 = "{:>5}   "
f2 = "{:.2f}"

print(f1.format("Years"), "Deposit")

for i in range(1,11):
    print(f1.format(i), f2.format(calculate(i)))