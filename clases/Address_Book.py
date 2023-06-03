from collections import UserDict
import pickle

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print("Файл не знайдено. Нова адресна книга створена.")

    def search(self, search_query):
        search_results = []
        for record in self.data.values():
            if search_query in record.name.value or any(search_query in phone.value for phone in record.phones):
                search_results.append(record)
        return search_results