import unittest
from Api import Api

class TestGetTopN(unittest.TestCase):
    def setUp(self):
        api = Api()
        self.app = api.app.test_client()

    def test_valid_topN(self):
        # Test for a valid topN value (within the range 1 to 100)
        response = self.app.get('/topN/50')
        response_data = response.data.decode('utf-8')
        doc_list = response_data.split(",")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(doc_list), 50)

    def test_lower_bound(self):
        # Test for the lower bound (topN = 1)
        response = self.app.get('/topN/1')
        response_data = response.data.decode('utf-8')
        doc_list = response_data.split(",")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(doc_list), 1)

    def test_upper_bound(self):
        # Test for the upper bound (topN = 100)
        response = self.app.get('/topN/100')
        response_data = response.data.decode('utf-8')
        doc_list = response_data.split(",")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(doc_list), 100)

    def test_out_of_range(self):
        # Test for an out-of-range topN value (topN < 1)
        response = self.app.get('/topN/0')
        self.assertEqual(response.status_code, 400)

        # Test for an out-of-range topN value (topN > 100)
        response = self.app.get('/topN/101')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
