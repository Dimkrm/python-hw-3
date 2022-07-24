R = 3 ;
C = 3;
def Spiral(arr, mat):
	top = 0;
	bottom = R - 1;
	left = 0;
	right = C - 1;
	index = 0;
	while (True):
		if(left > right):
			break;
		for i in range(left, right + 1):
			mat[top][i] = arr[index];
			index += 1;
		top += 1;
		if (top > bottom):
			break;
		for i in range(top, bottom+1):
			mat[i][right] = arr[index];
			index += 1;
		right -= 1;
		if (left > right):
			break;
		for i in range(right, left-1, -1):
			mat[bottom][i] = arr[index];
			index += 1;
		bottom -= 1;
		if (top > bottom):
			break;
		for i in range(bottom, top-1, -1):
			mat[i][left] = arr[index];
			index += 1;
		left += 1;
def printSpiral(mat):
	for i in range(R):
		for j in range(C):
			print(mat[i][j],end= " ");
		print();
if __name__ == '__main__':
	arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ];
	mat= [[0 for i in range(C)] for j in range(R)];
	Spiral(arr, mat);
	printSpiral(mat);

