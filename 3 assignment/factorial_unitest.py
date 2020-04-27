import unittest
import doctest
import factorial_doctest

# Paverskite dokumentacinius testus unittest'ais
def run_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(factorial_doctest))
    return tests

if __name__ == "__main__":
    unittest.main()