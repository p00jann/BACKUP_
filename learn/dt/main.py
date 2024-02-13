# import math
#
import datatable as dt
# import numpy as np
#
from datatable import f, by, sum, mean, sd

# #
# # print(dt.__version__)
# #
# # DT1 = dt.Frame(A=range(5), B=[1.7, 3.4, 0, None, -math.inf],
# #                stypes={"A": dt.int64})
# #
# # print((DT1))
# # # DT2 = dt.Frame(pandas_dataframe)
# # # DT3 = dt.Frame(numpy_array)
# #
# # DT4 = dt.fread("records.csv")
# # DT4[:, sum(f.salary), by(f.pos)]
# # DT4.sort("name")
# # print(DT4)
# #
# # np.random.seed(1)
# # NP = np.random.randn(5)
# # print(dt.Frame(NP))
#
# # from datetime import date
# #
# # source = {"dates" : [date(2000, 1, 5), date(2010, 11, 23), date(2020, 2, 29), None],
# #           "integers" : range(1, 5),
# #           "floats" : [10.0, 11.5, 12.3, -13],
# #           "strings" : ['A', 'B', None, 'D']
# #           }
# # DT = dt.Frame(source)
# # # print(DT)
# #
# # print(DT[..., 'dates'])
#
# from datatable import (dt, f, by, ifelse, update, sort,
#                        count, min, max, mean, sum, rowsum)
#
# df =  dt.Frame("""Fruit   Date       Name  Number
#                   Apples  10/6/2016  Bob     7
#                   Apples  10/6/2016  Bob     8
#                   Apples  10/6/2016  Mike    9
#                   Apples  10/7/2016  Steve  10
#                   Apples  10/7/2016  Bob     1
#                   Oranges 10/7/2016  Bob     2
#                   Oranges 10/6/2016  Tom    15
#                   Oranges 10/6/2016  Mike   57
#                   Oranges 10/6/2016  Bob    65
#                   Oranges 10/7/2016  Tony    1
#                   Grapes  10/7/2016  Bob     1
#                   Grapes  10/7/2016  Tom    87
#                   Grapes  10/7/2016  Bob    22
#                   Grapes  10/7/2016  Bob    12
#                   Grapes  10/7/2016  Tony   15""")
#
# # print(df[:, sum(f.Number), by('Fruit')])
# # print(df[:, sum(f.Number), by('Fruit', 'Name')])
# print(df[:, sum(f.Number), by(f[0])])

import pandas as pd
PD = pd.DataFrame({"A": range(1000), "B": range(500,1500) })
DT = dt.Frame(PD)
print(DT)

print(DT[:, mean(f.A), dt.by("B")])