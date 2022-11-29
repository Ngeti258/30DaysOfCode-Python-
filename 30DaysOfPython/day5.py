empty_list=list()
print(empty_list)

new_list=['Law','Engineering','Medicine','CompSci','Education']
print(len(new_list))

print(new_list[0::2])

details=['Gabriel',22,185,'Single','Machakos']
name,age,height,marital_status,address,*rest=details
print(details)

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[3],it_companies[-1])
it_companies[0]='Netflix'
print(it_companies)
it_companies.append('Facebook')
print(it_companies)

it_companies.insert(len(it_companies)//2,'Unilever')
print(it_companies)

it_companies[0].upper()
print(it_companies)
print('#'.join(it_companies))
print('IBM' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:])
print(it_companies[:-3])
print(it_companies[len(it_companies)//2])
del it_companies[0]
print(it_companies)
del it_companies[len(it_companies)//2]
print(it_companies)
del it_companies[-1]
print(it_companies)
print(it_companies.clear())
del it_companies
#print(it_companies)

front_end=['HTML','CSS','JS','React','Redux']
back_end=['Node','Express','MongoDB']
joined=front_end+back_end
print(joined)
joined[5]='Python and SQL'
print(joined)

age=[19,22,19,24,20,25,26,24,25,24]
age.sort()
print(age)
min_age=age[0]
max_Age=age[-1]
age.append(min_age)
age.append(max_Age)
age.sort()
print(age)

print(age[len(age)//2])

sum=0
for i in age:
    sum=sum+i
#print(sum)
average_age=sum//(len(age))
print(average_age)
range=max_Age-min_age
print(range)

print
# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Cape Verde',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombi',
#   'Comoros',
#   'Congo (Brazzaville)',
#   'Congo',
#   'Costa Rica',
#   "Cote d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor Timur)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia, The',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Macedonia',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia and Montenegro',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Swaziland',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Taiwan',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe',
# ];
# print(countries[len(countries)//2])
# print(countries[0:len(countries)//2])
# print(countries[len(countries)//2:])

# first,second,third,*scandinavia=['china','Russia','USA','Finland','Sweden','Norway','Denmark']
# print(scandinavia)