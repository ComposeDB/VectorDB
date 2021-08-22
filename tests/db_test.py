import numpy as np

from src.config import FaissDBSettings
from src.faissdb import FaissDB

import unittest

class TestFaissDB(unittest.TestCase):

    def test_get_put_val(self):
        settings = FaissDBSettings()
        db = FaissDB(settings)
        db.create_partition('test')
        val_input = "val1"
        x = np.array([1.,2.,3.,4.])
        db.put('test', x, "val1")
        val_get = db.getVal('test', x)
        self.assertEqual(val_input, val_get)

    def test_create_index(self):
        settings = FaissDBSettings()
        db = FaissDB(settings)
        db.create_partition('test')
        db.create_index('test')

if __name__ == '__main__':
    unittest.main()