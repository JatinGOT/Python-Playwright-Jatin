str = 1
str2 = "jatin"

print("{} {}".format(str,str2))


# Split
print(str2.split("."))


text = "Python.Java.C++.JavaScript"

# Split the string
words = text.split(".")
print(words)

# Join the list using a different separator
new_text = " | ".join(words)
print(new_text)



tst = "Jatin.Kumar"

print(" ".join(tst.split(".")))