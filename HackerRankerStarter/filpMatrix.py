matrix = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

matrix = [
    [1,4],
    [3,2]
]
col_len = len(matrix)

# show orig matrix
for i in range(col_len):
    print(matrix[i])

# flip first to rows
# this flips the row but it has to check if the flip is necessary
# only if tail is larger than head
for i in range(col_len//2):
    matrix[i] = matrix[i][::-1]


print("\n\n")
# show matrix after 1st flip
for i in range(col_len):
    print(matrix[i])

top = 0
bottom = col_len -1 
for i in range(col_len//2):
    while top < bottom:
        matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]
        top += 1
        bottom -=1

print("\n\n")
# show matrix after 2nc flip
for i in range(col_len):
    print(matrix[i])