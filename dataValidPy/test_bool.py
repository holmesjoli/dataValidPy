from dataValidPy.test_utils import test_pass, test_fail, col_setUp, cls_to_df

class test_all_true_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Initiates the test class for test all true
        :param series: the column to test
        :type series: pandas series
        """
        self.td = "All true"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "Not all True")

        self._test()

    def _test(self):

        if self.col.all():
            test_pass.__init__(self)

class test_all_false_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Initiates the test class for test all false
        :param series: the column to test
        :type series: pandas series
        """

        self.td = "All false"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "Not all False")

        self._test()

    def _test(self):

        if (self.col == False).all():
            test_pass.__init__(self)

class test_any_true_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Initiates the test class for test any true
        :param series: the column to test
        :type series: pandas series
        """

        self.td = "Any True"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "All False")

        self._test()

    def _test(self):

        if self.col.any():
            test_pass.__init__(self)

class test_any_false_class(col_setUp, test_fail):

    def __init__(self, series):
        """
        Initiates the test class for test any false
        :param series: the column to test
        :type series: pandas series
        """

        self.td = "Any False"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "All True")

        self._test()

    def _test(self):

        if (self.col == False).any():
            test_pass.__init__(self)

@cls_to_df
def test_all_true(series):
    return test_all_true_class(series)

@cls_to_df
def test_all_false(series):
    return test_all_false_class(series)

@cls_to_df
def test_any_true(series):
    return test_any_true_class(series)

@cls_to_df
def test_any_false(series):
    return test_any_false_class(series)
    