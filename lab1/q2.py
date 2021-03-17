# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab1 Q2


coins = int(input("Enter an integer between 1 and 99: "))
print("One combination of coins that equals", coins, "cents is:")

quarter = coins // 25
dime = (coins % 25) // 10
nickel= ((coins % 25) % 10) // 5
penny = ((coins % 25) % 10) % 5

print(quarter, "quarters") if quarter > 1 else print(quarter, "quarter")
print(dime, "dimes") if dime > 1 else print(dime, "dime")
print(nickel, "nickels") if nickel > 1 else print(nickel, "nickel")
print(penny, "pennies") if penny > 1 else print(penny, "penny")