# Take a list of numbers and sort using bubble sort

def bubblesort(data):
    for i in range(len(data)):
        for j in range(len(data) - i-1):
            if data[j] > data[j+1]:

                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp


n = int(input("enter the size of array  "))
data = []
for i in range(n):
    data.append(int(input("enter the value  ")))

bubblesort(data)
print("sorted array :\n")
print(data)
