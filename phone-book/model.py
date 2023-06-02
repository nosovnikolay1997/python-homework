book = list()
path = 'phonebook.txt'

def load():
    global book, path
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            lines = [l.strip() for l in file.readlines()]
            book = list(zip(lines[0::3], lines[1::3], lines[2::3]))
    except:
        pass

def save():
    global book, path
    with open(path, 'w', encoding='UTF-8') as file:
        for entry in book:
            for i in entry:
                file.write(i + '\n')

def get_book():
    return book

def search(query):
    result = list()
    for item in book:
        if query.lower() in ''.join(item).lower():
            result.append(item)
    return result

def add(entry):
    book.append(entry)

def update(i, entry):
    if 0 <= i < len(book):
        book[i] = entry
        return True
    return False

def remove(i):
    if 0 <= i < len(book):
        book.pop(i)
        return True
    return False
