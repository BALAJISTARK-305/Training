# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

out = []


def allKLength(s, k):

    n = len(s)
    allKLengthRec(s, "", n, k)


def allKLengthRec(s, prefix, n, k):

    if (k == 0):
        out.append(prefix)
        return

    for i in range(n):

        newPrefix = prefix + s[i]

        allKLengthRec(s, newPrefix, n, k - 1)


s = ['a', 'e', 'i', 'o', 'u']
k = 5
j = 0
allKLength(s, k)
for i in out:
    if len(set(i)) == len(i):
        print(i)
        j += 1
print(j)
