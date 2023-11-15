# import csv
#
# name = 'vadim'
# surname = 'marushkevich'
#
# with open('123.csv',mode='w',encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         [name,surname]
#     )


# import csv
#
# name = 'vadim'
# surname = 'marushkevich'
# data_names = ['oleg','vera']
#
# with open('123.csv',mode='w',encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         # data_names
#         ("user_name","user_address")
#     )
#
# user_data = [
#     ["user1", "adress1"],
#     ["user1", "adress1"],
#     ["user1", "adress1"]
# ]
#
# for user in user_data:
#     with open('123.csv','a',encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             user
#         )

# import csv
#
# user_data = [
#     ("user_name", "user_address"),
#     ["user1", "adress1"],
#     ["user2", "adress2"],
#     ["user3", "adress3"]
# ]
#
# with open('123.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter=' ')
#     writer.writerows(
#         user_data
#     )
