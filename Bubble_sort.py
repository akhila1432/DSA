#..................................... BUBBLE SORT ALGORITHM .......................

def bubble_sort(arr):
    n = len(arr)
    for j in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
               temp = arr[i]
               arr[i] = arr[i+1]
               arr[i+1] = temp

arr = [2,4,12,3,1,45,76,25]
bubble_sort(arr)
print(arr)