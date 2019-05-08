import pandas as pd
from dataValidPy.test_utils import test_pass, test_fail, test_warn, df_setUp, cls_to_df

class test_expc_cols_class(df_setUp, test_fail):

    def __init__(self, df, expc_cols):
        """
        Initiates the test class for the expected cols function
        :param df: the dataframe to test
        :type df: a pandas dataframe
        :param expc_cols: the names of the expected columns
        :type expc_cols: list
        """

        self.td = "Expected cols"
        self.expc_cols = pd.Series(expc_cols)

        df_setUp.__init__(self, df)

        self.missing_cols = self.expc_cols[(self.expc_cols.isin(self.df.columns)) == False]
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Expected columns are missing: {}".format(", ".join(self.missing_cols))

    def _test(self):
        if len(self.missing_cols) == 0:
            test_pass.__init__(self)

class test_unexpc_cols_class(df_setUp, test_warn):

    def __init__(self, df, expc_cols):
        """
        Initiates the test class for the unexpected cols test function
        :param df: the dataframe to test
        :type df: a pandas dataframe
        :param expc_cols: the names of the expected columns
        :type expc_cols: list
        """

        self.td = "Unexpected cols"
        self.expc_cols = pd.Series(expc_cols)

        df_setUp.__init__(self, df)

        self.extra_cols = self.df.columns[self.df.columns.isin(self.expc_cols) == False]

        test_warn.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Extra columns: {}".format(", ".join(self.extra_cols))

    def _test(self):
        if len(self.extra_cols) == 0:
            test_pass.__init__(self)

@cls_to_df
def test_expc_cols(df, expc_cols):
    return test_expc_cols_class(df, expc_cols)

@cls_to_df
def test_unexpc_cols(df, expc_cols):
    return test_unexpc_cols_class(df, expc_cols)
