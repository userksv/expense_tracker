class Record():
    '''
    Класс `Модель` для создания записи

    Переменные 
    --------------------
    __id: int
        Используется для номера записи
    __date: str
        Дата записи
    __category: str
        Категоря Расход\Доход 
    __amount: int
        Сумма
    description: str
        Краткое описание

    Методы:
    --------------------
    to_dict()
        Конвертирует объект в словарь
    '''
    def __init__(self, id: int, date: str, category: str, amount: int, description: str) -> None:
        self.__id = id
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__description = description

    def __str__(self) -> str:
        return f'{self.__date} - {self.__category} - {self.__amount} - {self.__description}'
    
    def to_dict(self):
        '''Простой serializer to json'''
        return {
            'id': self.__id,
            'date': self.__date,
            'category': self.__category,
            'amount': self.__amount,
            'description': self.__description
        }