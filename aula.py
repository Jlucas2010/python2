
with open("file", "r") as file:
    c = file.read()
    print(c)

with open("file", "r") as file:
    c1 = file.readline()
    print(c1)
    c2 = file.readline()
    print(c2)

with open("file", "r") as file:
    c0 = file.readlines()
    for l in c0:
        print(l)