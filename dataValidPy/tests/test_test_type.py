import unittest
import pandas as pd

from dataValidPy.test_utils import test_pass, test_fail
from dataValidPy.test_type import test_type_class

class TypesTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):
 
        super(TypesTestClass, self).__init__(*args, **kwargs)

        df = pd.DataFrame({"col1": [1,2,3,4],
                           "col2": ["a", "b", "c", "d"],
                           "col3": [True, True, False, True],
                           "col4": [1.0, 2.0, 3.0, 4.0],
                           "col5": ["2014-12-04 04:07:59", "2016-11-07 05:56:31", "2018-05-21 03:40:23", "2009-01-31 12:45:90"],
                           "col6": ["2014-12-04", "2016-11-07", "2018-05-21", "2009-01-31"]})

        self.ttt1 = test_type_class(df.col1, "INTEGER")
        self.ttt2 = test_type_class(df.col2, "INTEGER")
        self.ttt3 = test_type_class(df.col3, "INTEGER")
        self.ttt4 = test_type_class(df.col4, "INTEGER")

        self.ttt5 = test_type_class(df.col1, "FLOAT")
        self.ttt6 = test_type_class(df.col2, "FLOAT")
        self.ttt7 = test_type_class(df.col3, "FLOAT")
        self.ttt8 = test_type_class(df.col4, "FLOAT")

        self.ttt9 = test_type_class(df.col1, "BOOLEAN")
        self.ttt10 = test_type_class(df.col2, "BOOLEAN")
        self.ttt11 = test_type_class(df.col3, "BOOLEAN")
        self.ttt12 = test_type_class(df.col4, "BOOLEAN")

        self.ttt13 = test_type_class(df.col1, "CHAR_STRING")
        self.ttt14 = test_type_class(df.col2, "CHAR_STRING")
        self.ttt15 = test_type_class(df.col3, "CHAR_STRING")
        self.ttt16 = test_type_class(df.col4, "CHAR_STRING")

        self.ttt17 = test_type_class(df.col1, "NUMBER")
        self.ttt18 = test_type_class(df.col2, "NUMBER")
        self.ttt19 = test_type_class(df.col3, "NUMBER")
        self.ttt20 = test_type_class(df.col4, "NUMBER")

    def test_test_type(self):

        self.assertTrue(hasattr(self.ttt1, "td"))
        self.assertEqual(self.ttt1.ti, test_pass().ti)
        self.assertEqual(self.ttt1.tm, test_pass().tm)
    
        self.assertTrue(hasattr(self.ttt2, "td"))
        self.assertEqual(self.ttt2.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt2.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt3, "td"))
        self.assertEqual(self.ttt3.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt3.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt4, "td"))
        self.assertEqual(self.ttt4.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt4.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt5, "td"))
        self.assertEqual(self.ttt5.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt5.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt6, "td"))
        self.assertEqual(self.ttt6.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt6.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt7, "td"))
        self.assertEqual(self.ttt7.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt7.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt8, "td"))
        self.assertEqual(self.ttt8.ti, test_pass().ti)
        self.assertEqual(self.ttt8.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt9, "td"))
        self.assertEqual(self.ttt9.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt9.tm, test_pass().tm)
    
        self.assertTrue(hasattr(self.ttt10, "td"))
        self.assertEqual(self.ttt10.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt10.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt11, "td"))
        self.assertEqual(self.ttt11.ti, test_pass().ti)
        self.assertEqual(self.ttt11.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt12, "td"))
        self.assertEqual(self.ttt12.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt12.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt13, "td"))
        self.assertEqual(self.ttt13.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt13.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt14, "td"))
        self.assertEqual(self.ttt14.ti, test_pass().ti)
        self.assertEqual(self.ttt14.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt15, "td"))
        self.assertEqual(self.ttt15.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt15.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt16, "td"))
        self.assertEqual(self.ttt16.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt16.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt17, "td"))
        self.assertEqual(self.ttt17.ti, test_pass().ti)
        self.assertEqual(self.ttt17.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt18, "td"))
        self.assertEqual(self.ttt18.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt18.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt19, "td"))
        self.assertEqual(self.ttt19.ti, test_fail("blah").ti)
        self.assertNotEqual(self.ttt19.tm, test_pass().tm)

        self.assertTrue(hasattr(self.ttt20, "td"))
        self.assertEqual(self.ttt20.ti, test_pass().ti)
        self.assertEqual(self.ttt20.tm, test_pass().tm)
