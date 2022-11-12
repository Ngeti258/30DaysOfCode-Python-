dog=dict()
dog={'Name':'Tusker','color':'Black','Breed':'Shephard','Legs':'Short','Age':7}
print(dog)
student={'first_name':'Gabriel','last_name':'Ngeti','Gender':'Male','age':22
,'maritial_status':'married','skills':['Dancing',
'Football','Coding'],'Country':'Kenya','City':'Machakos','Address':{'Street':'Kthemboni','Postal':'90100'}}
print(len(student))
print(student.get('skills'))

student['skills'].append('HTML')
print(student.get('skills'))

key=student.keys()
print(key)
value=student.values()
print(value)
tuples=student.items()
print(tuples)

del student['skills']
print(student)

del student
print(student)