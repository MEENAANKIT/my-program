import json
import requests
from pprint import pprint
a=requests.get("https://meet.google.com/afm-ipwd-jvv").text
c=json.loads(a)
for i in c:
    pprint(i)
