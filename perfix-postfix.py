
s = "+*+abc*+xyz"
# print(s)
stack = []

operators = set(['+', '-', '*', '/', '^'])

s = s[::-1]
# print(s)
for i in s:

    if i in operators:

        a = stack.pop()
        b = stack.pop()

        temp = a+b+i
        stack.append(temp)
        # print(*stack)

    else:
        stack.append(i)
        # print(*stack)

print(*stack)
