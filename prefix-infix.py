
def prefixToInfix(prefix):
    stack = []

    for i in range(len(prefix)):
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
        else:
            a = stack.pop()
            b = stack.pop()
            str = "(" + a + prefix[i] + b + ")"
            stack.append(str)

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


str = "+*+abc*+xyz"
print(prefixToInfix(str))
