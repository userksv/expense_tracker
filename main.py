import json
from file_handler import FileHandler

class Record():
    '''Model'''
    def __init__(self, date: str, category: str, amount: int, description: str) -> None:
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__description = description

    def __str__(self) -> str:
        return f'{self.__date} - {self.__category} - {self.__amount} - {self.__description}'
    
    def to_dict(self):
        return {
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
        record = Record(date, category, amount, description).to_dict()
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

# r = RecordsData()
# print(r.get_balance('total_expenses'))
# print(r.get_balance('total_income'))
# print(r.get_balance('total'))



class MainApp():
    '''View'''
    def __init__(self) -> None:
        self.records = RecordsData()

    def help(self):
        print()
        print('1. Текущий баланс')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Поиск')
        print('0. Выход')
    
    def print_balance(self):
        print()
        print('1. Общий баланс')
        print('2. Расходы')
        print('3. Доходы')
        command = input('Выберите комманду: ')
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
        print(f'{output} - {self.records.get_balance(balance_type)}')
    
    def add_record(self):
        date = input('Введите дату(Год-Месяц-День): ')
        category = input('Введите категорию(Доход/Расход): ')
        amount = int(input('Введите сумму(Целое число): '))
        description = input('Введите описание: ')
        self.records.add_record(date, category, amount, description)
        print('Запись добавлена.')

    def edit_record(self):
        description = input('Введите описание: ???')
    
    def search(self):
        print('1. Поиск по дате')
        print('2. Поиск по категории')
        print('3. Поиск по сумме')

    def run(self):
        print('Добро пожаловать!')
        self.help()
        while True:
            print()
            command = input('Выберите комманду: ')
            if command == '0':
                break
            elif command == '1':
                self.print_balance()
            elif command == '2':
                self.add_record()
            else:
                self.help()


app = MainApp()
app.run()
# records = RecordsData()
# records.add_record('2024-05-03', 'Расход', 500, 'Покупка продуктов')
# records.add_record('2024-05-03', 'Доход', 3000, 'Зарплата')