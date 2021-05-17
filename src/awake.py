import pyautogui as pa
import time
import sys
from datetime import datetime
pa.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    x , y = pa.position()
    pa.moveTo(x+5, y+5)
    pa.press("shift")
    pa.press("ctrl")
    print("Movement made at {}".format(datetime.now().time()))
