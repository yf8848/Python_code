#!/bin/env python

import datetime
import matplotlib.mpl_finance as finance
import matplotlib.mlab as mlab

ticker = 'IBM'
d1 = datetime.date(2013,1,1)
d2 = datetime.date.today()

price = finance.fetch_historical_yahoo_ochl(ticker, d1, d2)
r = mlab.csv2rec(price)

price.close()
r.sort()