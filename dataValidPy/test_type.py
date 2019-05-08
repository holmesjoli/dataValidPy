import numpy as np
from dataValidPy.test_utils import test_pass, test_fail, col_setUp, cls_to_df

class test_type_class(col_setUp):

    def __init__(self, series, expc_type):
        """
        Initiates test type class. Classes tests if the column meets the expected type condition. 
        :param series: the column to test
        :type series: pandas series
        :param expc_type: the expected type of the column
        :type expc_type: string
        """

        col_setUp.__init__(self, series)

        self.td = "Test column type"
        self.expc_type = self.get_type(expc_type)

        test_fail.__init__(self, tm = self._test_message())

        self._test()
    
    def _test_message(self):
        return "Column is of type {}, but expected type is {}".format(self.col_type, self.expc_type)

    def _test(self):

        if self.col_type == self.expc_type:
            test_pass.__init__(self)
        elif np.issubdtype(self.col_type, self.expc_type):
            test_pass.__init__(self)

@cls_to_df
def test_type(series, col_type):
    return test_type_class(series, col_type)