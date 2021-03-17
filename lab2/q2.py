# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab2 Q2

def print_second_largest(nums):

    def get_second_largest(nums):
        #TODO: Return the second largest element and its index
        temp = nums.copy()
        temp.sort()
        result = temp[-2]
        index = nums.index(result)
        return result, index

    #TODO: Call the inner function and handle the output message
    if (len(nums) < 2):
        print("Oops, too few numbers in the list!")
    else:
        results = get_second_largest(nums)
        print("The second largest number is " + str(results[0]) + ", at index " + str(results[1]) + ".")


print_second_largest([4, 8, 3])
print_second_largest([1])
print_second_largest([3, 4, 5, 6, 7])