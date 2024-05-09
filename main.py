from controller import RecordsData
from validators import Validator


class MainApp():
    '''
    Класс `View` консольный интерфейс приложения, вывод информации на экран

    Переменные
    --------------------
    records: RecordsData
        Исполозуется для доступа к контроллеру 
    separator: str
        Печать линни
    validator: Validator
        Используется для валидации введенных данных пользователем
    '''

    def __init__(self) -> None:
        self.records = RecordsData()
        self.separator = '-' * 25
        self.validator = Validator()

    def help(self):
        '''Метод для отображения основного меню приложения'''
        print('Главное меню')
        print('1. Текущий баланс')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Поиск')
        print('5. Просмотреть все записи')
        print('0. Выход')
        print(self.separator)
    
    def print_balance(self):
        '''
        Медот для отображения выбранного типа баланса
        В зависимости от выбора пользователем
        balance_type: str 
            присваивается выбранное значиние и вызывется метод контролллера `records` get_balance
            далее данные выводятся на экран
        '''
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
        '''
        Медот добавлет запись.
        Если введные данные пользователем валидны. вызывается метод котероллера `records` add_record
        '''
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
        '''Вывод ошибок на экран'''
        print(self.separator)
        print('Ошибки при вводе данных.')
        print(self.separator)
        for erroor in errors:
            print(erroor)
        print()

    def get_all_records(self):
        '''Получение всех записей'''
        return self.records.get_all_records()
    
    def print_records(self, records: list):
        '''Вывод записей на экран'''
        if not records:
            print('Нет записей.')
            print(self.separator)
            return
        else:
            print('Найденые записи:')
            print(self.separator)
            for record in records:
                # Формируем строку для выводв
                print(f"Номер записи: {record['id']}\nДата: {record['date']}\nКатегория: {record['category']}\nСумма: {record['amount']}\nОписание: {record['description']}")
                print(self.separator)
    
    def edit_record(self):
        '''
        Метод для редактирования записи
        Если запись найдена и введеные данные валидны, то вызывется метод контроллера `records` edit_record
        '''
        try:
            record_number = int(input('Введите номер записи для редактирования: '))
        except ValueError:
            print('Номер должен быть целое число')
            print(self.separator)
            return
        # Поиск записи
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
        '''
        Метод для поиска записи от выбранного параметра
        Если введеные данные валидны, вызывается метод контроллера `records` serach_by
        '''
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
        '''Запуск приложения'''
        print('Добро пожаловать!')
        print(self.separator)
        while True:
            self.validator.clear_errors() # Обнуляем ошибки
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
    