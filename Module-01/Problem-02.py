# Write a Python program to read a file that contains lines of text.
# Convert each line into a list, list out all unique words and their frequency across whole file

file1 = open("myfile.txt", "r+")

string_words = file1.read()
file1.close()
word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(
    str(list(zip(word_list, word_freq)))))
