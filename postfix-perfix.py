operators = set(['+', '-', '*', '/', '^'])


def postToPre(post):

    s = []

    for i in post:

        if i in operators:

            a = s.pop()
            b = s.pop()

            temp = i + b + a

            s.append(temp)
            # print(*s)

        else:

            s.append(i)
            # print(*s)
    return s


post = "ab+c*xy+z*+"
# print(post)

print("Prefix : ", *postToPre(post))
