#!python3

file = open("data.csv")
data = file.read()


myData = data.split("\n")

db = []
for i in myData:
    db.append(i.split(","))

print(db[0])
for i in db:
    if i[1] == "141769":
        print(i)
        

