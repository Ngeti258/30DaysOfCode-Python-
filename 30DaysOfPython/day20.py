# import numpy
# lst=[1,2,3,4,5]
# np_arr=numpy.array(lst)
# print(np_arr+2)

# import webbrowser # web browser module to open websites

# # list of urls: python
# # url_lists = [
# #     'http://www.python.org',
# #     'https://www.linkedin.com/in/asabeneh/',
# #     'https://github.com/Asabeneh',
# #     'https://twitter.com/Asabeneh',
# # ]

# # # opens the above list of websites in a different tab
# # for url in url_lists:
# #     webbrowser.open_new_tab(url)

# import requests
# import re
# url='http://www.gutenberg.org/files/1112/1112.txt'
# response=requests.get(url)
# paragraph=response.text
# new_paragraph=re.sub(pattern='[^\w\s]',repl='',string= paragraph)
# new_paragraph_1=re.split(' ',new_paragraph)
# wordset=set()
# for i in new_paragraph_1:
#     wordset.add(i)
# final_result=[]
# for each in wordset:
#     value=new_paragraph.count(each)
#     new_dict={value:each}
#     final_result.append(new_dict)
# for each in final_result:
#     print(each)

import requests
url='https://api.thecatapi.com/v1/breeds'
response=requests.get(url)
paragraph=response.text