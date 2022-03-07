
def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    if len(queue) < 1:
        return None
    return queue.pop(0)


def size(queue):
    return len(queue)


def choice(queue, value):
    match value:
        case 1:
            n = (input("enter the value to be pushed  "))
            return enqueue(queue, n)
        case 2:
            p = dequeue(queue)
            print("popped item: " + p)
        case 3:
            print("queue : " + str(queue))
        case 4:
            print("exited")
            return "exit"


queue = []
flag = 0
print("1. Enqueue  2. Dequeue 3. diplay 4. exit\n")
while(flag == 0):
    value = int(input("enter the choice  "))
    if choice(queue, value) == "exit":
        flag = 1
    elif value > 4 or value <= 0:
        print("     !!! enter the valid choice !!! ")
