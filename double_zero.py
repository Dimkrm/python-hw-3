def double_zero(arr, n):
    count = 0
    for i in range(0, n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while (count < n):
        arr[count] = 0
        count+=1
def modify(ar, n):
    if n == 1:
        return
    for i in range(0, n - 1):
 
        if (arr[i] != 0) and (arr[i] == arr[i + 1]):
            arr[i] = 2 * arr[i]
            arr[i + 1] = 0
            i+=1
    double_zero(arr, n)
#def double_zero(array)
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i],end=" ")
 
arr = [ 1,0,2,3,0,4,5,0 ]
n = len(arr)
 
print("Original:",end=" ")
printArray(arr, n)
 
modify(arr, n)
 
print("\nModified:",end=" ")
printArray(arr, n)
 