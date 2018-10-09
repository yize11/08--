import re
s = '12abc45_1@163.com'
ret = re.match(r'\w{4,20}@163\.com',s)
if ret:
    print('满足')
