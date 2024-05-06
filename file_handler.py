import json
import os

class FileHandler():
    '''Класс для взаимодействия с файлом.'''
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        # Создаем структуру файла, если его нет
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w') as file:
                json.dump({"records":[]}, file, indent=2)

    def write_to_file(self, record:dict):
        '''Метод обновляет файл новой записью `record` путем обновления всего файла'''
        json_data = self.read_file()            # loading json file as dictionary
        json_data['records'].append(record)     # Добавляем новую запись в list
        id = len(json_data['records']) + 1      # формируем id для новой записи

        # полное обновление файла актуальными данными
        with open(self.__filename, 'w') as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)
    
    def read_file(self):
        '''Медот читает файл и выгружает данные в `list`.'''
        with open(self.__filename, 'r') as file:
            json_data = json.load(file)
        return json_data
        
    def update_file(self, records: list):
        '''Метод обновляет файл полностью актуальными данными `records`'''
        with open(self.__filename, 'w') as file:
            json.dump(records, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    f = FileHandler('data.json')
    records = f.read_file()['records']
    # filtered = list(filter(lambda record: record['category'] == 'Доход', records))
    # print(sum([record['amount'] for record in filtered]))
    # print({'amount': 3000} in records[0])
    # print('Расход' in records[0].values())
    # print(list(filter(lambda record: 'Расход' in record.values(), records)))
    
    # print(len(f.read_file()['records']))
    # f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 3000, 'description': 'Покупка продуктов'})
    # f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 234, 'description': 'Покупка продуктов'})
    # f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 500, 'description': 'Покупка продуктов'})
    # # print(f.balance())