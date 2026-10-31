f = open("Poem.txt", "r")
t = f.read().lower()
f.close()

words = t.split()
to_c = words.count("to")
the_c = words.count("the")

print("to:", to_c)
print("the:", the_c)
print("Hello")
