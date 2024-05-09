from model import Record
from file_handler import FileHandler


class RecordsData():
    '''
    Класс `controller` для обработки данных из файла

    Переменные 
    --------------------
    __file_handler: FileHandler
        Для доступа к файлу
    '''
    def __init__(self) -> None:
        # Инициализируем переменную и создаем файл если не существует
        self.__file_handler = FileHandler('records.json') 
    
    def add_record(self, date: str, category: str, amount: int, description: str):
        '''Метод создает новую запись'''
        id = len(self.__file_handler.read_file()['records']) + 1 # Создаем номер записи
        record = Record(id, date, category, amount, description).to_dict()
        try:
            self.__file_handler.write_to_file(record)
            return True
        except:
            return False
    
    def get_balance(self, balance_type: str):
        '''Возвращает баланс в зависимосит от выбранного типа баланса'''
        records = self.__file_handler.read_file()['records']
   
        if balance_type == 'total_expenses':
            return abs(sum([-record['amount'] for record in records if record['category'] == 'Расход']))
        elif balance_type == 'total_income':
            return sum([record['amount'] for record in records if record['category'] == 'Доход'])
        else:
            # Если категория `Расход` то меняем знак `суммы` на минус
            return sum([-record['amount'] if record['category'] == 'Расход' else record['amount'] for record in records])

    def get_all_records(self):
        return self.__file_handler.read_file()['records']
    
    def find_record_by_id(self, record_number: int):
        records = self.__file_handler.read_file()['records']
        for record in records:
            if record['id'] == record_number:
                return record

    def edit_record(self, record: object, date: str, category: str, amount: int, description: str):
        '''
        Метод для редактирования записи. Запись редактируется полностью и обновляется файл
        '''
        record['date'] = date
        record['category'] = category
        record['amount'] = amount
        record['description'] = description
        records = self.__file_handler.read_file()['records']
        for entry in records:
            if entry['id'] == record['id']:
                entry_index = records.index(entry)              # находим индекс записи
                records.pop(entry_index)                        # Удаляем старую запись
                records.insert(entry_index, record)             # Вставлем новую запись по индексу удаленной записи
        self.__file_handler.update_file({'records': records})   
        return True

    def search_by(self, search_condition: str | int):
        '''
        Метод для поиска записей по переданному параметру
        Используется list comprehension
        '''
        records = self.__file_handler.read_file()['records']
        return list(filter(lambda record: search_condition in record.values(), records))
