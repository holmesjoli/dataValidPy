from dataValidPy.test_utils import test_pass, test_fail, col_setUp

class test_all_true(col_setUp, test_fail):

    def __init__(self, series):

        self.td = "All true"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "Not all True")

        self._test()

    def _test(self):

        if self.col.all():
            test_pass.__init__(self)

class test_all_false(col_setUp, test_fail):

    def __init__(self, series):

        self.td = "All false"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "Not all False")

        self._test()

    def _test(self):

        if (self.col == False).all():
            test_pass.__init__(self)

class test_any_true(col_setUp, test_fail):

    def __init__(self, series):

        self.td = "Any True"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "All False")

        self._test()

    def _test(self):

        if self.col.any():
            test_pass.__init__(self)

class test_any_false(col_setUp, test_fail):

    def __init__(self, series):

        self.td = "Any False"

        col_setUp.__init__(self, series)
        test_fail.__init__(self, tm = "All True")

        self._test()

    def _test(self):

        if (self.col == False).any():
            test_pass.__init__(self)
