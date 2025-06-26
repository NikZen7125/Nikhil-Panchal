# Function for User to input matrices
def input_matrix():
    # Initialize empty list for user matrices
    user_matrix = []
    # Loop through two matrices
    for i in range(1,3):
        # Initialize empty list for current matrix
        matrix = []
        # Loop through three rows
        for j in range(0,3):
            # Initialize empty list for current row
            row = []
            # Loop through three columns
            for k in range(0,3):
                # Get user input for current element
                row.append(int(input(f"Enter Element at [{j}][{k}] in Matrix {i}: ")))
            # Add row to current matrix
            matrix.append(row)
        # Print newline
        print()
        # Add matrix to user matrices
        user_matrix.append(matrix)
    # Return list of user matrices
    return user_matrix

# Function for matrix multiplication
def matrix_mul(a, b):
    # Initialize result matrix
    matrix_ans = []
    
    # Iterate over rows of matrix a
    for i in range(0,3):
        # Initialize row for result matrix
        row = []
        # Iterate over columns of matrix b
        for j in range(0,3):
            # Initialize element for result matrix
            ans = 0
            # Perform dot product of row and column
            for k in range(0,3):
                ans += a[i][k] * b[k][j]
            # Append element to row
            row.append(ans)
        # Append row to result matrix
        matrix_ans.append(row)
        # Print current row of result matrix
        print(matrix_ans[i])

# Get input matrices from user
matrix_a, matrix_b = input_matrix()

print("Result Matrix:")

# Perform matrix multiplication
matrix_mul(matrix_a, matrix_b)