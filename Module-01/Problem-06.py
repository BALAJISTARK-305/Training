# Write a Python program to create all possible permutations from a given collection of distinct numbers

# 1,3,6,9
# 1369
# 1396

def permute(nums):
    result = [[]]
    out = []
    for n in nums:
        new_perms = []
        for perm in result:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result = new_perms
    for i in result:
        temp = "".join(i)
        out.append(temp)
    res = " , ".join(out)
    return res


myNum = ['1', '3', '6', '9']
print("Original Cofllection: ", myNum)
print("Collection of distinct numbers:\n", permute(myNum))
