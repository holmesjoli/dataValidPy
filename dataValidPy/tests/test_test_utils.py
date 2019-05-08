import unittest
import pandas as pd

from dataValidPy.test_utils import test_pass_ti, test_pass_tm, test_pass, \
     test_warn_ti, test_warn_tm, test_warn, test_fail_ti, test_fail_tm, test_fail, df_setUp, \
     col_setUp

class UtilsTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):

        super(UtilsTestClass, self).__init__(*args, **kwargs)

        self.df_dct = {"col1": [1,2,3,4],
                       "col2": ["a", "b", "c", "d"]}

        self.df = pd.DataFrame(self.df_dct)

        self.tp_ti = test_pass_ti()
        self.tw_ti = test_warn_ti()
        self.tf_ti = test_fail_ti() 

        self.tp_tm = test_pass_tm()
        self.tw_tm = test_warn_tm(tm = "blah")
        self.tf_tm = test_fail_tm(tm = "blah") 

        self.tp = test_pass()
        self.tw = test_warn(tm = "blah")
        self.tf = test_fail(tm = "blah")

    def ti(self, tp, tw, tf):
        self.assertTrue(hasattr(tp, "ti"))
        self.assertTrue(hasattr(tw, "ti"))
        self.assertTrue(hasattr(tf, "ti"))
    
    def tm(self, tp, tw, tf):
        self.assertTrue(hasattr(tp, "tm"))
        self.assertTrue(hasattr(tw, "tm"))
        self.assertTrue(hasattr(tf, "tm"))

    def test_indicator(self):

        self.ti(self.tp_ti, self.tw_ti, self.tf_ti)
        self.tm(self.tp_tm, self.tw_tm, self.tf_tm)
        self.ti(self.tp, self.tw, self.tf)
        self.tm(self.tp, self.tw, self.tf)

    def test_df_setUp(self):
        self.df_setUp = df_setUp(self.df)

        self.assertTrue(hasattr(self.df_setUp, "df"))
        self.assertTrue(hasattr(self.df_setUp, "columns"))
        self.assertTrue(hasattr(self.df_setUp, "n_row"))
        self.assertTrue(hasattr(self.df_setUp, "n_col"))
    
    def test_test_col_setUp(self):
        col_setUp1 = col_setUp(self.df.col1)
        col_setUp2 = col_setUp(self.df.col2)

        self.assertTrue(hasattr(col_setUp1, "col"))
        self.assertTrue(hasattr(col_setUp1, "col_type"))
        self.assertTrue(hasattr(col_setUp1, "col_len"))

        self.assertTrue(hasattr(col_setUp1, "col_int"))
        self.assertTrue(hasattr(col_setUp1, "col_flt"))
        self.assertTrue(hasattr(col_setUp1, "col_str"))

        self.assertTrue(hasattr(col_setUp1, "uni_values"))
        self.assertTrue(hasattr(col_setUp1, "len_uni_values"))

        self.assertTrue(hasattr(col_setUp1, "min"))
        self.assertTrue(hasattr(col_setUp1, "max"))
        self.assertTrue(hasattr(col_setUp1, "mean"))
        self.assertTrue(hasattr(col_setUp1, "median"))

        self.assertFalse(hasattr(col_setUp2, "min"))
        self.assertFalse(hasattr(col_setUp2, "max"))
        self.assertFalse(hasattr(col_setUp2, "mean"))
        self.assertFalse(hasattr(col_setUp2, "median"))
        