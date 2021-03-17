# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab4 Q3

def merge_and_sort(input_file_A, input_file_B, output_file):
    try:
        f_a = open(input_file_A)
    except OSError:
        print("File access error!")
    try:
        f_b = open(input_file_B)
    except OSError:
        print("File access error!")

    f_o = open(output_file, "w")
    result = []
    listA = f_a.readlines()
    listB = f_b.readlines()
    result.extend(listA)
    result.extend(listB)
    result.sort()
    try:
        result = [str(int(x)) + "\n" for x in result]
    except TypeError:
        print("Invalid input!")
    f_o.writelines(result)
    f_a.close()
    f_b.close()
    f_o.close()
    


merge_and_sort("a.txt", "b.txt", "c.txt")# Creates c.txt

