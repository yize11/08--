import re
s = """<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">"""
ret = re.match('.+?"(.+?)"',s).group(1)
print(ret)
ret1 = re.search(r"https://.+?\.jpg",s)
print(ret1.group())
