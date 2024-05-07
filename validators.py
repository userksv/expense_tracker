from datetime import datetime
class Validator():
    def __init__(self) -> None:
        self.__errors = []
    
    def validate_number(self, value: any):
        if not value.isdigit():
            self.__errors.append('Недопустимое значение суммы, пример (Целое число)')
            return False
        else: 
            return True
    
    def errors(self):
        return self.__errors
    
    def clear_errors(self):
        self.__errors = []
        
    def validate_date(self, value: any):
        format = "%Y-%m-%d"
        try:
            datetime.strptime(value, format)
        except ValueError:
            self.__errors.append('Недопустимый формат даты, пример (Год-Месяц-День)')
            return False
        return True

    def validate_category(self, value: any):
        if value.lower() not in ['доход', 'расход']:
            self.__errors.append('Неверный формат данных, пример (Доход/Расход)')
            return False
        return True
        
    def validate_data(self, date: any, amount: any, category: any):
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


if __name__ == '__main__':
    v = Validator()
    valid = v.validate_number('34')
    print(v.errors())