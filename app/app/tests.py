from django.test import SimpleTestCase
from app import calc


class TestModule(SimpleTestCase):
    def test_calc(self):
        res = calc.add_numbers(4, 6)
        self.assertEqual(res, 10)

    def test_subtr(self):
        res = calc.subtr(4, 6)
        self.assertEqual(res, -2)
