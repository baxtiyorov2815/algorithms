# O(n^2)
def bubblesort(arr, sorted=False):

    while not sorted:
        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False

    return arr

arr = [5, 3, 50, 68, 12]
print("hello")
print(bubblesort(arr))