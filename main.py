from controller import RecordsData
from validators import Validator
class MainApp():
    '''View'''
    def __init__(self) -> None:
        self.records = RecordsData()
        self.separator = '-' * 25
        self.validator = Validator()

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
        amount = input('Введите сумму(Целое число): ')
        description = input('Введите описание: ')
        if self.validator.validate_data(date, amount, category):
            self.records.add_record(date, category, int(amount), description)
            print('Запись добавлена.')
            print()
        else:
            self.print_errors(self.validator.errors())
            return

    def print_errors(self, errors: list):
        print(self.separator)
        print('Ошибки при вводе данных.')
        print(self.separator)
        for erroor in errors:
            print(erroor)
        print()

    def get_all_records(self):
        return self.records.get_all_records()
    
    def print_records(self, records: list):
        if not records:
            print('Нет записей.')
            print(self.separator)
            return
        else:
            print('Найденые записи:')
            print(self.separator)
            for record in records:
                print(f"Номер записи: {record['id']}\nДата: {record['date']}\nКатегория: {record['category']}\nСумма: {record['amount']}\nОписание: {record['description']}")
                print(self.separator)
    
    def edit_record(self):
        try:
            record_number = int(input('Введите номер записи для редактирования: '))
        except ValueError:
            print('Номер должен быть целое число')
            print(self.separator)
            return
        
        record = self.records.find_record_by_id(record_number)
        if not record:
            print('Запись не найдена')
            print(self.separator)
        else:
            print('Изменение записи: ')
            date = input('Введите дату(Год-Месяц-День): ')
            category = input('Введите категорию(Доход/Расход): ')
            amount = input('Введите сумму(Целое число): ')
            description = input('Введите описание: ')
            if self.validator.validate_data(date, amount, category):
                self.records.edit_record(record, date, category, int(amount), description)
                print('Изменения сохранены!')
                print()
            else:
                self.print_errors(self.validator.errors())
                return

    def search(self):
        print('1. Поиск по дате')
        print('2. Поиск по категории')
        print('3. Поиск по сумме')
        command = input('Выберите команду: ')
        print()
        search_condition = ''
        if command == '1':
            search_condition = input('Введите дату записи(Год-Месяц-День): ')
            valid = self.validator.validate_date(search_condition)
        elif command == '2':
            search_condition = input('Введите категорию(Доход/Расход): ')
            valid = self.validator.validate_category(search_condition)
        elif command == '3':
            search_condition = input('Введите сумму(Целое число): ')
            if valid := self.validator.validate_number(search_condition):
                search_condition = int(search_condition)
        else: 
            return
        if valid:
            self.print_records(self.records.search_by(search_condition))
        else:
            self.print_errors(self.validator.errors())

    def run(self):
        print('Добро пожаловать!')
        print(self.separator)
        while True:
            self.validator.clear_errors()
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
                self.search()
            elif command == '5':
                self.print_records(self.get_all_records())
            else:
                self.help()

if __name__ == '__main__':
    app = MainApp()
    app.run()
    