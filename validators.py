from datetime import datetime
class Validator():
    '''
    Класс для валидации введенных пользователем данных

    Переменные
    -----------------
    __errors: list
        Хранение ошибок
    '''
    def __init__(self) -> None:
        self.__errors = []
    
    def validate_number(self, value: any):
        '''Метод проверят значение `value` '''
        if not value.isdigit():
            self.__errors.append('Недопустимое значение суммы, пример (Целое число)')
            return False
        else: 
            return True
    
    def errors(self):
        '''Доступ к приветной переменной'''
        return self.__errors
    
    def clear_errors(self):
        self.__errors = []
        
    def validate_date(self, value: any):
        '''Метод для валидации формата даты. Используется datiteme module'''
        format = "%Y-%m-%d"
        try:
            datetime.strptime(value, format)
        except ValueError:
            self.__errors.append('Недопустимый формат даты, пример (Год-Месяц-День)')
            return False
        return True

    def validate_category(self, value: any):
        '''Метод для валидации категории'''
        if value.lower() not in ['доход', 'расход']:
            self.__errors.append('Неверный формат данных, пример (Доход/Расход)')
            return False
        return True
        
    def validate_data(self, date: any, amount: any, category: any):
        '''Метод для валидации введенных данных'''
        format = "%Y-%m-%d"

        if not amount.isdigit():
            self.__errors.append('Недопустимое значение `суммы`, пример (Целое число)')
    
        if category.lower() not in ['доход', 'расход']:
            self.__errors.append('Неверный формат `категория`, пример (Доход/Расход)')
        
        try:
            datetime.strptime(date, format)
        except ValueError:
            self.__errors.append('Недопустимый формат `даты`, пример (Год-Месяц-День)')
        
        if self.__errors:
            return False
        else: return True
