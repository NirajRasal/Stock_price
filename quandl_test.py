import quandl
import numpy as np
import pandas as pd

mydata = quandl.get("FRED/GDP")

top = mydata.tail();
print(top)