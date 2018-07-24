import unittest
from view import View

class TestUM(unittest.TestCase):
    def test_start_stop_run(self):
        assert View.start_stop_run(self, 'text', 'date') == {'text':'date'}









# unittest.main()



