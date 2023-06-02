import view
import model
import text
import sys

def start():
    model.load()
    while True:
        choice = view.menu()
        match choice:
            case 1:
                book = model.get_book()
                view.print_entries(book)
            case 2:
                query = input(text.query)
                entries = model.search(query)
                view.print_entries(entries)
            case 3:
                model.add(view.input_entry())
                view.print_message(text.add_success)
            case 4:
                index = view.input_int(text.index) - 1
                entry = view.input_entry()
                if model.update(index, entry):
                    view.print_message(text.update_success)
                else:
                    view.print_message(text.update_fail)
            case 5:
                index = view.input_int(text.index) - 1
                if model.remove(index):
                    view.print_message(text.remove_success)
                else:
                    view.print_message(text.remove_fail)
            case 6:
                model.save()
                sys.exit()
            case 7:
                sys.exit()
