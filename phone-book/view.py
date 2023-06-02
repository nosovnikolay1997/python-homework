import text

def menu():
    for i, v in enumerate(text.menu, 1):
        print(str(i) + '. ' + v)
    while True:
        choice = input(text.menu_choice)
        if choice.isdigit() and 0 < int(choice) <= len(text.menu):
            return int(choice)

def print_entries(e):
    if e:
        width = 0
        for n, pn, c in e:
            width = max(
                    width,
                    len(text.name) + len(n),
                    len(text.phone_number) + len(pn),
                    len(text.comment) + len(c)
                    )
        print('=' * width)
        i = 1
        for n, pn, c in e:
            if i > 1:
                print()
            print(str(i) + '.')
            print(text.name + n)
            print(text.phone_number + pn)
            print(text.comment + c)
            i += 1
        print('=' * width)

def print_message(message):
    print('=' * len(message))
    print(message)
    print('=' * len(message))

def input_entry():
    return (input(text.name), input(text.phone_number), input(text.comment))

def input_int(prompt) -> int:
    while True:
        inp = input(prompt)
        if inp.isdigit():
            return int(inp)
