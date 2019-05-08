import unittest
import pandas as pd

from dataValidPy.test_utils import test_pass, test_fail, test_warn
from dataValidPy.test_df import test_expc_cols_class, test_unexpc_cols_class

class DfTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):

        super(DfTestClass, self).__init__(*args, **kwargs)

        self.df_dct1 = {"col1": [2,6,5],
                        "col2": ["x", "y", "z"],
                        "col3": [True, False, True]}

        self.df_dct2 = {"col1": [2,6,5],
                        "col2": ["x", "y", "z"]}

        self.df_dct3 = {"col1": [2,6,5],
                        "col2": ["x", "y", "z"],
                        "col3": [True, False, True],
                        "col4": [7, 8, 9]}

        self.df1 = pd.DataFrame(self.df_dct1)
        self.df2 = pd.DataFrame(self.df_dct2)
        self.df3 = pd.DataFrame(self.df_dct3)

        self.expc_cols = ["col1", "col2", "col3"]

        self.tec1 = test_expc_cols_class(self.df1, self.expc_cols)
        self.tec2 = test_expc_cols_class(self.df2, self.expc_cols)
        self.tec3 = test_expc_cols_class(self.df3, self.expc_cols)

        self.tuc1 = test_unexpc_cols_class(self.df1, self.expc_cols)
        self.tuc2 = test_unexpc_cols_class(self.df2, self.expc_cols)
        self.tuc3 = test_unexpc_cols_class(self.df3, self.expc_cols)

    def test_test_expc_cols(self):
        self.assertTrue(hasattr(self.tec1, "td"))
        self.assertEqual(self.tec1.ti, test_pass().ti)
        self.assertEqual(self.tec1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tec2, "td"))
        self.assertEqual(self.tec2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tec2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tec3, "td"))
        self.assertEqual(self.tec3.ti, test_pass().ti)
        self.assertEqual(self.tec3.tm, test_pass().tm)

    def test_test_unexpc_cols(self):
        self.assertTrue(hasattr(self.tuc1, "td"))
        self.assertEqual(self.tuc1.ti, test_pass().ti)
        self.assertEqual(self.tuc1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tuc2, "td"))
        self.assertEqual(self.tuc2.ti, test_pass().ti)
        self.assertEqual(self.tuc2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tuc3, "td"))
        self.assertEqual(self.tuc3.ti, test_warn("blah").ti)
        self.assertNotEqual(self.tuc3.tm, test_pass().tm)