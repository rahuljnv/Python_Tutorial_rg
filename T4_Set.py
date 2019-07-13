# Set

s = set()
l = [1,2,3,4,5]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
print(type(l))

s.add(1)
s.add(2)

s1 = s.union({1,2,3,4})
print(s, s1)

s1 = s.intersection({1,2,3,4})
print(s, s1)

print(len(s))
print(max(s))

print(s.isdisjoint(s1))# No intersection--False

s.remove(2)
print(s)