# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab2 Q1

def get_tax_payable(income):
    tax, temp = 0, income
    count = temp // 40000
    if(count == 0):
        tax += temp * 0.02
    elif(count == 1):
        tax += 40000 * 0.02
        tax += (temp - 40000) * 0.07
    elif(count == 2):
        tax += 40000 * (0.02 + 0.07)
        tax += (temp - 40000 * 2) * 0.12
    else:
        tax += 40000 * (0.02 + 0.07 + 0.12)
        tax += (temp - 40000 * 3) * 0.17
    return tax
    

n = int(input("Enter the number of people: "))
for i in range(1, n + 1):
    print("#"+str(i)+":")
    income = float(input("Enter the net chargeable income: "))
    print("The tax payable is: " + "{:.1f}".format(get_tax_payable(income)))
