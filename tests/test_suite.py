import unittest

tests = unittest.TestLoader().discover(".", pattern="test_*.py")
results = unittest.TextTestRunner(verbosity=1).run(tests)
print(results)