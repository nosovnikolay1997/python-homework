import view
import model
import text
import sys

def start():
    pb = model.PhoneBook()
    while True:
        choice = view.menu()
        match choice:
            case 1:
                book = pb.get_book()
                view.print_entries(book)
            case 2:
                query = input(text.query)
                entries = pb.search(query)
                view.print_entries(entries)
            case 3:
                pb.add(view.input_entry())
                view.print_message(text.add_success)
            case 4:
                index = view.input_int(text.index) - 1
                entry = view.input_entry()
                if pb.update(index, entry):
                    view.print_message(text.update_success)
                else:
                    view.print_message(text.update_fail)
            case 5:
                index = view.input_int(text.index) - 1
                if pb.remove(index):
                    view.print_message(text.remove_success)
                else:
                    view.print_message(text.remove_fail)
            case 6:
                pb.save()
                sys.exit()
            case 7:
                sys.exit()
