import pandas as pd
from utilsPy.col_types import col_types

def cls_to_dct(cl):

    def wrapper():
       return {"Description": [cl().td],
               "Indicator": [cl().ti],
               "Message": [cl().tm]}

    return wrapper

def cls_to_df(cl):
    """
    Takes a class and converts the attributes to a dataframe
    """
    def wrapper(*args):
        x = cl(*args)
        return pd.DataFrame({"td": [x.td],
                             "ti": [x.ti],
                             "tm": [x.tm]})

    return wrapper

class col_level(object):

    def __init__(self):
        self.variable = ""

class df_level(object):

    def __init__(self):
        self.dataframe = ""

class test_pass_ti(object):

    def __init__(self):
        self.ti = "PASS"

class test_pass_tm(object):

    def __init__(self):
        self.tm = ""

class test_pass(test_pass_ti, test_pass_tm):

    def __init__(self):
        """
        Initiates the tests pass class
        """
        test_pass_ti.__init__(self)
        test_pass_tm.__init__(self)

class test_fail_ti(object):

    def __init__(self):
        self.ti = "ERROR"

class test_fail_tm(object):

    def __init__(self, tm):
        self.tm = tm

class test_fail(test_fail_ti, test_fail_tm):

    def __init__(self, tm):
        """
        Initiates the tests fail class
        """
        test_fail_ti.__init__(self)
        test_fail_tm.__init__(self, tm)

class test_warn_ti(object):

    def __init__(self):
        self.ti = "WARNING"

class test_warn_tm(object):

    def __init__(self, tm):
        self.tm = tm

class test_warn(test_warn_ti, test_warn_tm):

    def __init__(self, tm):
        """
        Initiates the tests warn class
        """
        test_warn_ti.__init__(self)
        test_warn_tm.__init__(self, tm)

class df_setUp(object):

    def __init__(self, df):
        """
        Initiates the dataframe setUp class, which includes dataframe specific attributes
        :param df: the dataframe to do the testing on
        :type df: a pandas dataframe
        """
        self.df = df
        self.columns = self.df.columns
        self.n_row = self.df.shape[0]
        self.n_col = self.df.shape[1]

class col_setUp(col_types):

    def __init__(self, series):
        """
        Initiates the column setUp class, which includes column specific attributes
        :param series: the column to test
        :type series: pandas series
        """
        col_types.__init__(self)

        self.col = series
        self.col_name = self.col.name
        self.col_type = self.col.dtype
        self.col_len = self.col.shape[0]

        self.col_int = col_types().test_ser_int(self.col)
        self.col_flt = col_types().test_ser_flt(self.col)
        self.col_str = col_types().test_ser_str(self.col)

        self.uni_values = self.col.unique()
        self.len_uni_values = len(self.uni_values)

        if self.col_int or self.col_flt:
            self.min = self.col.min()
            self.max = self.col.max()
            self.mean = self.col.mean()
            self.median = self.col.median()

class fail_upstream(test_fail, col_level, df_level):

    def __init__(self, cl):
        self.td = cl.td 
        test_fail.__init__(self, "Failed because upstream test failed")
        col_level.__init__(self)
        df_level.__init__(self)
     