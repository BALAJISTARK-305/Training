
def postfixToInfix(postfix):
    stack = []

    i = len(postfix) - 1
    while i >= 0:
        if not isOperator(postfix[i]):

            stack.append(postfix[i])
            i -= 1
        else:
            a = stack.pop()
            b = stack.pop()
            s = "(" + b + postfix[i] + a + ")"
            stack.append(s)
            i -= 1

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


s = "ab+c*xy+z*+"
s = s[::-1]
print(postfixToInfix(s))
