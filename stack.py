
def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop_s(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


def choice(stack, value):
    match value:
        case 1:
            n = (input("enter the value to be pushed  "))
            return push(stack, n)
        case 2:
            p = pop_s(stack)
            print("popped item: " + p)
        case 3:
            print("stack : " + str(stack))
        case 4:
            return "exit"


stack = []
flag = 0
print("1. push  2. pop 3. diplay 4. exit\n")
while(flag == 0):
    value = int(input("enter the choice  "))
    if choice(stack, value) == "exit":
        flag = 1
    else:
        print("     !!! enter the valid choice !!! ")
