import unittest
import pandas as pd
import numpy as np

from dataValidPy.test_utils import test_pass, test_fail
from dataValidPy.test_col import test_unique_class, test_values_class, test_null_values_class

class ColsTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):
 
        super(ColsTestClass, self).__init__(*args, **kwargs)

        self.df_dct = {"col1": [2, 6, 5, 7, 8, 9, 10],
                       "col2": [2, 2, 3, 5, 5, 6, 7],
                       "col3": ["a", "b", "c", "d", "e", "f", "g"],
                       "col4": ["a", "a", "b", "c", "d", "e", "f"],
                       "col5": [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],
                       "col6": [2, 2, 3, 5, 5, 6, np.nan]}

        self.df = pd.DataFrame(self.df_dct)

        self.tu1 = test_unique_class(self.df.col1)
        self.tu2 = test_unique_class(self.df.col2)
        self.tu3 = test_unique_class(self.df.col3)
        self.tu4 = test_unique_class(self.df.col4)

        self.tv1 = test_values_class(self.df.col2, [2, 3, 5, 6, 7])
        self.tv2 = test_values_class(self.df.col2, [1, 2, 3, 5, 6, 7])
        self.tv3 = test_values_class(self.df.col2, [5, 6, 7])
        self.tv4 = test_values_class(self.df.col4, ["a", "b", "c", "d", "e", "f"])
        self.tv5 = test_values_class(self.df.col4, ["a", "b", "c", "d", "e", "f", "g"])
        self.tv6 = test_values_class(self.df.col4, ["b", "c", "d", "e", "f"])

        self.tnv1 = test_null_values_class(self.df.col1)
        self.tnv2 = test_null_values_class(self.df.col6)

    def test_test_expc_uni_class(self):
        self.assertTrue(hasattr(self.tu1, "td"))
        self.assertEqual(self.tu1.ti, test_pass().ti)
        self.assertEqual(self.tu1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tu2, "td"))
        self.assertEqual(self.tu2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tu2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tu3, "td"))
        self.assertEqual(self.tu3.ti, test_pass().ti)
        self.assertEqual(self.tu3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tu4, "td"))
        self.assertEqual(self.tu4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tu4.tm, test_pass().tm)

    def test_test_expc_values_class(self):
        self.assertTrue(hasattr(self.tv1, "td"))
        self.assertEqual(self.tv1.ti, test_pass().ti)
        self.assertEqual(self.tv1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tv2, "td"))
        self.assertEqual(self.tv2.ti, test_pass().ti)
        self.assertEqual(self.tv2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tv3, "td"))
        self.assertEqual(self.tv3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tv3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tv4, "td"))
        self.assertEqual(self.tv4.ti, test_pass().ti)
        self.assertEqual(self.tv4.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tv5, "td"))
        self.assertEqual(self.tv5.ti, test_pass().ti)
        self.assertEqual(self.tv5.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tv6, "td"))
        self.assertEqual(self.tv6.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tv6.tm, test_pass().tm)

    def test_test_null_values_class(self):
        self.assertTrue(hasattr(self.tnv1, "td"))
        self.assertEqual(self.tnv1.ti, test_pass().ti)
        self.assertEqual(self.tnv1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tnv2, "td"))
        self.assertEqual(self.tnv2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tnv2.tm, test_pass().tm)
