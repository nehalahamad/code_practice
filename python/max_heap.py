# Max heap
def max_heapify(arr, i, heap_size):
    l, r = 2*i+1, 2*i+2
    largest = i
    if l<=heap_size and arr[l]>arr[largest]:
        largest = l
    if r<=heap_size and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)
    return arr
        
def build_max_heap(arr, heap_size):
    for i in range((heap_size-1)//2, -1, -1):
        max_heapify(arr, i, heap_size)

def heap_extract_max(arr):
    if len(arr)<1:
        raise Exception('heap underflow')
    maxx = arr[0]
    arr[0] = arr.pop()
    build_max_heap(arr)
    return maxx

def heap_sort(arr, heap_size):
    build_max_heap(arr, heap_size)
    
    for i in range(heap_size, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)

# ===========================================

arr = [4,5,6,1,2,4,32,3,9,8]
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [32, 9, 6, 5, 8, 4, 4, 3, 1, 2]
# maxx = heap_extract_max(arr)
heap_size = len(arr)-1
heap_sort(arr, heap_size)
print(arr)