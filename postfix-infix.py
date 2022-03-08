
def postfixToInfix(postfix):
    stack = []

    for i in range(len(postfix)):
        if not isOperator(postfix[i]):

            stack.append(postfix[i])
        else:
            a = stack.pop()
            b = stack.pop()
            s = "(" + b + postfix[i] + a + ")"
            stack.append(s)

    return stack.pop()


def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


s = "ab+c*xy+z*+"
s = s[::-1]
print(postfixToInfix(s))
