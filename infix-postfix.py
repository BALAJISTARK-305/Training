

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0


def infixToPostfix(infix):
    operators = []
    operands = []

    for i in range(len(infix)):
        if (infix[i] == '('):
            operators.append(infix[i])
            # print(*operators)

        elif (infix[i] == ')'):
            while (len(operators) != 0 and operators[-1] != '('):

                op1 = operands.pop()

                op2 = operands.pop()

                op = operators.pop()

                tmp = op2 + op1 + op
                operands.append(tmp)
                # print(*operands)

            operators.pop()

        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")
            # print(*operands)

        else:
            while (len(operators) != 0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands.pop()

                op2 = operands.pop()

                op = operators.pop()

                tmp = op2 + op1 + op
                operands.append(tmp)
                # print(*operands)
            operators.append(infix[i])
            # print(*operators)

    return operands[-1]


s = "(((a+b)*c)+((x+y)*z))"
# print(s)
print(infixToPostfix(s))
