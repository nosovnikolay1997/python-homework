class PhoneBook:
    default_path = 'phonebook.txt'

    def __init__(self, path: str = default_path):
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                lines = [l.strip() for l in file.readlines()]
                self.book = list(zip(lines[0::3], lines[1::3], lines[2::3]))
        except:
            self.book = list()

    def save(self, path: str = default_path):
        with open(path, 'w', encoding='UTF-8') as file:
            for entry in self.book:
                for i in entry:
                    file.write(i + '\n')

    def get_book(self):
        return self.book

    def search(self, query):
        result = list()
        for item in self.book:
            if query.lower() in ''.join(item).lower():
                result.append(item)
        return result

    def add(self, entry):
        self.book.append(entry)

    def update(self, i, entry):
        if 0 <= i < len(self.book):
            self.book[i] = entry
            return True
        return False

    def remove(self, i):
        if 0 <= i < len(self.book):
            self.book.pop(i)
            return True
        return False
