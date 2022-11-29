import numpy
lst=[1,2,3,4,5]
np_arr=numpy.array(lst)
print(np_arr+2)

import webbrowser # web browser module to open websites

# list of urls: python
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

import requests
url:'https://twitter.com/'
response=requests.get(url)
print(response)