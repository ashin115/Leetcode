import os
import unittest

def discover_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

if __name__ == '__main__':
    tests = discover_tests()
    test_runner = unittest.TextTestRunner(stream=open('test_output.txt', 'w'), verbosity=2)
    test_runner.run(tests)
    with open('test_output.txt', 'r') as f:
        print(f.read())
