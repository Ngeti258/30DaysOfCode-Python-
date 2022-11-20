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
        print(f'#{each}')
       
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
    combined_characters=string.ascii_letters[0:6] + string.digits
    character_array=[]
    character=[]
    while len(character_array)<6:
        while len(character)<7:
            character.append(random.choice(combined_characters))
        to_be_appended=''.join(character)
        character_array.append(f'#{to_be_appended}')
        for i in character:
            character.remove(i)
    return character_array
print(list_of_hexa())

def list_of_rgb_colors():
    from random import randint
    list_of_colors=[]
    colors=[]
    while len(list_of_colors)<7:
        while len(colors)<3:
           colors.append(randint(000,255))
        list_of_colors.append(f'rgb{colors}')
        for i in colors:
            colors.remove(i)
    return list_of_colors
print(list_of_rgb_colors())


def generate_colors(type,number):
    if type == 'hexa':
        import string
        import random
        combined_characters=string.ascii_letters[0:6] + string.digits
        character_array=[]
        character=[]
        while len(character_array)<number:
            while len(character)<7:
                character.append(random.choice(combined_characters))
            to_be_appended=''.join(character)
            character_array.append(f'#{to_be_appended}')
            for i in character:
               character.remove(i)
        return character_array
    elif type == 'rgb':
        from random import randint
        list_of_colors=[]
        colors=[]
        while len(list_of_colors)<number:
            while len(colors)<3:
                colors.append(randint(000,255))
            list_of_colors.append(f'rgb{colors}')
            for i in colors:
                colors.remove(i)
            
        return list_of_colors
print(generate_colors('hexa',4))

def shuffle_list(*list):
    import random
    shuffled=set()
    while len(shuffled)<len(list):
        shuffled.add(random.choice(list))
    return shuffled
print(shuffle_list('hello','my','name','is','Gabriel'))

def seven_random_numbers():
    import string
    import random
    random_set=set()
    numberlist=string.digits
    while len(random_set)<7:
        random_set.add(random.choice(numberlist))       
    return random_set
print(seven_random_numbers())

 