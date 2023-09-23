import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 7) == 35

    def test_division_success(self):
        assert self.calc.division(self, 24, 6) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 33, 1) == 32

    def test_adding_success(self):
        assert self.calc.adding(self, 7, 7) == 14

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def teardown(self):
        print ('Выполнение метода Teardown')
