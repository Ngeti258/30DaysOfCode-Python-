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

def caculate_slope(equation):
    y=mx+c