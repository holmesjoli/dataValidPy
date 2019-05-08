import unittest
import pandas as pd

from dataValidPy.test_numeric_col import test_less_than_value_class, \
    test_less_than_or_equal_value_class, \
    test_greater_than_value_class, test_greater_than_or_equal_value_class, \
    test_exclu_value_range_class, test_inclu_value_range_class, \
    test_exclu_lower_inclu_upper_range_class, test_inclu_lower_exclu_upper_range_class

from dataValidPy.test_utils import test_pass, test_fail

class NumericColsTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):
 
        super(NumericColsTestClass, self).__init__(*args, **kwargs)

        self.df_dct = {"col1": [2, 6, 5, 7, 8, 9, 10],
                       "col2": [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],
                       "col3": ["a", "b", "c", "d", "e", "f", "g"]}

        self.df = pd.DataFrame(self.df_dct)

        self.tltv1 = test_less_than_value_class(self.df.col1, 11)
        self.tltv2 = test_less_than_value_class(self.df.col1, 10)
        self.tltv3 = test_less_than_value_class(self.df.col2, 1.9)
        self.tltv4 = test_less_than_value_class(self.df.col2, 1.8)

        self.tltev1 = test_less_than_or_equal_value_class(self.df.col1, 11)
        self.tltev2 = test_less_than_or_equal_value_class(self.df.col1, 10)
        self.tltev3 = test_less_than_or_equal_value_class(self.df.col1, 9)
        self.tltev4 = test_less_than_or_equal_value_class(self.df.col2, 1.9)
        self.tltev5 = test_less_than_or_equal_value_class(self.df.col2, 1.8)
        self.tltev6 = test_less_than_or_equal_value_class(self.df.col2, 1.7)

        self.tgtv1 = test_greater_than_value_class(self.df.col1, 1)
        self.tgtv2 = test_greater_than_value_class(self.df.col1, 2)
        self.tgtv3 = test_greater_than_value_class(self.df.col2, 1.1)
        self.tgtv4 = test_greater_than_value_class(self.df.col2, 1.2)

        self.tgtev1 = test_greater_than_or_equal_value_class(self.df.col1, 1)
        self.tgtev2 = test_greater_than_or_equal_value_class(self.df.col1, 2)
        self.tgtev3 = test_greater_than_or_equal_value_class(self.df.col1, 3)
        self.tgtev4 = test_greater_than_or_equal_value_class(self.df.col2, 1.1)
        self.tgtev5 = test_greater_than_or_equal_value_class(self.df.col2, 1.2)
        self.tgtev6 = test_greater_than_or_equal_value_class(self.df.col2, 1.3)

        self.tivr1 = test_inclu_value_range_class(self.df.col1, 2, 10)
        self.tivr2 = test_inclu_value_range_class(self.df.col1, 2, 11)
        self.tivr3 = test_inclu_value_range_class(self.df.col1, 1, 10)
        self.tivr4 = test_inclu_value_range_class(self.df.col1, 1, 11)
        self.tivr5 = test_inclu_value_range_class(self.df.col1, 2, 9)
        self.tivr6 = test_inclu_value_range_class(self.df.col1, 3, 10)
        self.tivr7 = test_inclu_value_range_class(self.df.col1, 3, 9)

        self.tevr1 = test_exclu_value_range_class(self.df.col1, 1, 11)
        self.tevr2 = test_exclu_value_range_class(self.df.col1, 2, 11)
        self.tevr3 = test_exclu_value_range_class(self.df.col1, 1, 10)
        self.tevr4 = test_exclu_value_range_class(self.df.col1, 2, 11)

        self.teliu1 = test_exclu_lower_inclu_upper_range_class(self.df.col1, 1, 11)
        self.teliu2 = test_exclu_lower_inclu_upper_range_class(self.df.col1, 1, 10)
        self.teliu3 = test_exclu_lower_inclu_upper_range_class(self.df.col1, 2, 10)
        self.teliu4 = test_exclu_lower_inclu_upper_range_class(self.df.col1, 2, 11)

        self.tileu1 = test_inclu_lower_exclu_upper_range_class(self.df.col1, 1, 11)
        self.tileu2 = test_inclu_lower_exclu_upper_range_class(self.df.col1, 2, 11)
        self.tileu3 = test_inclu_lower_exclu_upper_range_class(self.df.col1, 1, 10)
        self.tileu4 = test_inclu_lower_exclu_upper_range_class(self.df.col1, 2, 10)

    def test_test_lt_value_class(self):
        self.assertTrue(hasattr(self.tltv1, "td"))
        self.assertEqual(self.tltv1.ti, test_pass().ti)
        self.assertEqual(self.tltv1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltv2, "td"))
        self.assertEqual(self.tltv2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tltv2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltv3, "td"))
        self.assertEqual(self.tltv3.ti, test_pass().ti)
        self.assertEqual(self.tltv3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltv4, "td"))
        self.assertEqual(self.tltv4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tltv4.tm, test_pass().tm)

    def test_test_lte_value_class(self):
        self.assertTrue(hasattr(self.tltev1, "td"))
        self.assertEqual(self.tltev1.ti, test_pass().ti)
        self.assertEqual(self.tltev1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltev2, "td"))
        self.assertEqual(self.tltev2.ti, test_pass().ti)
        self.assertEqual(self.tltev2.tm, test_pass().tm)
        
        self.assertTrue(hasattr(self.tltev3, "td"))
        self.assertEqual(self.tltev3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tltev3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltev4, "td"))
        self.assertEqual(self.tltev4.ti, test_pass().ti)
        self.assertEqual(self.tltev4.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tltev5, "td"))
        self.assertEqual(self.tltev5.ti, test_pass().ti)
        self.assertEqual(self.tltev5.tm, test_pass().tm)
        
        self.assertTrue(hasattr(self.tltev6, "td"))
        self.assertEqual(self.tltev6.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tltev6.tm, test_pass().tm)

    def test_test_gt_value_class(self):
        self.assertTrue(hasattr(self.tgtv1, "td"))
        self.assertEqual(self.tgtv1.ti, test_pass().ti)
        self.assertEqual(self.tgtv1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtv2, "td"))
        self.assertEqual(self.tgtv2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tgtv2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtv3, "td"))
        self.assertEqual(self.tgtv3.ti, test_pass().ti)
        self.assertEqual(self.tgtv3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtv4, "td"))
        self.assertEqual(self.tgtv4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tgtv4.tm, test_pass().tm)

    def test_test_gte_value_class(self):
        self.assertTrue(hasattr(self.tgtev1, "td"))
        self.assertEqual(self.tgtev1.ti, test_pass().ti)
        self.assertEqual(self.tgtev1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtev2, "td"))
        self.assertEqual(self.tgtev2.ti, test_pass().ti)
        self.assertEqual(self.tgtev2.tm, test_pass().tm)
        
        self.assertTrue(hasattr(self.tgtev3, "td"))
        self.assertEqual(self.tgtev3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tgtev3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtev4, "td"))
        self.assertEqual(self.tgtev4.ti, test_pass().ti)
        self.assertEqual(self.tgtev4.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtev5, "td"))
        self.assertEqual(self.tgtev5.ti, test_pass().ti)
        self.assertEqual(self.tgtev5.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tgtev6, "td"))
        self.assertEqual(self.tgtev6.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tgtev6.tm, test_pass().tm)

    def test_test_inclu_value_range_class(self):
        self.assertTrue(hasattr(self.tivr1, "td"))
        self.assertEqual(self.tivr1.ti, test_pass().ti)
        self.assertEqual(self.tivr1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr2, "td"))
        self.assertEqual(self.tivr2.ti, test_pass().ti)
        self.assertEqual(self.tivr2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr3, "td"))
        self.assertEqual(self.tivr3.ti, test_pass().ti)
        self.assertEqual(self.tivr3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr4, "td"))
        self.assertEqual(self.tivr4.ti, test_pass().ti)
        self.assertEqual(self.tivr4.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr5, "td"))
        self.assertEqual(self.tivr5.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tivr5.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr6, "td"))
        self.assertEqual(self.tivr6.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tivr6.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tivr7, "td"))
        self.assertEqual(self.tivr7.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tivr7.tm, test_pass().tm)

    def test_test_exclu_value_range_class(self):
        self.assertTrue(hasattr(self.tevr1, "td"))
        self.assertEqual(self.tevr1.ti, test_pass().ti)
        self.assertEqual(self.tevr1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tevr2, "td"))
        self.assertEqual(self.tevr2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tevr2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tevr3, "td"))
        self.assertEqual(self.tevr3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tevr3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tevr4, "td"))
        self.assertEqual(self.tevr4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tevr4.tm, test_pass().tm)

    def test_test_exclu_lower_inclu_upper_range_class(self):
        self.assertTrue(hasattr(self.teliu1, "td"))
        self.assertEqual(self.teliu1.ti, test_pass().ti)
        self.assertEqual(self.teliu1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.teliu2, "td"))
        self.assertEqual(self.teliu2.ti, test_pass().ti)
        self.assertEqual(self.teliu2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.teliu3, "td"))
        self.assertEqual(self.teliu3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.teliu3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.teliu4, "td"))
        self.assertEqual(self.teliu4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.teliu4.tm, test_pass().tm)

    def test_test_inclu_lower_exclu_upper_range_class(self):
        self.assertTrue(hasattr(self.tileu1, "td"))
        self.assertEqual(self.tileu1.ti, test_pass().ti)
        self.assertEqual(self.tileu1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tileu2, "td"))
        self.assertEqual(self.tileu2.ti, test_pass().ti)
        self.assertEqual(self.tileu2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tileu3, "td"))
        self.assertEqual(self.tileu3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tileu3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tileu4, "td"))
        self.assertEqual(self.tileu4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tileu4.tm, test_pass().tm)