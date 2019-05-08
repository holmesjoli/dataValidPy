import unittest
import pandas as pd

from dataValidPy.test_utils import test_pass, test_fail
from dataValidPy.test_bool import test_all_true, test_all_false, test_any_true, test_any_false

class BoolColsTestClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super(BoolColsTestClass, self).__init__(*args, **kwargs)

        self.df = pd.DataFrame({"col1": [True, True],
                                "col2": [False, False],
                                "col3": [True, False]})

        self.tat1 = test_all_true(self.df.col1)
        self.tat2 = test_all_true(self.df.col2)
        self.tat3 = test_all_true(self.df.col3)

        self.taf1 = test_all_false(self.df.col1)
        self.taf2 = test_all_false(self.df.col2)
        self.taf3 = test_all_false(self.df.col3)

        self.tant1 = test_any_true(self.df.col1)
        self.tant2 = test_any_true(self.df.col2)
        self.tant3 = test_any_true(self.df.col3)

        self.tanf1 = test_any_false(self.df.col1)
        self.tanf2 = test_any_false(self.df.col2)
        self.tanf3 = test_any_false(self.df.col3)

    def test_test_all_true(self):
        self.assertTrue(hasattr(self.tat1, "td"))
        self.assertEqual(self.tat1.ti, test_pass().ti)
        self.assertEqual(self.tat1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tat2, "td"))
        self.assertEqual(self.tat2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tat2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tat3, "td"))
        self.assertEqual(self.tat3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tat3.tm, test_pass().tm)

    def test_test_all_false(self):
        self.assertTrue(hasattr(self.taf1, "td"))
        self.assertEqual(self.taf1.ti, test_fail("blah").ti)
        self.assertNotEqual(self.taf1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.taf2, "td"))
        self.assertEqual(self.taf2.ti, test_pass().ti)
        self.assertEqual(self.taf2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.taf3, "td"))
        self.assertEqual(self.taf3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.taf3.tm, test_pass().tm)

    def test_test_any_true(self):
        self.assertTrue(hasattr(self.tant1, "td"))
        self.assertEqual(self.tant1.ti, test_pass().ti)
        self.assertEqual(self.tant1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tant2, "td"))
        self.assertEqual(self.tant2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tant2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tant3, "td"))
        self.assertEqual(self.tant3.ti, test_pass().ti)
        self.assertEqual(self.tant3.tm, test_pass().tm)

    def test_test_any_false(self):
        self.assertTrue(hasattr(self.tanf1, "td"))
        self.assertEqual(self.tanf1.ti, test_fail("blah").ti)
        self.assertNotEqual(self.tanf1.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tanf2, "td"))
        self.assertEqual(self.tanf2.ti, test_pass().ti)
        self.assertEqual(self.tanf2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.tant3, "td"))
        self.assertEqual(self.tant3.ti, test_pass().ti)
        self.assertEqual(self.tant3.tm, test_pass().tm)
