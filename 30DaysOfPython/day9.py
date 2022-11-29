# age=int(input('enter your age? '))
# driving_age=18
# if age>=18:
#     print('You are old enough to drive')
# else:
#     print(f'You  have to wait {driving_age-age} years to be able to drive')


# my_age=22
# your_age=int(input('Enter your age? '))
# if my_age>your_age:
#     print(f'I am {my_age-your_age} years older than you')
# elif your_age>my_age:
#     print(f'You are {your_age-my_age} years older than me')
# else:
#     print('We are the same age')

# number_one=int(input('Enter Number 0ne: '))
# number_two=int(input('Enter Number two: '))
# if number_one>number_two:
#     print(f'{number_one} is greater than {number_two}')
# elif number_two>number_one:
#     print(f'{number_two} is greater than {number_one}')
# else:
#     print(f'{number_one} is equal to {number_two}')

# Mark=int(input('Enter your marks: '))
# if Mark<=100 and Mark>80:
#     print('A')
# elif Mark>=70 and Mark<79:
#     print('B')
# elif Mark>=60 and Mark<69:
#     print('C')
# elif Mark>=50 and Mark<59:
#     print('D')
# elif Mark>=0 and Mark<49:
#     print('F')
# else:
#     print('Out of Bounds')



# month=input('Enter the month: ')
# if month=='September' or month=='October' or month=='November':
#     print('Autumn')
# elif month=='December' or month=='January' or month=='February':
#     print('Winter')
# elif month=='March' or month=='April' or month=='May':
#     print('Spring')
# elif month=='June' or month=='July' or month=='August':
#     print('Summer')
# else:
#     print('Invalid Month')


# fruits = ['banana','Orange','mango','Lemon']
# fruit=input('Enter a fruit: ')
# if fruit in fruits:
#     print('That fruit already exists in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)

person={
    'first_name': 'Gabriel',
    'last_name': 'Ngeti',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    middle=(len(person['skills'])//2)
    print(person['skills'][middle])

if 'skills' in person:
    print('Python' in person['skills'])



if 'Javascript' in person['skills'] and 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
    print('He is a full stack developer')
elif 'Javascript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
    print('He is a backend developer')
else:
    print('Unknown title')

if person['is_marred'] and person['country']=='Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is Married')
else:
    print('He aint married')


