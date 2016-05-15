import tushare
from datastorage.mongo import writetomongo

stock = tushare.get_profit_data(2015,4)
writetomongo(stock)