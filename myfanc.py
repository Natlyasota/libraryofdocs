import pprint
def get_person_name():
    number = input('Введите номер документа ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером нет'


def get_shelf():
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return key
    return 'В полках документа с данным номером нет.'

def get_list(documents):
    for doc in documents:
      print (f"{doc['type']} {doc['number']} {doc['name']};")
    return 'Показаны все документы'


def add_doc():
    shelf = input('Введите номер полки куда положить документ. ')
    if shelf not in directories:
        return 'Нет такой полки'
    doc = {}
    for info in ('type', 'number', 'name'):
        doc[info] = input(f'{info}: ')
    print(doc)
    documents.append(doc)
    directories[shelf].append(doc['number'])
    return 'Документ добавлен'


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def forautput():
    while True:
        print('Возможные команды: p, s, l, a')
        print('для выходна нажмите "q"')
        command = input('Введите название команды ')
        # print('Возможные команды: p, s, l, a,', 'для выходна нажмите "q"')

        if command == 'p':
            print(get_person_name())

        elif command == 's':
            print(get_shelf())

        elif command == 'l':
            print(get_list(documents))

        elif command == 'a':
            print(add_doc())
            print(documents)
            print(directories)

        elif command == 'q':
            break
        else:
            print('Команды не существует')


if __name__ == "__main__":
    forautput()