from biplist import *
import os
from test_utils import *
import unittest

class TestInvalidPlistFile(unittest.TestCase):
    def setUp(self):
        pass
    def test_empty_file(self):
        try:
            readPlist(fixture_path('empty_file.plist'))
            self.fail("Should not successfully read empty plist.")
        except NotBinaryPlistException, e:
            pass
        except InvalidPlistException, e:
            pass
        
if __name__ == '__main__':
    unittest.main()