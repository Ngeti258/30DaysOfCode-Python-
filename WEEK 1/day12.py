def random_user_id():
    import string
    import random
    characters=string.ascii_letters+string.digits
    user_id=[]
    while len(user_id)<6:
        user_id.append(random.choice(characters))
    return ''.join(user_id)
print(random_user_id())

def user_id_gen_by_user():
    number_of_characters=int(input('Enter the number of characters: '))
    number_of_ids=int(input('Enter the number of IDs: '))
    import string
    import random
    characters=string.ascii_letters+string.digits
    loop_times=[]
    while len(loop_times)<number_of_ids:
        user_id=[]
        while len(user_id)<number_of_characters:
           user_id.append(random.choice(characters))           
        joined= ''.join(user_id)
        loop_times.append(joined)
        # while len(user_id)>0:
        #     user_id.pop()
    for each in loop_times:
        print(each)
       
# (user_id_gen_by_user())

def rgb_color_gen():
    from random import randint
    color_array=[]
    while len(color_array)<3:
        color_array.append(randint(000,255))
    return f'rgb{color_array}'
print(rgb_color_gen())


def list_of_hexa():
    import string
    import random
    first_seven=[]
    for i in string.ascii_letters:
        first_seven.append(i)
    joined_to_f= ''.join(first_seven[0:6])
    total_combination=joined_to_f+string.digits
    random_characters=[]
    while len(random_characters)<7:
       random_characters.append(random.choice(total_combination))
       joined_random=''.join(random_characters)
    return f'#{joined_random}'
print(list_of_hexa())

def list_of_rgb_colors():
    from random import randint
    unlimited_colors=[]
    color_array=[]    
    while len(unlimited_colors)<7:
        while len(color_array)<3:
           color_array.append(randint(000,255))
           color=f'rgb{color_array}'
        unlimited_colors.append(color)
    return unlimited_colors
print(list_of_rgb_colors())




    
