number=[-4,-3,-2,-1,0,2,4,6]
nums=[i for i in number if i<1 ]
print(nums)

list_of_lists=[[[1,2,3]],[[4,5,6]],[[7,8,9]]]
flattened_list_1=[outer for first in list_of_lists  for outer in first  ]
flattened_list_2=[row for other in flattened_list_1 for row in other]
print(flattened_list_2)



numbers=[(i,1,i*1,i*(i*1),i*(i*(i*1)),i*(i*(i*(i*1))),i*(i*(i*(i*(i*1))))) for i in range(11)]
print(numbers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list_1=[outer for first in countries  for outer in first  ]
flattened_list_2=[row for other in flattened_list_1 for row in other] 
new_lst=[]
for i in flattened_list_2:    
    new_lst.append(i.upper())
    





