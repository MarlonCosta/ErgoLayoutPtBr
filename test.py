import unittest
import os
from main import *

unittest.TestLoader.sortTestMethodsUsing = None


class TestFileManagement(unittest.TestCase):
    path = r'c:\Users\mrlnr\Documents\test_log.json'

    def test_creating_logfile(self):
        if os.path.exists(self.path):
            os.remove(self.path)

        data = load_log(self.path)
        test_dict = {}
        self.assertDictEqual(data, test_dict)

    def test_loading_data(self):
        with open(self.path, "w") as file:
            json.dump({"a": 1, "b": 2, "c": 3}, file)

        data = load_log(self.path)
        test_dict = {"a": 1, "b": 2, "c": 3}
        self.assertDictEqual(data, test_dict)
