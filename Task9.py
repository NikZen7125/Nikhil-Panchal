# Function for User to input matrix
def input_matrix():
    # Initialize empty list for current matrix
    matrix = []
    # Loop through three rows
    for i in range(0,3):
        # Initialize empty list for current row
        row = []
        # Loop through three columns
        for j in range(0,3):
            # Get user input for current element
            row.append(int(input(f"Enter Element at [{i}][{j}]: ")))
        # Add row to current matrix
        matrix.append(row)
    # Print newline
    print()
    # Return matrix from user given input
    return matrix

# Get input matrix from user
matrix = input_matrix()

# matrix=[[2,1,3,],[4,0,1],[2,-1,2]]

# Initialize a list to hold sum results
sum = []

# Loop through the columns (i.e., calculating cofactor expansion along the first row)
for i in range(3):
    # Initialize a list to hold elements excluding the current row and column
    elements = []
    # Loop through the rows (excluding the current row)
    for j in range(1, 3):
        # Loop through the columns (excluding the current column 'i')
        for k in range(3):
            if k == i:  # Skip the element in the same column
                continue
            # Append the elements for cofactor calculation
            elements.append(matrix[j][k])
            # Print row and column indexes for debugging
            print(j, k)
    # Calculate the cofactor of the current element
    ans = (elements[0] * elements[3] - elements[1] * elements[2]) * matrix[0][i]
    # Append the cofactor result to the sum list
    sum.append(ans)

# Calculate the final determinant
result = sum[0] - sum[1] + sum[2]

# Output the determinant of the matrix
print("Determinant of Matrix:", result)