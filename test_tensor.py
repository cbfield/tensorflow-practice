import unittest

import tensor


class TestTensor(unittest.TestCase):
    """Test Cases for tensor.py"""

    def test_healthcheck(self):
        check = tensor.healthcheck()
        self.assertIsInstance(check,dict)
        self.assertTrue('statusCode' in check.keys())
        self.assertTrue('message' in check.keys())
        self.assertEqual(check['statusCode'],200)
        self.assertEqual(check['message'],'200 OK')


if __name__ == '__main__':
    unittest.main(verbosity=2)
