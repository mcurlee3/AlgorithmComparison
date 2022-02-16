##Insertion Sort
def InsertionSort(List):
    for index in range(1, len(List)):
        key = List[index]
        previous = index - 1

        while previous >=0 and key < List[previous]:
            List[previous + 1] = List[previous]
            previous = previous - 1
        
        List[previous + 1] = key
    
    return List

##Merge Used for both recursive and iterative MergeSort
def Merge(List, l, m, r):
    n1 = m-l+1
    n2 = r-m

    left = [0]*n1
    right = [0]*n2

    for i in range(0, n1):
        left[i] = List[i+l]

    for i in range(0, n2):
        right[i] = List[i+1+m]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] < right[j]:
            List[k] = left[i]
            i += 1
        else:
            List[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        List[k] = left[i]
        k += 1
        i += 1
    while j < n2:
        List[k] = right[j]
        k += 1
        j += 1


##Recursive MergeSort
def MergeSort(List, left, right):
    if left < right:
        middle = (left + right)//2
        MergeSort(List, left, middle)
        MergeSort(List, middle+1, right)
        Merge(List, left, middle, right)

##Iterative MergeSort
def MergeSortI(List):
    current_size = 1
    # traversing subarrays
    while current_size < len(List) - 1:
        left = 0
        # subarray being sorted
        while left < len(List)-1:
            # calculating mid value
            mid = left + current_size - 1
            # current_size
            right = ((2 * current_size + left - 1, len(List) - 1)[2 * current_size + left - 1 > len(List)-1])
            # Merge
            Merge(List, left, mid, right)
            left = left + current_size*2
        # Increasing sub array size
        current_size = 2 * current_size

##DownHeap Recursive
def DownHeap(List, i, n):
    left = 2*i + 1
    right = 2*i + 2
    j = i
    if (left < n) and (List[left] > List[i]):
        i = left
    if (right < n) and (List[right] > List[i]):
        i = right
    if i != j:
        List[i], List[j] = List[j], List[i]
        DownHeap(List, i, n)

##DownHeap Iterative
def DownHeapR(List, i, n):
    done = False

    while not done:
        low = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and List[left] < List[i]:
            low = left
        else:
            low = i
        if right < n and List[right] < List[low]:
            low = right

        if low != i:
            List[i], List[low] = List[low], List[i]
            i = low
        else:
            done = True

##HeapSort Recursive      
def HeapSort(List, left, right):
    n = len(List)
    for i in range(n//2, -1, -1):
        DownHeap(List, i, n)

    for i in range(n-1, 0, -1):
        List[i], List[0] = List[0], List[i]
        DownHeap(List, 0, i)

##HeapSort Iterative
def HeapSortI(List, left, right):
    n = len(List)
    for i in range(n//2, -1, -1):
        DownHeap(List, i, n)

    for i in range(n-1, 0, -1):
        List[i], List[0] = List[0], List[i]
        DownHeap(List, 0, i)

def Partition(List, left, right):
    pivot = List[right]
    i = left - 1
    for j in range(left, right):
        if List[j] <= pivot:
            i = i + 1
        (List[i], List[j]) = (List[j], List[i])
    (List[i + 1], List[right]) = (List[right], List[i + 1])
    return i + 1

##QuickSort Recursive
def QuickSort(List, left, right):
    if left < right:
        p = Partition(List, left, right)
        QuickSort(List, left, p-1)
        QuickSort(List, p, right)

##QuickSort Iterative
def QuickSortI(List, left, right):
    n = right - left + 1
    temp = [0] * n

    l = -1

    l += 1
    temp[l] = left
    l += 1
    temp[l] = right

    while l >= 0:
        right = temp[l]
        l -= 1
        left = temp[l]
        l -= 1

        p = Partition(List, left, right)
    if p-1 > left:
        l += 1
        temp[l] = left
        l += 1
        temp[l] = p-1
    if p + 1 < right:
        l += 1
        temp[l] = p+1
        l += 1
        temp[l] = right

#Meadian for Modified Quick Search
def Median(List, left, right, mid):
    l = List[left]
    m = List[mid]
    r = List[right]

    if l <= m <= r:
        return m, mid
    if r <= m <= l:
        return m, mid
    if l <= r <= m:
        return r, right
    if m <= r <= l:
        return r, right
    return l, left

#Modified Partition for Modified Quick Search
def modPartition(List, left, right):
    pivot, x = Median(List, left, right, (left+right)//2)
    i = left + 1
    j = right

    while i < j:
        while i <= right and List[i] <= pivot:
            i += 1
        while j >= 0 and List[j] > pivot:
            j -= 1

        if i < j:
            List[i], List[j] = List[j], List[i]

        else:
            List[j], List[x] = pivot, List[j]
    return j

#Recursive Modified Quick Sort
def modQuickSort(List, left, right):
    if left < right: 
        if (left -1) > 8:
            p = modPartition(List, left, right)
            QuickSort(List, left, p-1)
            QuickSort(List, p+1, right)

    else:
        for i in range(left+1, right+1):
            key = List[i]
            j = i - 1

            while j >= left and List[j] > key:
                List[j+1] = List[j]
                j -= 1

            List[j+1] = key

#Iterative Modified Quick Sort
def modQuickSortI(List, left, right):
    if left < right: 
        if (right -1) > 8:
            p = modPartition(List, left, right)
            QuickSortI(List, left, p-1)
            QuickSortI(List, p+1, right)

        else:
            InsertionSort(List)