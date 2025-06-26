# Task 8 : Matrix Multiplication

# Function to input two 3x3 matrices from the user
def input_matrix():
    user_matrix = []
    for i in range(1, 3):
        matrix = []
        for j in range(0, 3):
            row = []
            for k in range(0, 3):
                # Get user input for each matrix element
                row.append(int(input(f"Enter Element at [{j}][{k}] in Matrix {i}: ")))
            matrix.append(row)
        print()
        user_matrix.append(matrix)
    return user_matrix

# Function to multiply two 3x3 matrices
def matrix_mul(a, b):
    matrix_ans = []
    for i in range(0, 3):  # Iterate over rows of matrix 'a'
        row = []
        for j in range(0, 3):  # Iterate over columns of matrix 'b'
            ans = 0
            for k in range(0, 3):  # Perform dot product for row and column
                ans += a[i][k] * b[k][j]
            row.append(ans)
        matrix_ans.append(row)
        print(matrix_ans[i])

# Input matrices from the user
matrix_a, matrix_b = input_matrix()

print("Result Matrix:")
# Multiplying the matrices
matrix_mul(matrix_a, matrix_b)
