import json
import os

class FileHandler():
    '''
    Класс для взаимодействия с файлом

    Переменные
    --------------------
    __filename: str(path)
        путь к файлу
    
    '''
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        # Создаем файл и структуру внутри файла, если его нет
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w') as file:
                json.dump({"records":[]}, file, indent=2)

    def write_to_file(self, record:dict):
        '''Метод обновляет файл новой записью `record` путем обновления всего файла'''
        json_data = self.read_file()            # Читаем файл
        json_data['records'].append(record)     # Добавляем новую запись в list

        # полное обновление файла актуальными данными
        with open(self.__filename, 'w') as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)
    
    def read_file(self):
        '''Медот читает файл и возвращает словарь'''
        with open(self.__filename, 'r') as file:
            json_data = json.load(file)
        return json_data
        
    def update_file(self, records: list):
        '''Метод обновляет файл полностью актуальными данными `records`'''
        with open(self.__filename, 'w') as file:
            json.dump(records, file, indent=2, ensure_ascii=False)