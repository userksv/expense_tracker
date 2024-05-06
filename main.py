import json
from file_handler import FileHandler

class Record():
    '''Model'''
    def __init__(self, id: int, date: str, category: str, amount: int, description: str) -> None:
        self.__id = id
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__description = description

    def __str__(self) -> str:
        return f'{self.__date} - {self.__category} - {self.__amount} - {self.__description}'
    
    def to_dict(self):
        return {
            'id': self.__id,
            'date': self.__date,
            'category': self.__category,
            'amount': self.__amount,
            'description': self.__description
        }


class RecordsData():
    '''Model controller'''
    def __init__(self) -> None:
        self.__file_handler = FileHandler('data.json')
    
    def add_record(self, date: str, category: str, amount: int, description: str):
        id = len(self.__file_handler.read_file()['records']) + 1 # Создаем номер записи
        if category == 'Расход':
            amount = -amount
        record = Record(id, date, category, amount, description).to_dict()
        # Safe to the file
        self.__file_handler.write_to_file(record)
    
    def get_balance(self, balance_type: str):
        '''Возвращает баланс в зависимосит от выбранного типа баланса'''
        json_data = self.__file_handler.read_file()
        records = json_data['records']
   
        if balance_type == 'total_expenses':
            return abs(sum([record['amount'] for record in records if record['category'] == 'Расход']))
        elif balance_type == 'total_income':
            return sum([record['amount'] for record in records if record['category'] == 'Доход'])
        else:
            return sum([record['amount'] for record in records])

    def get_all_records(self):
        return self.__file_handler.read_file()['records']
    
    def find_record_by_id(self, record_number: int):
        records = self.__file_handler.read_file()['records']
        for record in records:
            if record['id'] == record_number:
                return record

    def edit_record(self, record: object, date: str, category: str, amount: int, description: str):
        record['date'] = date
        record['category'] = category
        record['amount'] = amount
        record['description'] = description
        records = self.__file_handler.read_file()['records']
        for entry in records:
            if entry['id'] == record['id']:
                entry_index = records.index(entry)              # index of record which will be updated
                records.pop(entry_index)                        # delete old record
                records.insert(entry_index, record)             # insert new record
        self.__file_handler.update_file({'records': records})   # rewrite file

    def search_by(self, search_condition: str | int):
        records = self.__file_handler.read_file()['records']
        return list(filter(lambda record: search_condition in record.values(), records))


class MainApp():
    '''View'''
    def __init__(self) -> None:
        self.records = RecordsData()
        self.separator = '-' * 25

    def help(self):
        print('Главное меню')
        print('1. Текущий баланс')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Поиск')
        print('5. Просмотреть все записи')
        print('0. Выход')
        print(self.separator)
    
    def print_balance(self):
        print('1. Общий баланс')
        print('2. Расходы')
        print('3. Доходы')
        print()
        command = input('Выберите команду: ')
        print()
        if command == '1':
            balance_type = 'total'
            output = 'Общий баланс'
        elif command == '2':
            balance_type = 'total_expenses'
            output = 'Общие расходы'
        elif command == '3':
            balance_type = 'total_income'
            output = 'Общие доходы'
        else:
            self.help()
            return
        print(f'{output}: {self.records.get_balance(balance_type)}')
        print(self.separator)

    
    def add_record(self):
        date = input('Введите дату(Год-Месяц-День): ')
        category = input('Введите категорию(Доход/Расход): ')
        amount = int(input('Введите сумму(Целое число): '))
        description = input('Введите описание: ')
        self.records.add_record(date, category, amount, description)
        print('Запись добавлена.')
        print()

    def get_all_records(self):
        return self.records.get_all_records()
    
    def print_records(self, records: list):
        print(records)
        if records == None:
            print('Нет записей.')
        print('Найденые записи:')
        print(self.separator)
        for record in records:
            print(f"Номер записи: {record['id']}\nДата: {record['date']}\nКатегория: {record['category']}\nСумма: {record['amount']}\nОписание: {record['description']}")
            print(self.separator)
    
    def edit_record(self):
        record_number = int(input('ВВедите номер записи для редактирования: '))
        record = self.records.find_record_by_id(record_number)
        if not record:
            print('Запись не найдена')
        else:
            print('Изменение записи: ')
            date = input('Введите дату(Год-Месяц-День): ')
            category = input('Введите категорию(Доход/Расход): ')
            amount = int(input('Введите сумму(Целое число): '))
            description = input('Введите описание: ')
            self.records.edit_record(record, date, category, amount, description)
            print('Изменения сохранены')

    def search(self):
        print('1. Поиск по дате')
        print('2. Поиск по категории')
        print('3. Поиск по сумме')
        command = input('Выберите команду: ')
        print()
        search_condition = ''
        if command == '1':
            search_condition = input('Введите дату записи(Год-Месяц-День): ')
        elif command == '2':
            search_condition = input('Введите категорию(Доход/Расход): ')
        elif command == '3':
            search_condition = int(input('Введите сумму(Целое число): '))
        # print(self.records.search_by(search_condition)) 
        return self.records.search_by(search_condition)
        
    def run(self):
        print('Добро пожаловать!')
        print(self.separator)
        while True:
            self.help()
            command = input('Выберите команду: ')
            print()
            if command == '0':
                print('Всего доброго!')
                break
            elif command == '1':
                self.print_balance()
            elif command == '2':
                self.add_record()
            elif command == '3':
                self.edit_record()
            elif command == '4':
                self.print_records(self.search())
            elif command == '5':
                self.print_records(self.get_all_records())
            else:
                self.help()

if __name__ == '__main__':
    app = MainApp()
    app.run()
    