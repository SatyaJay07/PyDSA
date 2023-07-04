def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    print(arr)
ar=[5,4,3,2]
insertionSort(ar)
print("end")

#output below
"""[2, 3, 4, 5]
end"""
