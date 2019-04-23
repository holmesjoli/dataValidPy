import pandas as pd
import numpy as np

from dataValidPy.test_utils import test_pass, test_fail, col_setUp, cls_to_df

def numeric_error(number):
    """
    Throws an error if the number is not a number
    """
    if np.issubdtype(type(number), np.number):
        pass
    else:
        raise Exception("Number entered is not numeric")

class upper_bound(object):

    def __init__(self, upper):
        """
        Initiates the upper class
        :param upper: numeric upper bound
        :type upper: float or int
        """
        self.upper = upper
        numeric_error(self.upper)

class lower_bound(object):

    def __init__(self, lower):
        """
        Initiates the lower class
        :param lower: numeric lower bound
        :type lower: float or int
        """
        self.lower = lower
        numeric_error(self.lower)

class test_less_than_value_class(col_setUp, upper_bound, test_fail):

    def __init__(self, series, upper):
        """
        Initiates the test class for the less than value class.  
        Tests that X < upper is True
        :param series: the column to test
        :type series: pandas series
        :param upper: numeric upper bound
        :type upper: float or int
        """

        self.td = "Less than value (<)"

        col_setUp.__init__(self, series)
        upper_bound.__init__(self, upper)
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Values outside of upper bound"

    def _test(self):
        
        if self.max < self.upper:
            test_pass.__init__(self)

class test_less_than_or_equal_value_class(col_setUp, upper_bound, test_fail):

    def __init__(self, series, upper):
        """
        Initiates the test class for the less than value class.  
        Tests that X < upper is True
        :param series: the column to test
        :type series: pandas series
        :param upper: numeric upper bound
        :type upper: float or int
        """

        self.td = "Less than value (<=)"

        col_setUp.__init__(self, series)
        upper_bound.__init__(self, upper)
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Values outside of upper bound"

    def _test(self):
        if self.max <= self.upper:
            test_pass.__init__(self)

class test_greater_than_value_class(col_setUp, lower_bound, test_fail):

    def __init__(self, series, lower):
        """
        Initiates the test class for the greater than value class.  
        Tests that X > lower is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float or int
        """

        self.td = "Greater than value (>)"

        col_setUp.__init__(self, series)
        lower_bound.__init__(self, lower)
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Values outside of lower bound"

    def _test(self):
        if self.min > self.lower:
            test_pass.__init__(self)

class test_greater_than_or_equal_value_class(col_setUp, lower_bound, test_fail):

    def __init__(self, series, lower):
        """
        Initiates the test class for the greater than value class.  
        Tests that X >= lower is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float or int
        """

        self.td = "Greater than value (>)"

        col_setUp.__init__(self, series)
        lower_bound.__init__(self, lower)
        test_fail.__init__(self, tm = self._test_message())

        self._test()

    def _test_message(self):
        return "Values outside of lower bound"

    def _test(self):
        if self.min >= self.lower:
            test_pass.__init__(self)

class value_range(col_setUp, lower_bound, upper_bound, test_fail):

    def __init__(self, series, lower, upper):
        """
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float
        :param upper: numeric upper bound
        :type upper: float
        """

        col_setUp.__init__(self, series)
        lower_bound.__init__(self, lower)
        upper_bound.__init__(self, upper)
        test_fail.__init__(self, tm = self._test_message())

    def _test_message(self):
        return "Values outside of range"

class test_exclu_value_range_class(value_range):

    def __init__(self, series, lower, upper):
        """
        Initiates the test class for the exclusive values range 
        Tests that lower < X < upper is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float
        :param upper: numeric upper bound
        :type upper: float
        """

        self.td = "Exclusive Range (lower < X < upper)"
        value_range.__init__(self, series, lower, upper)
    
        self._test()
       
    def _test(self):
        if self.min > self.lower and self.max < self.upper:
            test_pass.__init__(self)

class test_inclu_value_range_class(value_range):

    def __init__(self, series, lower, upper):
        """
        Initiates the test class for the inclusive values range 
        Tests that lower <= X <= upper is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float
        :param upper: numeric upper bound
        :type upper: float
        """

        self.td = "Inclusive Range (lower <= X <= upper)"
        value_range.__init__(self, series, lower, upper)
    
        self._test()
       
    def _test(self):
        if self.min >= self.lower and self.max <= self.upper:
            test_pass.__init__(self)

class test_exclu_lower_inclu_upper_range_class(value_range):

    def __init__(self, series, lower, upper):
        """
        Initiates the test class for the values range 
        Tests that lower < X <= upper is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float
        :param upper: numeric upper bound
        :type upper: float
        """

        self.td = "Exclusive lower bound, inclusive upper bound (lower < X <= upper)"
        value_range.__init__(self, series, lower, upper)
    
        self._test()
       
    def _test(self):
        if self.min > self.lower and self.max <= self.upper:
            test_pass.__init__(self)

class test_inclu_lower_exclu_upper_range_class(value_range):

    def __init__(self, series, lower, upper):
        """
        Initiates the test class for the values range 
        Tests that lower <= X < upper is True
        :param series: the column to test
        :type series: pandas series
        :param lower: numeric lower bound
        :type lower: float
        :param upper: numeric upper bound
        :type upper: float
        """

        self.td = "Inclusive lower bound, exclusive upper bound (lower <= X < upper)"
        value_range.__init__(self, series, lower, upper)
    
        self._test()
       
    def _test(self):
        if self.min >= self.lower and self.max < self.upper:
            test_pass.__init__(self)


@cls_to_df
def test_less_than_value(series, upper):
    return test_less_than_value_class(series, upper)

@cls_to_df
def test_less_than_or_equal_value(series, upper):
    return test_less_than_or_equal_value_class(series, upper)

@cls_to_df
def test_greater_than_value(series, lower):
    return test_greater_than_value_class(series, lower)

@cls_to_df
def test_greater_than_or_equal_value(series, lower):
    return test_greater_than_or_equal_value_class(series, lower)

@cls_to_df
def test_inclu_value_range(series, lower, upper):
    return test_inclu_value_range_class(series, lower, upper)

@cls_to_df
def test_exclu_value_range(series, lower, upper):
    return test_exclu_value_range_class(series, lower, upper)

@cls_to_df
def test_exclu_lower_inclu_upper_range(series, lower, upper):
    return test_exclu_lower_inclu_upper_range(series, lower, upper)

@cls_to_df
def test_inclu_lower_exclu_upper_range(series, lower, upper):
    return test_inclu_lower_exclu_upper_range(series, lower, upper)