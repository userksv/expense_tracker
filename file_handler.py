import json
import os

class FileHandler():
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        # Создаем структуру файла, если его нет
        if not os.path.exists(self.__filename):
            with open(self.__filename, 'w') as file:
                json.dump({"records":[]}, file, indent=2)

    def write_to_file(self, record:dict):
        json_data = self.read_file()            # loading json file as dictionary
        json_data['records'].append(record)     
    
        with open(self.__filename, 'w') as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)
        
    def read_file(self):
        '''Return json file'''
        with open(self.__filename, 'r') as file:
            json_data = json.load(file)
        return json_data



# f = FileHandler('data.json')
# f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 3000, 'description': 'Покупка продуктов'})
# f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 234, 'description': 'Покупка продуктов'})
# f.write_to_file({'date': '2024-05-03', 'category':'Расход','amount': 500, 'description': 'Покупка продуктов'})
# # print(f.balance())