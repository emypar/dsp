# Hint:  use Google to find python function

from datetime import \
  datetime, timedelta
import locale

def td(d_start, d_stop, fmt, lc_time=None):
  """Return timedelta for d_start..d_end using fmt format

     If date names are involved (month, day of week) set LC_TIME
     locale as needed.

  """

  if lc_time:
    lc_time_sav = locale.getlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_TIME, lc_time)
  delta = datetime.strptime(d_stop, fmt) \
          - datetime.strptime(d_start, fmt)
  if lc_time:
    locale.setlocale(locale.LC_TIME, lc_time_sav)
  return delta


####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
print("a) num_days = {}".format(td(date_start, date_stop,
                                   '%m-%d-%Y').days))

####b)
date_start = '12312013'
date_stop = '05282015'
print("b) num_days = {}".format(td(date_start, date_stop,
                                   '%m%d%Y').days))

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
print("c) num_days = {}".format(td(date_start, date_stop,
                                   '%d-%b-%Y', 'en_US.utf8').days))

