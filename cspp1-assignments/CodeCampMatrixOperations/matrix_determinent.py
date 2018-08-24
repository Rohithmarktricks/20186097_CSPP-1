def get_matrix_minor(matrix,i,j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]




def get_matrix_determinent(matrix):
	if len(matrix) == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	else:
		determinant = 0
		for element in range(len(matrix)):
			determinant += ((-1)**element)*matrix[0][element]*get_matrix_determinent(get_matrix_minor(matrix,0,element))