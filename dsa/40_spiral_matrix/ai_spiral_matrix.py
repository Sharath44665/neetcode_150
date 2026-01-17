def generate_spiral_matrix(n: int):
    # Initialize an n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries of the spiral
    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = 1  # Start filling with the number 1

    while left <= right and top <= bottom:
        # Fill the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  # Move down to the next row

        # Fill the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  # Move left to the previous column

        if top <= bottom:
            # Fill the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move up to the previous row

        if left <= right:
            # Fill the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Move right to the next column

    return matrix

# Example usage
n = 3
result = generate_spiral_matrix(n)
for row in result:
    print(row)


