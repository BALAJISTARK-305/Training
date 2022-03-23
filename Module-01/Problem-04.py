# Write a Python function to insert a string in the middle of a string

# This is a garden <-- beautiful, 4
# This is a beautiful garden

def ins_middle(strg, word, i):
    i = i-1
    return " ".join(strg[:i] + word + strg[i:])


strg = input('Enter the Sentence : ')
stlist = []
stlist = strg.split(" ")
wol = []
wol.append(input('Enter the word to be inserted : '))
place = int(input('Enter the position : '))
print(ins_middle(stlist, wol, place))
