from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    # python 2.X version
    from urllib2 import urlopen
except ImportError:
    # python 3.X version
    from urllib.request import urlopen

import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

response = urlopen(json_url)

req = response.read()

with open('//Users/KellerZhang/Downloads/btc_close_2017_urllib.json','wb') as f:
    f.write(req)

file_urllib=json.loads(req)
print(file_urllib)