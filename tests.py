import unittest

from model import Record
from controller import RecordsData
from main import MainApp
from unittest.mock import patch, MagicMock


class TestModel(unittest.TestCase):
    def test_is_record(self):
        record = Record(1, '2024-05-05', 'Income', 3000, 'Salary')
        self.assertIsInstance(record, Record)

    def test_to_dict(self):
        record = Record(1, '2024-05-05', 'Income', 3000, 'Salary')
        exp = {'id': 1, 'date': '2024-05-05', 'category': 'Income', 'amount': 3000, 'description': 'Salary'}
        self.assertDictEqual(exp, record.to_dict())


class TestRecordController(unittest.TestCase):

    def test_get_balance_total_expenses(self):
        # Mocking the return value of read_file method
        mock_file_handler = MagicMock()
        mock_file_handler.read_file.return_value = {
            'records': [
                {'category': 'Расход', 'amount': 10},
                {'category': 'Расход', 'amount': 20},
                {'category': 'Доход', 'amount': 30},
            ]
        }
        records_data = RecordsData()
        records_data._RecordsData__file_handler = mock_file_handler  # Injecting the mock file handler
        balance = records_data.get_balance('total_expenses')
        self.assertEqual(balance, 30)  # Sum of absolute values of 'Расход' category
    
    def test_get_balance_total_income(self):
        # Mocking the return value of read_file method
        mock_file_handler = MagicMock()
        mock_file_handler.read_file.return_value = {
            'records': [
                {'category': 'Расход', 'amount': 10},
                {'category': 'Расход', 'amount': 20},
                {'category': 'Доход', 'amount': 30},
            ]
        }
        records_data = RecordsData()
        records_data._RecordsData__file_handler = mock_file_handler  # Injecting the mock file handler
        balance = records_data.get_balance('total_income')
        self.assertEqual(balance, 30)  # Sum of absolute values of 'Расход' category
    
    def test_get_balance_total_balance(self):
        # Mocking the return value of read_file method
        mock_file_handler = MagicMock()
        mock_file_handler.read_file.return_value = {
            'records': [
                {'category': 'Расход', 'amount': 10},
                {'category': 'Расход', 'amount': 20},
                {'category': 'Доход', 'amount': 30},
            ]
        }
        records_data = RecordsData()
        records_data._RecordsData__file_handler = mock_file_handler  # Injecting the mock file handler
        balance = records_data.get_balance('total')
        self.assertEqual(balance, 0)  # Sum of absolute values of 'Расход' category

    @patch('file_handler.FileHandler.write_to_file')
    def test_add_record(self, mock_write_to_file):

        mock_write_to_file.return_value = True

        records = RecordsData()
        result = records.add_record('2024-05-08', 'Расход', 100, 'Some description')
        self.assertTrue(result)

    @patch('file_handler.FileHandler.read_file')
    def test_get_all_records(self, mock_read_file):
        mock_read_file.return_value = {'records': [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}]}
        records = RecordsData()
        result = records.get_all_records()
        self.assertEqual(result, [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}])

    @patch('file_handler.FileHandler.read_file')
    def test_find_record_by_id(self, mock_read_file):
        mock_read_file.return_value = {'records': [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}]}
        records = RecordsData()
        result = records.find_record_by_id(1)
        self.assertEqual(result, {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'})

        result = records.find_record_by_id(2)
        self.assertFalse(result, False)

    # if there is mulptiple mock objects, queue is matters
    @patch('file_handler.FileHandler.update_file') 
    @patch('file_handler.FileHandler.read_file')
    def test_edit_record(self, mock_read_file, mock_update_file):
        mock_read_file.return_value = {'records': [
            {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'},
            {'id': 2, 'date': '2024-05-09', 'category': 'Расход', 'amount': 200, 'description': 'Some'}
        ]}
        record = {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}
        mock_update_file.return_value = True
        records = RecordsData()
        result = records.edit_record(record, '2024-05-09', 'Расход', 300, 'Some')
        self.assertTrue(result)

    @patch('file_handler.FileHandler.read_file')
    def test_search_by_date(self, mock_read_file):       # Поиск по дате
        mock_read_file.return_value = {'records': [
            {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'},
        ]}
        records = RecordsData()
        result = records.search_by('2024-05-08')
        self.assertEqual(result, [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}])
    
        result = records.search_by('2024-05-01')        # Ничего не найдено
        self.assertEqual(result, [])
    
    @patch('file_handler.FileHandler.read_file')
    def test_search_by_amount(self, mock_read_file):       # Поиск по сумме
        mock_read_file.return_value = {'records': [
            {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'},
        ]}
        records = RecordsData()
        result = records.search_by(100)
        self.assertEqual(result, [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}])
        
        result = records.search_by(10000)
        self.assertEqual(result, [])                    # Ничего не найдено
    
    @patch('file_handler.FileHandler.read_file')
    def test_search_by_category(self, mock_read_file):       # Поиск по категории
        mock_read_file.return_value = {'records': [
            {'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'},
        ]}
        records = RecordsData()
        result = records.search_by('Расход')
        self.assertEqual(result, [{'id': 1, 'date': '2024-05-08', 'category': 'Расход', 'amount': 100, 'description': 'Some description'}])

        result = records.search_by('Доход')
        self.assertEqual(result, [])                    # Ничего не найдено


if __name__ == '__main__':
    unittest.main()