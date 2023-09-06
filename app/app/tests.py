from django.test import SimpleTestCase
from app import calc


class TestModule(SimpleTestCase):
    def test_calc(self):
        res = calc.add_numbers(4, 6)
        self.assertEqual(res, 10)
