L = [1, "a" , "string" , 1+2]
print (L)
L.append(85) 
print (L)
L.pop()
print (L)
print (L[1])


a = 'This is not a string'
print (a)
b = "This is not a string"
print (b)
c= '''This is a string'''
print (c)


tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])

d = {1: 'Lorem', 2: 'Ipsum', 3: 'Dolerum'}
print(d)


d1 = {1: 'God', 2: 'of', 3: 'War'}
print(d1)
d2 = dict(a = "House", b = "of", c = "Cards")
print(d2)

d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
print(d["name"])
print(d.get("name"))


d = {1: 'Game', 2: 'of', 3: 'Thrones'}
d["age"] = 22
d[1] = "Python dict"
print(d)
