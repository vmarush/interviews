import requests

response = requests.get(url="https://www.balldontlie.io/api/v1/teams")
response_list_all = response.json()

def search_by_attribute():
    for x in response_list_all["data"]:
        print(x["abbreviation"], x["full_name"])
    cur = input("введите абривиатуру  команды").upper()
    for j in response_list_all["data"]:
        if j["abbreviation"] == cur:
            print(
                f'id = {j["id"]}, город = {j["city"]}, ассоциация = {j["conference"]},'
                f' полное название = {j["full_name"]}, коротное название = {j["name"]}')




def search_by_city():
    for x in response_list_all["data"]:
        print(x["conference"])
    cur = input("введите асоциацию  команды").capitalize()
    for j in response_list_all["data"]:
        if j["conference"] == cur:
            print(
                f'id = {j["id"]}, абривиатура = {j["abbreviation"]}, город = {j["city"]},'
                f' полное название = {j["full_name"]}, коротное название = {j["name"]}')


def search_by_name():
    for x in response_list_all["data"]:
        print(x["name"])
    cur = input("введите короткое имя  команды").capitalize()
    for j in response_list_all["data"]:
        if j["name"] == cur:
            print(
                f'id = {j["id"]}, абривиатура = {j["abbreviation"]}, город = {j["city"]},'
                f' полное название = {j["full_name"]}')

def menu():
    print(f'поиск по абривиатуре =  1 ',
          f'поиск по асоциации =  2',
          f'поиск по короткому названию =  3')

    try:
        menu1 = int(input("введите число"))
        d = {1: search_by_attribute,
             2: search_by_city,
             3: search_by_name}
        print(d[menu1]())
    except KeyError:
        print('введите число от 1 до 3')
    except ValueError:
        print('введено не число')
menu()

cur = input("введите абривиатуру  команды или  асоциацию или короткое имя")
for j in response_list_all["data"]:
    if j["abbreviation"] == cur or j["conference"] == cur or j["name"] == cur:
        print(
            f'id = {j["id"]},абривиатура = {j["abbreviation"]},'
            f' город = {j["city"]}, ассоциация = {j["conference"]},'
            f' полное название = {j["full_name"]}, коротное название = {j["name"]}')


