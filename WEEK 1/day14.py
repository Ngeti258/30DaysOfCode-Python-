#map applies changes to each individual element in a list
#filter is used to remove elements of the list that do not meet the requirements
#reduce basically performs operations between the elements of the list

#higher order functions are functions that perform operations on elements without being defined
#closure is a function that has a nested function which is allowed to return values
#decorator allows function to recieve increased finctionality without changing its structure

#map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def multiply(x):
    return x*4
numbers_multiplied=map(multiply,numbers)
print(list(numbers_multiplied))

#filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(x):
    if x%2==1:
        return x
odd_numbers=filter(is_odd,numbers)
print(list(odd_numbers))

#reduce
# numbers=[1, 2, 3, 4, 5]
# def all_mult(x,y):
#     return x*y
# total_mult= reduce(all_mult,numbers)
# print(total_mult)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for each_country in countries:
    print(each_country)
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for each_name in names:
    print(each_name)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for each_number in numbers:
    print(each_number)

def to_upper(country):
    return country.upper()
to_upper_case=map(to_upper,countries)
print(list(to_upper_case))

def squared(number):
    return number**2
squared_numbers=map(squared,numbers)
print(list(squared_numbers))

def name_to_upper(x):
    return x.upper()
names_uppered=map(name_to_upper,names)
print(list(names_uppered))

def ends_with_land(country):
    if country.endswith('land'):
        return country
counties_with_land=filter(ends_with_land,countries)
print(list(counties_with_land))

def countries_with_len_six(country):
    if len(country)== 6:
        return country
six_gang=filter(countries_with_len_six,countries)
print(list(six_gang))

def countries_with_len_six_or_more(country):
    if len(country)>= 6:
        return country
six_gang_or_more=filter(countries_with_len_six_or_more,countries)
print(list(six_gang_or_more))

def countries_starting_with_E(country):
    if country.startswith('E'):
        return country
result=filter(countries_starting_with_E,countries)
print(list(result))










