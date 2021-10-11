# to place the pivot value in the correct position
def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left<=right and list1[left] <= pivot:
            left = left+1
        while left<=right and list1[right] >= pivot:
            right = right-1
        if right < left:
            break
        else:
            list1[left],list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right
# to do the recursive to sort the elements
def quicksort(list1,first,last):
    if first<last:
       p = pivot_place(list1,first,last)  # calling the above function
       quicksort(list1,first,p-1)
       quicksort(list1,p+1,last)

# main
list1 = [13,2,34,12,43,35]
n = len(list1)
quicksort(list1,0,n-1)
print(list1)
