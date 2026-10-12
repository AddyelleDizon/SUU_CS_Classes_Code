def insertionSort(A):
    n = len(A)

    for j in range(1, n):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

    return A

def reversedInsertionSort(A):
    n = len(A)

    for j in range(1, n):
        key = A[j]
        # Insert B[j] into the sorted sequence B[1...j-1]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

    return A

def merge(left, right):
    merged = []
    i = j = 0 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def mergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    
    mid = len(A) // 2
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])

    return merge(left, right)

def bubbleSort(A):
    n = len(A)

    for i in range(n - 1):
        for j in range (n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    
    return A

arr1 = [6, 7, 4, 9, 0, 5]
arr2 = [6, 7, 4, 9, 0, 5]
arr3 = [6, 7, 4, 9, 0, 5]
arr4 = [6, 7, 4, 9, 0, 5]

B = insertionSort(arr1)
C = reversedInsertionSort(arr2)
D = mergeSort(arr3)
E = bubbleSort(arr4)

print("This is insertion sort: ", B)
print("This is reversed insertion sort: ", C)
print("This is merge sort: ", D)
print("This is bubble sort: ", E)