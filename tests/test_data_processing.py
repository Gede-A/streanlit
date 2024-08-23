import unittest
from app.utils import fetch_data, process_data

class TestDataProcessing(unittest.TestCase):

    def test_fetch_data(self):
        data = fetch_data()
        self.assertFalse(data.empty)

    def test_process_data(self):
        data = fetch_data()
        processed_data = process_data(data)
        self.assertTrue('processed_column' in processed_data.columns)

if __name__ == '__main__':
    unittest.main()
