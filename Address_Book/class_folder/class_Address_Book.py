from collections import UserDict
from ..class_folder.class_Record import Record
    
class Iterator:
    def __init__(self, records) -> None:
        self.records = records
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.records):
            raise StopIteration
        record = self.records[self.index]
        self.index += 1
        return record

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def get_records(self, name: str) -> Record:
        return self.data[name]
    
    def __str__(self) -> str:
        print({self.data})

    def __iter__(self):
        return Iterator(list(self.data.values()))

    def paginate(self, page_size: int):
        records = list(self.data.values())
        total_records = len(records)
        num_pages = (total_records + page_size - 1) // page_size

        for page in range(num_pages):
            start_index = page * page_size
            end_index = (page + 1) * page_size
            yield [(record.name.value, record) for record in records[start_index:end_index]]