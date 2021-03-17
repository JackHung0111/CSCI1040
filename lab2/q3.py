# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab2 Q3

def do_matrix_operation(A, opt, B):

    def add(A, B):
        #TODO: return a matrix resulted from the addition of A and B
        result = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] + B[i][j]
        return result
            
    def multiply(A, B):
        #TODO: return a matrix resulted from the multiplication of A and B
        result = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
    #TODO: check opt and call the corresponding operator function
    if(opt == "+"):
        return add(A,B)
    if(opt == "."):
        return multiply(A,B)
    


# 3x3 matrix
X = [[12, 7, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]]

# 3x3 matrix
Y = [[5, 8, 1],
 [6, 7, 3],
 [4, 5, 9]]

print(do_matrix_operation(X, '+', Y)) # addition
print(do_matrix_operation(X, '.', Y)) # multiplication