#sets are unordered unique collections no duplicate data.
s={3,23,2,11}
p={5,23,9,12}
print(s, type(s))
# print[s[3]]#it will not following indexing shows error bcoz set is unordered.
print(s.remove(2))#it will remove that  element.
print(s.add(2))#it will add that element.
print(s.pop())#it will remove random element.
c=s.union(p)
c=s.intersection(p)
print(c)