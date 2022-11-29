# # with open('C:\\Users\\GABU\\Desktop\\notes.txt','a') as f:
# #     hello=f.write('This text has to be appended at the end')


# import json
# person={
#     'name':'Gabriel',
#     'country':'Kenya',
#     'city':'Machakos',
#     'skills':['Python','React','Javascript']
# }
# with open('C:\\Users\\GABU\\Desktop\\json_example.json','w',encoding='utf-8') as f:
#     json.dump(person,f,ensure_ascii=False,indent=4)


# import csv
# with open('C:\\Users\\GABU\\Desktop\\csv_example.csv') as f:
#     csv_reader = csv.reader(f,delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teacher. He lives in {row[1]},{row[2]}.')
#             line_count += 1
#     print(f'Number of lines: {line_count}')


