# 1155108381
# Quiz Q1

input_list = input("Enter width and height: ").split(" ")
w, h = int(input_list[0]), int(input_list[1])

# print first row
for i in range(w):
    print("* ", end="")
print("")

# print other row
for i in range(h-2):
    for j in range(w):
        if(j == 0 or j == w-1):
            print("* ",end= "")
        else:
            print("  ",end="")
    print("")

# print last row
if (h > 1):
    for i in range(w):
        print("* ", end="")
print("")

