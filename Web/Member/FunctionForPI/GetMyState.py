import json
import requests
import time

def MyState(BMBC):
        while True:
            r = requests.get('http://localhost:8000/Member/State/')

            #mystate = r[BMBC]
            print(r)
            #if mystate!='0':
             #   return mystate
            time.sleep(5)