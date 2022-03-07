
def bubblesort(data):
    for i in range(len(data)):
        for j in range(len(data) - i-1):
            if data[j] > data[j+1]:

                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp


def mergesort(data):
    size = len(data)
    if(size) > 1:
        middle = size//2
        l_arr = data[middle:]
        r_arr = data[:middle]
        mergesort(l_arr)
        mergesort(r_arr)

        p = 0
        q = 0
        r = 0

        l_size = len(l_arr)
        r_size = len(r_arr)
        while p < l_size and q < r_size:
            if l_arr[p] < r_arr[q]:
                data[r] = l_arr[p]
                p += 1
            else:
                data[r] = r_arr[q]
                q += 1
            r += 1
        while p < l_size:
            data[r] = l_arr[p]
            p += 1
            r += 1
        while q < r_size:
            data[r] = r_arr[q]
            q += 1
            r += 1


n = int(input("enter the size of array  "))
data = []
for i in range(n):
    data.append(int(input("enter the value  ")))

ch = int(input(" 1 for Bubble sort and 2 for Merge sort\n"))
if ch is 1:
    bubblesort(data)
    print("sorted array :\n")
    print(data)
elif ch is 2:
    mergesort(data)
    print("Sorted array :\n")
    print(data)
