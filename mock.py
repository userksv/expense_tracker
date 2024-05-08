from unittest.mock import MagicMock

class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

real = ProductionClass()
real.something = MagicMock()
print(real.method())
print(real.something.assert_called_once_with(1, 2, 3))