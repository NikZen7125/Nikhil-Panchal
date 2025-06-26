# Function to input a 3x3 matrix from the user
def input_matrix():
    matrix = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            # Get user input for each matrix element
            row.append(int(input(f"Enter Element at [{i}][{j}]: ")))
        matrix.append(row)
    print()
    return matrix

# Get input matrix from the user
matrix = input_matrix()

# Initialize list to hold sum results for cofactor expansion
sum = []

# Loop through the columns
for i in range(3):
    elements = []
    # Loop through the remaining rows (excluding the first row)
    for j in range(1, 3):
        for k in range(3):
            if k == i:  # Skip current column
                continue
            elements.append(matrix[j][k])  # Append elements for cofactor calculation
    # Calculate cofactor for the current element
    ans = (elements[0] * elements[3] - elements[1] * elements[2]) * matrix[0][i]
    sum.append(ans)

# Calculate the determinant
result = sum[0] - sum[1] + sum[2]

print("Determinant of Matrix:", result)
