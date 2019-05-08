import pandas as pd

from dataValidPy.test_utils import test_pass, test_fail, col_setUp, cls_to_df

class test_unique_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Initiates the test class to test the uniqueness of a column
        :param series: the column to test
        :type series: pandas series
        """
        self.td = "Unique Values"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Not Unique"

    def _test(self):
        if self.col_len == self.len_uni_values:
            test_pass.__init__(self)

class test_values_class(col_setUp, test_fail):

    def __init__(self, series, expc_values):
        """
        Initiates the test class to test the values of a column
        :param series: the column to test
        :type series: pandas series
        :param expc_values: the expected values
        :type expc_values: list
        """
        self.td = "Expected Values"
        self.expc_values = expc_values
        col_setUp.__init__(self, series)

        self.add_values = set(self.uni_values) - set(self.expc_values)

        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        add_values_str = "\n".join(map(str, self.add_values))
        return "Additional values in col:{}".format(add_values_str)

    def _test(self):
        if len(self.add_values) == 0:
            test_pass.__init__(self)

class test_null_values_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Tests to see if there are any null values
        :param series: the column to test
        :type series: pandas series
        """
        self.td = "Null Values"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "Contains null values")

        self._test()

    def _test(self):
        if pd.notnull(self.col).all():
            test_pass.__init__(self)

@cls_to_df
def test_unique(series):
    return test_unique_class(series)

@cls_to_df
def test_values(series, expc_values):
    return test_values_class(series, expc_values)

@cls_to_df
def test_null_values(series):
    return test_null_values_class(series)