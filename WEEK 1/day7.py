it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]

print(len(it_companies))
it_companies.add('Twitter')
#print(it_companies)
multiple_it_companies={'Intel','Unilever','Deltalogic'}
it_companies.update(multiple_it_companies)
print(it_companies)
it_companies.pop()
print(it_companies)


#A.update(B)
print(A)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
#print(A)

age_to_set=set(age)
print(len(age_to_set))
print(len(age))


#String is text hold words...
#list is a data type that hold elements that can be manipulated 
#set is unlike a list where a set can not be manipulated and contains unique elements


unique_words='I am a teacher and i love to inspire and teach the people'
new=(unique_words.split(' '))
print(len(new))
to_set=set(new)
print(len(to_set))
