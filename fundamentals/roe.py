import tushare
from datastorage.mongo import writetomongo

stocks = tushare.get_report_data(2016,1)
writetomongo(stocks)

