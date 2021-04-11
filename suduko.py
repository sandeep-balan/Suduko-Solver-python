board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#   Print the board in suduko format
def print_board(bo):
	for i in range(len(bo)):

		#After every three rows we want to print the line
		
		if i % 3 == 0 and i != 0 :
				print("------------------------")
		for j in range((len(bo[0]))):

			# After every three coloums we wnat to print the symbol
			
			if j % 3 == 0 and j !=0:
				print(" | ",end = '')
			if j == 8:
				print(bo[i][j])
			else:
				print(bo[i][j],end =' ')

# Find the empty element in the suduko board
def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j)
	return None

# To check whether the given number is valid or not
def check_valid(bo, num, pos):

	# Check the rows
	for i in range(len(bo[0])):
		if bo[pos[0]][i]== num and pos[1] != i:
			return False

	# Check the coloums
	for j in range(len(bo)):
		if bo[j][pos[1]] == num and pos[0] != j:
			return False

	# Check the 3 X 3 box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for k in range(box_y * 3, box_y * 3 + 3):
		for l in range(box_x * 3, box_x * 3 +3):
			if bo[k][l] == num and (k, l) != pos:
				return False
	return True

# Let's solve the suduko board
def solve(bo):
	find = find_empty(bo)
	if not find:
		return True
	else:
		(row, col) = find

	for i in range(1,10):
		if check_valid(bo, i, (row ,col)):
			bo[row][col] = i

			if solve(bo):
				return True
		bo[row][col] = 0
	return False

print_board(board)	
solve(board)
print()
print()
print("The solved Suduko board")
print_board(board)