import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
match = paragraph.replace('.','')
new_match=re.split(' ',match)
st=set()
for i in new_match:
    st.add(i)
for each in st:
    values=new_match.count(each)
    newdict={values:each}
    print(newdict)


text='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles'
match_2=re.findall(r'-?\d+',text)
print(int(match_2[-1])-int(match_2[0]))

# def is_valid_variable(name):
#     if name[0]==
    
# print(is_valid_variable('1this'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
match_1=re.sub('%','',sentence)
match_2=re.sub('&','',match_1)
match_3=re.sub('@','',match_2)
match_4=re.sub('#','',match_3)
match_5=match_4.replace('$','')
match_6=match_5.replace('!','')
match_7=match_6.replace('?','')
match_8=match_7.replace('.','')
match_9=match_8.replace(',','')
match_10=match_9.replace(';','')

new_match_1=re.split(' ',match_10)
match_set=set()
for i in new_match_1:
    match_set.add(i)

final_list=[]
for each in match_set:
    val=new_match_1.count(each)
    val_dict={val:each}
    if val>1:
       final_list.append(val_dict)

print(final_list)

    

