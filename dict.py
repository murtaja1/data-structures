# a = {(1,2):1,(2,3):2}
# print(a.items())

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

# c = {1.0:1, 1:1}
# print(c)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# print(len(crates[box]))

# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r['Name']) == id(rec['Name']))

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)