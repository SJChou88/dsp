# Hint:  use Google to find python function
from datetime import datetime
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_format = "%m-%d-%Y"
delta = datetime.strptime(date_stop, date_format) - datetime.strptime(date_start,date_format)
delta.days
####b)  
date_start = '12312013'  
date_stop = '05282015'
date_format2 = "%m%d%Y"
delta2 = datetime.strptime(date_stop, date_format2) - datetime.strptime(date_start,date_format2)
delta2.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_format3 = "%d-%b-%Y"
delta3 = datetime.strptime(date_stop, date_format3) - datetime.strptime(date_start,date_format3)
delta3.days