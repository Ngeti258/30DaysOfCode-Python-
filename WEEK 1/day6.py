empty_tuple=tuple()
print(empty_tuple)
brothers=('Eberly','Pennil','Billion')
sisters=('Esther','Emily','Monica')
siblings=brothers+sisters
print(siblings)
print(len(siblings))
family_members=list(siblings)
family_members.insert(0,'Sterwart')
family_members.insert(1,'Jnae')
print(family_members)
parents=family_members[0:2]
siblings=family_members[2:]
print(parents)
print(siblings)

fruits=('Banana','Apple','Guava')
vegetables=('Cabbage','Kale','Broccolli','Tomato')
animal_products=('Milk','Meat','Cheese')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
print(food_stuff_lt[len(food_stuff_lt)//2])
food_stuff_lt.remove('Broccolli')
print(food_stuff_lt)
print(food_stuff_lt[3:-3])

del food_stuff_tp
#print(food_stuff_tp)
nordic_countries=('Denmark','Finland','Iceland','Norway','Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)