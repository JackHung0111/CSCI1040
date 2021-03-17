# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab1 Q4

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "x", i, "=", f"{i*j:<3d}", end = " ")
    print(end="\n")