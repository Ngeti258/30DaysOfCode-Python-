print('Thirty '+'Days '+'Of '+'Python')
print('Coding '+'For '+'All')
company='Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize().title().swapcase())

#word_slicing
words='Coding for all'
print(words[6:])

print(words.find('Coding'))
print(words.replace('Coding','Python'))

new_words='Python for Everyone'
print(new_words.replace('Everyone','All'))

print(words.split( ))

companies='Facebook,Google,Microsoft,IBM,Oracle,Amazon'
print(companies.split(','))

print(words[0])
print(words.rindex('l'))

print(words[10])
print(new_words[0:13:5])
print(words[0:12:4])

print(words.index('C'))
print(words.index('f'))

print(words.rfind('l'))

sentence='You cannot end a sentence with because because because is a conjuction'
print(sentence.find('because'))

print(sentence.rindex('because'))

print(sentence[31:54])

print(sentence.index('because'))

print(sentence[31:54])

print(words.startswith('Coding'))

print(words.endswith('coding'))

spaced=' Coding For All '
print(spaced.expandtabs(0))

#30DaysOfPython is not an identifier because it starts with a number
#thirty_days_of_python is an identifier

python_libraries=['Django','Flask','Bottle','Pyramid','Falcon']
print(' #'.join(python_libraries))
print('I am enjoying this challenge\n.I just wonder what is next')

print('Name\tAge\tCountry\tCity\nGabriel\t22\tKenya\tMachakos')

radius=10
area=3.142*radius**2
print('The area of a circle with radius {} is {} meters square'.format(radius,area))

