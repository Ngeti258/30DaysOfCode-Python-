def add_two_numbers(first,second):
    return first+second
print(add_two_numbers(12,21))

def area_of_circle(radius):
    return 3.142*radius**2
print(area_of_circle(7))

def add_all_nums(*args):
    total=0
    for each in args:
        if type(each)==int:
            total = total+each
        else:
            print('Not a number')
    return total
print(add_all_nums(12,30,38293))
    
def convert_celcius_to_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit
print(convert_celcius_to_fahrenheit(20))

def check_season(month):
    if month=='September' or month=='October' or month=='November':
      print('Autumn')
    elif month=='December' or month=='January' or month=='February':
       print('Winter')
    elif month=='March' or month=='April' or month=='May':
       print ('Spring')
    elif month=='June' or month=='July' or month=='August':
       print('Summer')
    else:
       print('Invalid Month')
check_season('January')

# Do Q6 AND 7

def print_list(*args):
    for each in args:
        print(each)

print_list('hey',11,'what','are','you','doing')

def reverse_list(*elements):
    normal_to_reverse=[]
    for each in elements:
        normal_to_reverse.append(each)
    return normal_to_reverse[::-1] 
print(reverse_list('hey','i','think','german','will','win','the','world cup'))   

def capitalize_list_items(list):
    capitalized=[]
    for each_item in list:
        uppered=each_item.upper()
        capitalized.append(uppered)

    return capitalized

print(capitalize_list_items(['Potato','Tomato','Mango','Milk']))


def add_item(nums,*new_num):
    for each in new_num:
        nums.append(each)
    return nums
print(add_item([12,23,2,2,24],32))

def remove_item(lst,item):
    for each in lst:
        if each==item:
            lst.remove(each)
    return lst
print(remove_item(['Potato','Tomato','Mango','Milk'],'Milk'))


def sum_of_numbers(limit):
    total=0
    for each_number in range(limit+1):
        total += each_number
    return total
print(sum_of_numbers(100))


def sum_of_odds(num):
    total=0
    for each_odd in range(1,num+1,2):
        total += each_odd
    return total
print(sum_of_odds(7))


def sum_of_evens(num):
    total=0
    for each_even in range(0,num+1,2):
        total += each_even
    return total
print(sum_of_evens(7))

def evens_and_odds(limit):
    odds=0
    evens=0
    for each in range(limit+1):
        if each%2==1:
            odds += 1
        else:
            evens += 1
    print(f'The number of odds are {odds}')
    print(f'The number of evens are {evens}')

evens_and_odds(100)
            
def factorial(number):
    factor=1
    for each in range(1,number+1):
        factor *= each
    return factor
print(factorial(10))


def is_empty(list):
    if len(list)==0:
        print('Its empty')
    else:
        print('not empty')
is_empty('')

def calculate_mean(*numbers):
    total=0
    for num in numbers:
        total += num
    return total/len(numbers)
print(calculate_mean(7,2,3))

def calculate_median(*numbers):       
    sortee=sorted(numbers)
    return sortee[len(numbers)//2]
print(calculate_median(12,30,45,76,34,6,4,23,67,37))


def calculate_mode(*numbers):
    number_with_frequency=[]
    number_set=set()
    for each in numbers:
        number_set.add(each)    
    for each_set_number in number_set:
       values=numbers.count(each_set_number)
       newdict={each_set_number:values}
       number_with_frequency.append(newdict)
    new_highest=[]
    for nums in number_with_frequency:
        for key,value in nums.items():
           details=[value,key ]   
           new_highest.append(f'{details[1]}-')
           new_highest.append(details[0])     
    return new_highest
print(calculate_mode(12,30,45,76,34,6,4,23,67,67,37,23,67,37,67,37,12,30,12))
#the fisrt value in the output is the number in the list followed by the frequency


def calculate_range(*numbers):    
    sortee=sorted(numbers)
    return sortee[-1]-sortee[0]
print(calculate_range(21,3,2,4,35,4,54,5))

def calculate_variance(*numbers):
    totaled_squares=0
    squared=[]
    difference_with_mean=[]
    total=0
    for num in numbers:
        total += num
    mean=total/len(numbers)
    for num in numbers:
        difference_with_mean.append(mean-num)
    for each in difference_with_mean:
        square=each*each
        squared.append(square)
    for each in squared:
        totaled_squares += each
    return totaled_squares/(len(numbers)-1)
print(calculate_variance(12,3,25,6,68,4,79,8,33))

import math  
def calculate_standard_deviation(*numbers):
    totaled_squares=0
    squared=[]
    difference_with_mean=[]
    total=0
    for num in numbers:
        total += num
    mean=total/len(numbers)
    for num in numbers:
        difference_with_mean.append(mean-num)
    for each in difference_with_mean:
        square=each*each
        squared.append(square)
    for each in squared:
        totaled_squares += each
    return math.sqrt(totaled_squares/(len(numbers)-1))
print(calculate_standard_deviation(12,3,25,6,68,4,79,8,33))

import math
def is_prime(number): 
    if (number <= 1):
        return False 
    for i in range(2,number-1):
        if number%i==0:
            return False
    return True
print(is_prime(59))

def is_unique(*args):
    arg_set=set()
    arg_list=list()
    for each in args:
        arg_set.add(each)
        arg_list.append(each)
    if len(arg_list)==len(arg_set):
        return True
    return False
print (is_unique(12,4,35,4,46))

def same_data_type(*args):
    for each in args:
        for each_2 in args:
            if type(each)!=type(each_2):
                return False
        return True

print(same_data_type('hey',12,24,35,45,'jello'))


    











